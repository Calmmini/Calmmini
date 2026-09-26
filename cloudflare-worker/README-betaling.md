# CALMMINI — online betalen via Mollie (normale webshop)

Bestelproces: klant vult gegevens in → wordt doorgestuurd naar **Mollie**
(iDEAL, Bancontact, creditcard) → betaalt → komt terug op de bedankt-pagina.
Verzendkosten: **vast € 8,00**. Bij een geslaagde betaling komt de bestelling
automatisch per e-mail binnen op info@calmmini.nl (via je Web3Forms-sleutel).

## Stap 1 — Cloudflare Worker plaatsen
1. dash.cloudflare.com → **Workers & Pages** → **Create** → **Create Worker**.
2. Naam bijv. `calmmini-pay` → **Deploy** → **Edit code** → plak de inhoud van
   `worker.js` → **Deploy**.
3. **Settings → Variables and Secrets** en voeg toe:
   - Type **Text**: `SITE_URL` = `https://www.calmmini.nl`,
     `SHOP_EMAIL` = `info@calmmini.nl`, `SHIPPING` = `8.00`
   - Type **Secret**: `MOLLIE_API_KEY` = je Mollie key (begin met `test_...`),
     `WEB3FORMS_KEY` = je Web3Forms access key (dezelfde als op de site)
4. Kopieer je Worker-URL, bijv. `https://calmmini-pay.JOUW-SUBDOMEIN.workers.dev`

## Stap 2 — Site koppelen
Open `assets/js/app.js`, zet bovenin bij `PAY_ENDPOINT` je Worker-URL:

    var PAY_ENDPOINT = "https://calmmini-pay.JOUW-SUBDOMEIN.workers.dev";

Commit/push naar GitHub. Klaar.

## Stap 3 — Testen
Doe een bestelling → je wordt doorgestuurd naar Mollie (in testmodus kies je een
test-betaling) → na betalen kom je terug op de bedankt-pagina en komt de
bestelling per mail binnen. Werkt alles? Wissel in Cloudflare `MOLLIE_API_KEY`
om naar je **Live** key.

## Belangrijk
- Prijzen en het verzendbedrag (€8) worden in de Worker bepaald (niet in de
  browser), zodat er niet met bedragen geknoeid kan worden. Pas je prijzen aan?
  Werk dan de `PRICES`-lijst boven in `worker.js` bij en deploy opnieuw, en zet
  `SHIPPING` gelijk in `worker.js`/Cloudflare én `SHIPPING` in `assets/js/app.js`.
