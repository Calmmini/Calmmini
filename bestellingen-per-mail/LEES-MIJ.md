# Bestellingen & contactberichten per e-mail (zonder betaalsysteem)

De webshop rekent niet meer online af. In plaats daarvan:
- de klant plaatst een bestelling en ziet meteen "Bedankt voor je bestelling";
- jij ontvangt die bestelling **per e-mail op info@calmmini.nl**;
- jij stuurt de klant vervolgens zelf een betaallink + verzendkosten.

Ook het contactformulier komt via hetzelfde kanaal binnen.

Dit werkt met **Web3Forms** — een gratis dienst die formulieren naar je mail
stuurt. Geen server, geen Cloudflare, geen Mollie nodig.

## Instellen (3 minuten)
1. Ga naar https://web3forms.com
2. Vul bij "Create your Access Key" je e-mailadres **info@calmmini.nl** in en
   klik op de knop. Je krijgt direct een **Access Key** (een lange code) in je mail.
3. Open `assets/js/app.js`. Bovenin staat:

       var FORM_KEY = "";

   Zet je Access Key ertussen, bijvoorbeeld:

       var FORM_KEY = "abcd1234-5678-90ab-cdef-1234567890ab";

4. Sla op en zet het bijgewerkte `app.js` op GitHub. Klaar.

## Testen
- Doe een bestelling op je site → je ziet de bedankt-melding en er komt een
  e-mail met de bestelling binnen op info@calmmini.nl.
- Vul het contactformulier in → je ontvangt dat bericht ook per e-mail.

Zolang `FORM_KEY` leeg is, toont de site wel de bedankt-melding maar wordt er
niets verstuurd (handig om te testen vóór je koppelt).

## Let op — de oude Cloudflare Worker
De eerdere betaalkoppeling (Cloudflare + Mollie) is niet meer nodig. Je mag die
Worker in je Cloudflare-dashboard gewoon verwijderen.
