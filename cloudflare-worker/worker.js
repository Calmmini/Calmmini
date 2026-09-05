/**
 * CALMMINI — betaalkoppeling (Cloudflare Worker)
 * ------------------------------------------------------------------
 * Twee taken:
 *   POST /create-payment  -> maakt een Mollie-betaling en geeft de
 *                            checkout-URL terug (klant gaat naar iDEAL).
 *   POST /webhook         -> Mollie meldt hier de status; bij 'paid'
 *                            sturen we jou de bestelling + de klant een
 *                            bevestiging (via Resend).
 *
 * Instellen doe je met omgevingsvariabelen (zie README-betaling.md):
 *   MOLLIE_API_KEY   (secret)  test_... of live_...
 *   RESEND_API_KEY   (secret)  re_...
 *   SHOP_EMAIL       (var)     waar bestellingen heen mogen (jij)
 *   FROM_EMAIL       (var)     afzender, bv. "CALMMINI <bestelling@calmmini.nl>"
 *   SITE_URL         (var)     https://www.calmmini.nl
 *   SHIPPING         (var)     vast verzendbedrag, bv. "4.95"
 * ------------------------------------------------------------------
 */

// Server-side prijzen (bron van waarheid — de browser kan hier niet mee knoeien).
// Gegenereerd uit data.py. Pas je prijzen aan? Werk deze lijst dan ook bij.
const PRICES = {"sabon-beldi-naturel": {"name": "Sabon Beldi Naturel", "price": 8.95}, "sabon-beldi-nila": {"name": "Sabon Beldi Nila", "price": 9.95}, "sabon-beldi-eucalyptus": {"name": "Sabon Beldi Eucalyptus", "price": 9.95}, "sabon-beldi-musk": {"name": "Sabon Beldi Musk", "price": 9.95}, "sabon-beldi-aker-fassi": {"name": "Sabon Beldi Aker Fassi", "price": 9.95}, "groene-klei": {"name": "Groene Klei", "price": 9.95}, "rode-klei": {"name": "Rode Klei", "price": 9.95}, "ghassoul-roos": {"name": "Ghassoul Rose", "price": 10.95}, "ghassoul-oranjebloesem": {"name": "Ghassoul Orange Blossom", "price": 10.95}, "hammamkruiden-lichaam": {"name": "Hammamkruiden Lichaam", "price": 12.95}, "hammamkruiden-haar": {"name": "Hammamkruiden Haar", "price": 12.95}, "saffloerolie": {"name": "Saffloerolie", "price": 12.95}, "amandelolie": {"name": "Amandelolie", "price": 12.95}, "abrikozenpitolie": {"name": "Abrikozenpitolie", "price": 12.95}, "aloe-vera-olie": {"name": "Aloe Vera Olie", "price": 12.95}, "shea-butter": {"name": "Shea Butter", "price": 11.95}, "mediterraanse-scrub": {"name": "Mediterraanse Scrub", "price": 11.95}, "kessa": {"name": "Kessa Scrubhandschoen", "price": 5.95}, "puimsteen": {"name": "Puimsteen", "price": 4.95}, "mengkom": {"name": "Mengkom Set", "price": 4.95}};

const CORS = (origin) => ({
  "Access-Control-Allow-Origin": origin || "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
});

