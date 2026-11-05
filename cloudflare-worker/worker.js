/**
 * CALMMINI — betaalkoppeling (Cloudflare Worker) — Mollie + bestelmail
 * ------------------------------------------------------------------
 *   POST /create-payment  -> maakt een Mollie-betaling (incl. verzending)
 *                            en geeft de checkout-URL terug (klant -> iDEAL).
 *   POST /webhook         -> Mollie meldt de status; bij 'paid' sturen we de
 *                            bestelling per e-mail naar de winkel (via Web3Forms).
 *   GET  /test-mail       -> stuurt NU een testmail en toont het resultaat in de
 *                            browser. Handig om te controleren of de mail werkt.
 *
 * Variabelen (Cloudflare -> Settings -> Variables and Secrets):
 *   MOLLIE_API_KEY   (Secret)  test_... of live_...
 *   WEB3FORMS_KEY    (Secret)  jouw Web3Forms access key
 *   SHOP_EMAIL       (Text)    info@calmmini.nl
 *   SITE_URL         (Text)    https://calmmini.nl
 *   SHIPPING         (Text)    8.00
 * ------------------------------------------------------------------
 */

// Server-side prijzen (bron van waarheid). Gegenereerd uit data.py.
const PRICES = {"sabon-beldi-naturel": {"name": "Sabon Beldi Naturel", "price": 11.95}, "sabon-beldi-nila": {"name": "Sabon Beldi Nila", "price": 13.95}, "sabon-beldi-eucalyptus": {"name": "Sabon Beldi Eucalyptus", "price": 13.95}, "sabon-beldi-musk": {"name": "Sabon Beldi Musk", "price": 13.95}, "sabon-beldi-aker-fassi": {"name": "Sabon Beldi Aker Fassi", "price": 13.95}, "groene-klei": {"name": "Groene Klei", "price": 17.95}, "rode-klei": {"name": "Rode Klei", "price": 17.95}, "ghassoul-roos": {"name": "Ghassoul Rose", "price": 13.95}, "ghassoul-oranjebloesem": {"name": "Ghassoul Orange Blossom", "price": 13.95}, "hammamkruiden-lichaam": {"name": "Hammamkruiden Lichaam", "price": 11.95}, "hammamkruiden-haar": {"name": "Hammamkruiden Haar", "price": 11.95}, "saffloerolie": {"name": "Saffloerolie", "price": 18.95}, "amandelolie": {"name": "Amandelolie", "price": 10.95}, "abrikozenpitolie": {"name": "Abrikozenpitolie", "price": 10.95}, "aloe-vera-olie": {"name": "Aloe Vera Olie", "price": 16.95}, "shea-butter": {"name": "Shea Butter", "price": 13.95}, "mediterraanse-scrub": {"name": "Mediterraanse Scrub", "price": 18.95}, "kessa": {"name": "Kessa Scrubhandschoen", "price": 4.0}, "puimsteen": {"name": "Puimsteen", "price": 4.95}, "mengkom": {"name": "Mengkom Set", "price": 4.95}};

