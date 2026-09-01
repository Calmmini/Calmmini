# CALMMINI — Webshop

Complete, statische e-commerce webshop voor **CALMMINI** (Marokkaanse hammamverzorging).
Gebouwd als pure HTML/CSS/JS — geen build-stap of framework nodig.

## Snel bekijken (lokaal)
Vanwege de nette map-URL's (`/producten/`, `/product/…/`) kun je de site het beste
via een lokale server bekijken:

```bash
cd calmmini
python3 -m http.server 8000
# open http://localhost:8000
```

De interne links bevatten `index.html`, dus dubbelklikken op `index.html` werkt
ook — een server geeft alleen de mooiste URL's.

## Online zetten
Upload de **inhoud** van de map `calmmini/` naar de root van je webhosting of naar
een static host (Netlify, Vercel, Cloudflare Pages, GitHub Pages). Verander vóór
livegang `DOMAIN` verwijzingen: alle canonical/OG/sitemap-URL's staan nu op
`https://www.calmmini.nl`.

## Structuur
```
index.html                Home
producten/                Alle producten (met filters, sortering, zoeken)
categorie/<slug>/         Categoriepagina's (SEO-landingspagina's)
product/<slug>/           Productpagina's
winkelwagen/  afrekenen/  Winkelwagen + demo-checkout (localStorage)
blog/  blog/<slug>/       Journal (SEO-content, interne links)
over-calmmini/ contact/ veelgestelde-vragen/
verzending-en-retour/ privacybeleid/ algemene-voorwaarden/
404.html
assets/css/style.css      Design system
assets/js/data.js         Productcatalogus (voor winkelwagen/zoeken)
assets/js/app.js          Winkelwagen, filters, UI
assets/img/…              Productfoto's + sfeerbeelden
sitemap.xml  robots.txt  site.webmanifest  favicon.svg
```

Categorie-URL's:
- `/categorie/sabon-beldi/`
- `/categorie/ghassoul-klei/`
- `/categorie/hammampoeder/`
- `/categorie/verzorgingsolien/`
- `/categorie/butter-scrub/`
- `/categorie/accessoires/`

## Productfoto's
De 15 aangeleverde productfoto's zijn geplaatst en aan de juiste producten
gekoppeld. Enkele producten hadden nog geen foto en tonen daarom een nette,
merkgerichte placeholder. Vervang die 1-op-1 (zelfde bestandsnaam) in
`assets/img/products/` — aanbevolen: staand, ~900×1125 px, `.jpg`:

- `hammamkruiden-haar.jpg` — Hammamkruiden Haar
- `amandelolie.jpg` — Amandelolie
- `mediterraanse-scrub.jpg` — Mediterraanse Scrub
- `kessa.jpg` — Kessa Scrubhandschoen
- `puimsteen.jpg` — Puimsteen
- `mengkom.jpg` — Mengkom Set

Alle productbestanden (echte foto's zijn niet gemarkeerd):

- `sabon-beldi-naturel.jpg` — Sabon Beldi Naturel
- `sabon-beldi-nila.jpg` — Sabon Beldi Nila
- `sabon-beldi-eucalyptus.jpg` — Sabon Beldi Eucalyptus
- `sabon-beldi-musk.jpg` — Sabon Beldi Musk
- `sabon-beldi-aker-fassi.jpg` — Sabon Beldi Aker Fassi
- `groene-klei.jpg` — Groene Klei
- `rode-klei.jpg` — Rode Klei
- `ghassoul-roos.jpg` — Ghassoul Rose
- `ghassoul-oranjebloesem.jpg` — Ghassoul Orange Blossom
- `hammamkruiden-lichaam.jpg` — Hammamkruiden Lichaam
- `hammamkruiden-haar.jpg` — Hammamkruiden Haar  **(nog placeholder)**
- `saffloerolie.jpg` — Saffloerolie
- `amandelolie.jpg` — Amandelolie  **(nog placeholder)**
- `abrikozenpitolie.jpg` — Abrikozenpitolie
- `aloe-vera-olie.jpg` — Aloe Vera Olie
- `shea-butter.jpg` — Shea Butter
- `mediterraanse-scrub.jpg` — Mediterraanse Scrub  **(nog placeholder)**
- `kessa.jpg` — Kessa Scrubhandschoen  **(nog placeholder)**
- `puimsteen.jpg` — Puimsteen  **(nog placeholder)**
- `mengkom.jpg` — Mengkom Set  **(nog placeholder)**

Categorie- en sfeerbeelden staan in `assets/img/categories/` (opgebouwd uit de
echte productfoto's) en de losse `assets/img/*.jpg` (hero.jpg, ritueel.jpg,
verhaal.jpg).

## Nog in te vullen
De echte productgegevens uit het overzicht (ingrediënten/basis, gebruik, waar
goed voor, inhoud bij oliën) staan verwerkt op elke productpagina. Alleen deze
zaken zijn nog **placeholder** en moeten door CALMMINI worden ingevuld:
- **Prijzen** — nu voorbeeldwaarden (er stonden geen prijzen in het overzicht).
  Aanpassen: wijzig de prijzen in `build/data.py` en genereer opnieuw (zie
  hieronder), of pas ze aan in `assets/js/data.js` én in de HTML.
- **Productfoto's** — voor de 6 hierboven genoemde producten.
- **Reviews, keurmerken, certificeringen, levertijden** — bewust niet verzonnen.
- **Juridische teksten** (privacy, voorwaarden, verzending/retour) — placeholders.
- **Formulieren & checkout** — demo (geen echte verwerking). Koppel bijv. Mollie
  of Stripe voor betalingen en een e-maildienst voor formulieren/nieuwsbrief.
- **Bedrijfsgegevens** (KvK, btw, adres, telefoon) — in de footer/contactpagina.

Op elke productpagina staat de meegeleverde disclaimer: _"Test het product altijd
eerst op een klein stukje huid en stop met gebruiken bij irritatie of gevoeligheid."_

## Producten/teksten/prijzen wijzigen en opnieuw genereren
De HTML is gegenereerd met de scripts in `build/`. Wijzig `build/data.py`
(producten, categorieën, prijzen, blog) en draai opnieuw:
```bash
cd build
python3 photos.py        # plaatst productfoto's + genereert placeholders/categoriebeelden
python3 run.py           # (her)genereert alle HTML + sitemap etc.
```

## SEO — wat is ingebouwd
- Unieke `<title>` + meta description per pagina
- Schone URL-structuur + canonical URLs
- Breadcrumbs + BreadcrumbList structured data
- Product-, Article-, Organization-, WebSite (SearchAction)- en FAQ-structured data (JSON-LD)
- Open Graph + Twitter cards, `og:image`
- XML-sitemap, robots.txt, webmanifest
- Semantische headings, alt-teksten, `lang="nl"`
- Lazy-loading beelden, `preconnect`/`preload`, mobiel-first responsive
- Categorie- en blogpagina's als SEO-landingspagina's met interne links

_Alle canonical/sitemap-URL's gebruiken nu `https://www.calmmini.nl` — pas dit aan naar het
definitieve domein._