function money(n) { return (Math.round(n * 100) / 100).toFixed(2); }

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = env.SITE_URL || request.headers.get("Origin") || "*";

    if (request.method === "OPTIONS")
      return new Response(null, { headers: CORS(origin) });

    // -------- 1) betaling aanmaken --------
    if (url.pathname === "/create-payment" && request.method === "POST") {
      try {
        const body = await request.json();
        const items = Array.isArray(body.items) ? body.items : [];
        const c = body.customer || {};
        if (!items.length) return json({ error: "Lege winkelwagen" }, 400, origin);
        if (!c.email) return json({ error: "E-mailadres ontbreekt" }, 400, origin);

        // bedrag bepalen op basis van de eigen prijslijst
        let subtotal = 0;
        const lines = [];
        for (const it of items) {
          const p = PRICES[it.slug];
          const qty = Math.max(1, parseInt(it.qty, 10) || 1);
          if (!p) return json({ error: "Onbekend product: " + it.slug }, 400, origin);
          subtotal += p.price * qty;
          lines.push({ s: it.slug, n: p.name, q: qty, p: money(p.price) });
        }
        const shipping = parseFloat(env.SHIPPING || "4.95");
        const total = subtotal + shipping;

        const payload = {
          amount: { currency: "EUR", value: money(total) },
          description: "CALMMINI bestelling",
          redirectUrl: (env.SITE_URL || origin) + "/bestelling-geplaatst/",
          webhookUrl: url.origin + "/webhook",
          metadata: {
            email: c.email,
            naam: [c.voornaam, c.achternaam].filter(Boolean).join(" "),
            adres: [c.straat, c.huisnummer].filter(Boolean).join(" "),
            postcode: c.postcode || "",
            plaats: c.plaats || "",
            land: c.land || "Nederland",
            verzending: money(shipping),
            items: lines,
          },
        };

        const res = await fetch("https://api.mollie.com/v2/payments", {
          method: "POST",
          headers: {
            Authorization: "Bearer " + env.MOLLIE_API_KEY,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        });
        const data = await res.json();
        if (!res.ok) return json({ error: data.detail || "Mollie-fout" }, 502, origin);
        return json({ checkoutUrl: data._links.checkout.href }, 200, origin);
      } catch (e) {
        return json({ error: "Serverfout: " + e.message }, 500, origin);
      }
    }

    // -------- 2) webhook: status van Mollie --------
    if (url.pathname === "/webhook" && request.method === "POST") {
      try {
        const form = await request.formData();
        const id = form.get("id");
        if (!id) return new Response("no id", { status: 400 });

        const res = await fetch("https://api.mollie.com/v2/payments/" + id, {
          headers: { Authorization: "Bearer " + env.MOLLIE_API_KEY },
        });
        const pay = await res.json();

        if (pay.status === "paid") {
          await sendEmails(env, pay);
        }
        // altijd 200, anders blijft Mollie het opnieuw proberen
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
    status,
    headers: { "Content-Type": "application/json", ...CORS(origin) },
  });
}

async function sendEmails(env, pay) {
  const m = pay.metadata || {};
  const items = m.items || [];
  const rows = items
    .map((l) => `<tr><td>${l.q}×</td><td>${l.n}</td><td style="text-align:right">€ ${l.p}</td></tr>`)
    .join("");
  const bedrag = pay.amount ? pay.amount.value : "";
  const adres = `${m.naam || ""}<br>${m.adres || ""}<br>${m.postcode || ""} ${m.plaats || ""}<br>${m.land || ""}`;

  const orderHtml = `
    <h2>Nieuwe bestelling</h2>
    <p><strong>Klant:</strong> ${m.naam || ""} (${m.email || ""})</p>
    <p><strong>Adres:</strong><br>${adres}</p>
    <table>${rows}
      <tr><td></td><td>Verzending</td><td style="text-align:right">€ ${m.verzending || "0.00"}</td></tr>
      <tr><td></td><td><strong>Totaal betaald</strong></td><td style="text-align:right"><strong>€ ${bedrag}</strong></td></tr>
    </table>
    <p>Betaal-ID: ${pay.id}</p>`;

  const klantHtml = `
    <h2>Bedankt voor je bestelling bij CALMMINI</h2>
    <p>We hebben je betaling van <strong>€ ${bedrag}</strong> ontvangen en gaan je bestelling klaarmaken.</p>
    <table>${rows}
      <tr><td></td><td>Verzending</td><td style="text-align:right">€ ${m.verzending || "0.00"}</td></tr>
      <tr><td></td><td><strong>Totaal</strong></td><td style="text-align:right"><strong>€ ${bedrag}</strong></td></tr>
    </table>
    <p><strong>Bezorgadres:</strong><br>${adres}</p>
    <p>Rust voor mij. Gewoon thuis.<br>— CALMMINI Hammamrituelen</p>`;

  // naar de winkel
  await resend(env, env.SHOP_EMAIL, "Nieuwe bestelling — € " + bedrag, orderHtml);
  // naar de klant
  if (m.email) await resend(env, m.email, "Je bestelling bij CALMMINI", klantHtml);
}

async function resend(env, to, subject, html) {
  return fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: "Bearer " + env.RESEND_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ from: env.FROM_EMAIL, to: [to], subject, html }),
  });
}
