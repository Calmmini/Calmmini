# CALMMINI — automatische betaling koppelen (Mollie + e-mail)

Je site staat op GitHub Pages en je domein bij JouwWeb (CNAME). Die blijven zo.
Dit mapje voegt één klein stukje "achter de schermen" toe op **Cloudflare**,
zodat afrekenen automatisch via **Mollie/iDEAL** gaat en er automatisch mails
worden verstuurd (bestelling naar jou + bevestiging naar de klant, via **Resend**).

Je hoeft niets te programmeren — alleen accounts aanmaken en een paar velden invullen.

---

## Wat je nodig hebt
- Een **Mollie**-account (met KvK + zakelijke bankrekening voor iDEAL).
- Een **Resend**-account (gratis) voor de e-mails.
- Een **Cloudflare**-account (gratis).

---

## Stap 1 — Mollie
1. Maak een account op mollie.com en rond de verificatie af.
2. Zet de betaalmethoden aan (iDEAL, evt. Bancontact/creditcard).
3. Ga naar **Developers → API-keys** en kopieer je **API key**.
   Begin met de **Test API key** (test_...). Later wissel je naar Live (live_...).

## Stap 2 — Resend (e-mails)
1. Maak een account op resend.com.
2. Voeg je domein **calmmini.nl** toe en volg de stappen om het te verifiëren
   (je zet een paar DNS-regels — SPF/DKIM — bij je DNS-beheerder).
3. Kopieer je **API key** (re_...).
   Tip: gebruik als afzender een adres op je eigen domein, bv. bestelling@calmmini.nl.

## Stap 3 — Cloudflare Worker plaatsen (kopiëren-plakken, geen installatie)
1. Log in op dash.cloudflare.com → **Workers & Pages** → **Create** → **Create Worker**.
2. Geef 'm een naam, bv. `calmmini-pay`, en klik **Deploy**.
3. Klik **Edit code**, verwijder de voorbeeldcode en plak de inhoud van
   **worker.js** (uit dit mapje). Klik **Deploy**.
4. Ga naar **Settings → Variables**:
   - Onder **Variables** (gewoon) voeg toe:
     - `SITE_URL` = `https://www.calmmini.nl`
     - `SHOP_EMAIL` = `info@calmmini.nl`
     - `FROM_EMAIL` = `CALMMINI <bestelling@calmmini.nl>`
     - `SHIPPING` = `4.95`
   - Onder **Secrets** (Encrypt) voeg toe:
     - `MOLLIE_API_KEY` = je Mollie key (begin met test_...)
     - `RESEND_API_KEY` = je Resend key (re_...)
5. Kopieer bovenaan de **URL** van je Worker, bv.
   `https://calmmini-pay.JOUW-SUBDOMEIN.workers.dev`

## Stap 4 — De site aan de Worker koppelen
1. Open `assets/js/app.js`.
2. Bovenaan staat een blok **BETALING CONFIG**. Zet daar je Worker-URL:

       var PAY_ENDPOINT = "https://calmmini-pay.JOUW-SUBDOMEIN.workers.dev";

   Laat `SHIPPING` op `4.95` staan (of pas beide plekken samen aan: hier én
   de `SHIPPING`-variabele in Cloudflare — houd ze gelijk).
3. Commit/push naar GitHub. Klaar.

## Stap 5 — Testen
1. Doe een bestelling op je site en reken af.
2. Je wordt doorgestuurd naar Mollie (in testmodus kun je een test-betaling
   kiezen). Na betalen kom je terug op **/bestelling-geplaatst/**.
3. Controleer je mailbox: jij krijgt de bestelling, de klant de bevestiging.
4. Werkt alles? Wissel in Cloudflare de `MOLLIE_API_KEY` om naar je **Live** key.

---

## Belangrijk
- De **prijzen** en het **verzendbedrag** worden in de Worker bepaald
  (niet in de browser), zodat er niet met bedragen geknoeid kan worden.
  Pas je prijzen aan in de webshop? Werk dan de `PRICES`-lijst boven in
  `worker.js` ook bij, en deploy opnieuw.
- Dit mapje (`cloudflare-worker/`) hoeft niet per se op GitHub; het is alleen
  voor het plaatsen van de Worker. Kwaad kan het niet, er staan geen sleutels in.
- Wil je later betaalstatussen/voorraad bijhouden: dan kunnen we Cloudflare KV
  of een database toevoegen. Voor starten is dit genoeg.