const CORS = (o) => ({
  "Access-Control-Allow-Origin": o || "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
});
const money = (n) => (Math.round(n * 100) / 100).toFixed(2);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get("Origin") || env.SITE_URL || "*";
    if (request.method === "OPTIONS") return new Response(null, { headers: CORS(origin) });

    // --- Diagnose: stuur nu een testmail en toon het resultaat ---
    if (url.pathname === "/test-mail") {
      const key = (env.WEB3FORMS_KEY || "").trim();
      let status = "(niet verzonden)", antwoord = "(geen)";
      if (key) {
        try {
          const r = await sendMail(env, "TEST — CALMMINI bestelmail",
            "Dit is een testbericht vanuit de CALMMINI Worker.\nAls je dit ontvangt, werkt de bestelmail.");
          status = r.status; antwoord = await r.text();
        } catch (e) { antwoord = "fout: " + e.message; }
      }
      const uit =
        "WEB3FORMS_KEY aanwezig : " + (key ? "ja (" + key.length + " tekens)" : "NEE — niet ingesteld!") + "\n" +
        "SHOP_EMAIL             : " + (env.SHOP_EMAIL || "(leeg)") + "\n" +
        "Web3Forms HTTP-status  : " + status + "\n" +
        "Web3Forms antwoord     : " + antwoord + "\n";
      return new Response(uit, { status: 200, headers: { "Content-Type": "text/plain; charset=utf-8" } });
    }

    // --- Contactformulier van de site -> e-mail naar de winkel ---
    if (url.pathname === "/contact" && request.method === "POST") {
      try {
        const b = await request.json();
        const naam = (b.naam || "").toString().slice(0, 200);
        const email = (b.email || "").toString().slice(0, 200);
        const bericht = (b.bericht || "").toString().slice(0, 5000);
        const msg = "NIEUW BERICHT VIA DE WEBSITE\n\nNaam: " + naam +
                    "\nE-mail: " + email + "\n\nBericht:\n" + bericht;
        const r = await sendMail(env, "Nieuw bericht via de website — CALMMINI", msg, email);
        const ok = r.ok;
        return json({ success: ok }, ok ? 200 : 502, origin);
      } catch (e) {
        return json({ success: false, error: e.message }, 500, origin);
      }
    }

    if (url.pathname === "/create-payment" && request.method === "POST") {
      try {
        const body = await request.json();
        const items = Array.isArray(body.items) ? body.items : [];
        const c = body.customer || {};
        if (!items.length) return json({ error: "Lege winkelwagen" }, 400, origin);
        if (!c.email) return json({ error: "E-mailadres ontbreekt" }, 400, origin);
        const mollieKey = (env.MOLLIE_API_KEY || "").trim();
        if (!mollieKey) return json({ error: "MOLLIE_API_KEY ontbreekt in de Worker-instellingen" }, 500, origin);

        let subtotal = 0;
        const lines = [];
        for (const it of items) {
          const p = PRICES[it.slug];
          const qty = Math.max(1, parseInt(it.qty, 10) || 1);
          if (!p) return json({ error: "Onbekend product: " + it.slug }, 400, origin);
          subtotal += p.price * qty;
          lines.push(qty + "x " + p.name + " (€ " + money(p.price) + ")");
        }
        const afhalen = body.method === "afhalen";
        const shipping = afhalen ? 0 : parseFloat(env.SHIPPING || "8.00");
        const total = subtotal + shipping;
        const adres = afhalen
          ? "Afhalen in Amersfoort"
          : [c.straat, c.huisnummer].filter(Boolean).join(" ") + ", " +
            (c.postcode || "") + " " + (c.plaats || "") + ", " + (c.land || "Nederland");

        const payload = {
          amount: { currency: "EUR", value: money(total) },
          description: "CALMMINI bestelling",
          redirectUrl: (env.SITE_URL || origin).replace(/\/$/, "") + "/bestelling-geplaatst/" + (afhalen ? "?afhalen=1" : ""),
          webhookUrl: url.origin + "/webhook",
          metadata: {
            email: c.email,
            naam: [c.voornaam, c.achternaam].filter(Boolean).join(" "),
            methode: afhalen ? "AFHALEN (Amersfoort)" : "BEZORGEN",
            adres: adres,
            verzending: money(shipping),
            subtotaal: money(subtotal),
            items: lines.join("\n"),
          },
        };
        const res = await fetch("https://api.mollie.com/v2/payments", {
          method: "POST",
          headers: { Authorization: "Bearer " + mollieKey, "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
        const data = await res.json();
        if (!res.ok) return json({ error: data.detail || "Mollie-fout" }, 502, origin);
        return json({ checkoutUrl: data._links.checkout.href }, 200, origin);
      } catch (e) {
        return json({ error: "Serverfout: " + e.message }, 500, origin);
      }
    }

    if (url.pathname === "/webhook" && request.method === "POST") {
      try {
        const form = await request.formData();
        const id = form.get("id");
        if (!id) return new Response("no id", { status: 400 });
        const res = await fetch("https://api.mollie.com/v2/payments/" + id, {
          headers: { Authorization: "Bearer " + (env.MOLLIE_API_KEY || "").trim() },
        });
        const pay = await res.json();
        if (pay.status === "paid") {
          const subject = "Betaalde bestelling — CALMMINI (€ " + (pay.amount ? pay.amount.value : "") + ")";
          const m = pay.metadata || {};
          const body =
            "BETAALDE BESTELLING\n\n" + (m.items || "") +
            "\n\nSubtotaal: € " + (m.subtotaal || "") +
            "\nVerzending: € " + (m.verzending || "") +
            "\nTotaal betaald: € " + (pay.amount ? pay.amount.value : "") +
            "\n\nLevering: " + (m.methode || "BEZORGEN") +
            "\n\nKLANT\n" + (m.naam || "") + "\n" + (m.email || "") + "\n" + (m.adres || "") +
            "\n\nBetaal-ID: " + pay.id;
          const r = await sendMail(env, subject, body, m.email);
          console.log("mailOrder Web3Forms status:", r.status, await r.text());
        }
        return new Response("ok", { status: 200 });
      } catch (e) {
        console.log("webhook error:", e.message);
        return new Response("ok", { status: 200 });
      }
    }
    return new Response("CALMMINI payment worker", { status: 200 });
  },
};

function json(obj, status, origin) {
  return new Response(JSON.stringify(obj), {
    status, headers: { "Content-Type": "application/json", ...CORS(origin) },
  });
}

// Verstuurt een e-mail via Web3Forms naar het account van de WEB3FORMS_KEY.
function sendMail(env, subject, message, replyto) {
  return fetch("https://api.web3forms.com/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({
      access_key: (env.WEB3FORMS_KEY || "").trim(),
      subject: subject,
      from_name: "CALMMINI webshop",
      email: replyto || env.SHOP_EMAIL || "webshop@calmmini.nl",
      message: message,
    }),
  });
}
