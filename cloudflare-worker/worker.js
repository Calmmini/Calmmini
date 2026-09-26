/**
 * CALMMINI — betaalkoppeling (Cloudflare Worker) — Mollie + bestelmail
 * ------------------------------------------------------------------
 *   POST /create-payment  -> maakt een Mollie-betaling (incl. €8 verzending)
 *                            en geeft de checkout-URL terug (klant -> iDEAL).
 *   POST /webhook         -> Mollie meldt de status; bij 'paid' sturen we de
 *                            bestelling per e-mail naar de winkel (via Web3Forms).
 *
 * Variabelen (Cloudflare -> Settings -> Variables and Secrets):
 *   MOLLIE_API_KEY   (Secret)  test_... of live_...
 *   WEB3FORMS_KEY    (Secret)  jouw Web3Forms access key (zelfde als op de site)
 *   SHOP_EMAIL       (Text)    info@calmmini.nl
 *   SITE_URL         (Text)    https://www.calmmini.nl
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
    const origin = env.SITE_URL || request.headers.get("Origin") || "*";
    if (request.method === "OPTIONS") return new Response(null, { headers: CORS(origin) });

    if (url.pathname === "/create-payment" && request.method === "POST") {
      try {
        const body = await request.json();
        const items = Array.isArray(body.items) ? body.items : [];
        const c = body.customer || {};
        if (!items.length) return json({ error: "Lege winkelwagen" }, 400, origin);
        if (!c.email) return json({ error: "E-mailadres ontbreekt" }, 400, origin);

        let subtotal = 0;
        const lines = [];
        for (const it of items) {
          const p = PRICES[it.slug];
          const qty = Math.max(1, parseInt(it.qty, 10) || 1);
          if (!p) return json({ error: "Onbekend product: " + it.slug }, 400, origin);
          subtotal += p.price * qty;
          lines.push(qty + "x " + p.name + " (\u20ac " + money(p.price) + ")");
        }
        const shipping = parseFloat(env.SHIPPING || "8.00");
        const total = subtotal + shipping;

        const payload = {
          amount: { currency: "EUR", value: money(total) },
          description: "CALMMINI bestelling",
          redirectUrl: (env.SITE_URL || origin) + "/bestelling-geplaatst/",
          webhookUrl: url.origin + "/webhook",
          metadata: {
            email: c.email,
            naam: [c.voornaam, c.achternaam].filter(Boolean).join(" "),
            adres: [c.straat, c.huisnummer].filter(Boolean).join(" ") + ", " +
                   (c.postcode || "") + " " + (c.plaats || "") + ", " + (c.land || "Nederland"),
            verzending: money(shipping),
            subtotaal: money(subtotal),
            items: lines.join("\n"),
          },
        };
        const res = await fetch("https://api.mollie.com/v2/payments", {
          method: "POST",
          headers: { Authorization: "Bearer " + env.MOLLIE_API_KEY, "Content-Type": "application/json" },
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
          headers: { Authorization: "Bearer " + env.MOLLIE_API_KEY },
        });
        const pay = await res.json();
        if (pay.status === "paid") await mailOrder(env, pay);
        return new Response("ok", { status: 200 });
      } catch (e) {
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

async function mailOrder(env, pay) {
  const m = pay.metadata || {};
  const bedrag = pay.amount ? pay.amount.value : "";
  const message =
    "BETAALDE BESTELLING\n\n" + (m.items || "") +
    "\n\nSubtotaal: \u20ac " + (m.subtotaal || "") +
    "\nVerzending: \u20ac " + (m.verzending || "") +
    "\nTotaal betaald: \u20ac " + bedrag +
    "\n\nKLANT\n" + (m.naam || "") + "\n" + (m.email || "") + "\n" + (m.adres || "") +
    "\n\nBetaal-ID: " + pay.id;
  await fetch("https://api.web3forms.com/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({
      access_key: env.WEB3FORMS_KEY,
      subject: "Betaalde bestelling — CALMMINI (\u20ac " + bedrag + ")",
      from_name: "CALMMINI webshop",
      email: env.SHOP_EMAIL,
      replyto: m.email || env.SHOP_EMAIL,
      message: message,
    }),
  });
}
