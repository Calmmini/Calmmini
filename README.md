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
assets/img/…              Placeholder-beelden
sitemap.xml  robots.txt  site.webmanifest  favicon.svg
```

Categorie-URL's:
- `/categorie/hammamkruiden/`
- `/categorie/ghassoul/`
- `/categorie/savon-noir/`
- `/categorie/olien/`
- `/categorie/scrubs/`
- `/categorie/haarverzorging/`
- `/categorie/lichaamsverzorging/`

## Echte productfoto's toevoegen
Vervang de placeholder-bestanden 1-op-1 (zelfde bestandsnaam) in
`assets/img/products/`. Aanbevolen: staand, ~900×1125 px, `.jpg`.

- `hammamkruiden-haar.jpg` — Hammamkruiden voor het Haar
- `hammamkruiden-lichaam.jpg` — Hammamkruiden voor het Lichaam
- `hammamkruiden-ritueelset.jpg` — Hammamkruiden Ritueelset
- `ghassoul-poeder.jpg` — Ghassoul Poeder
- `ghassoul-blokken.jpg` — Ghassoul Blokken
- `savon-noir.jpg` — Savon Noir
- `savon-beldi-elfassi.jpg` — Savon Beldi Elfassi
- `savon-noir-a-nila.jpg` — Savon Noir à Nila
- `natuurlijke-olie-haar.jpg` — Natuurlijke Olie voor het Haar
- `natuurlijke-olie-lichaam.jpg` — Natuurlijke Olie voor het Lichaam
- `marokkaanse-olie-mix.jpg` — Marokkaanse Olie — Multifunctioneel
- `marokkaanse-scrub.jpg` — Marokkaanse Scrub
- `gommage-handschoen.jpg` — Kessa Gommage-handschoen
- `haarmasker-natuurlijk.jpg` — Natuurlijk Haarmasker
- `lichaamsboter-natuurlijk.jpg` — Natuurlijke Lichaamsboter
- `hammam-startpakket.jpg` — Hammam Startpakket

Categorie- en sfeerbeelden staan in `assets/img/categories/` en de losse
`assets/img/*.jpg` (hero.jpg, ritueel.jpg, verhaal.jpg).

## Nog invullen (placeholders)
De opdracht was om **geen feitelijke productinformatie te verzinnen**. Daarom zijn
deze zaken bewust als placeholder gelaten:
- **Prijzen** — nu voorbeeldwaarden; pas ze aan in `assets/js/data.js` én op de
  product-/categoriepagina's (of genereer opnieuw, zie hieronder).
- **Ingrediënten, gebruik, inhoud/gewicht, werking, herkomst** — per productpagina
  in de accordeon (`[…wordt toegevoegd]`).
- **Reviews, keurmerken, certificeringen, levertijden** — nog niet toegevoegd.
- **Juridische teksten** (privacy, voorwaarden, verzending/retour) — placeholders.
- **Formulieren & checkout** — demo (geen echte verwerking). Koppel bijv. Mollie
  of Stripe voor betalingen en een e-maildienst voor formulieren/nieuwsbrief.
- **Bedrijfsgegevens** (KvK, btw, adres, telefoon) — in de footer/contactpagina.

## Producten/teksten wijzigen en opnieuw genereren
De HTML is gegenereerd met de scripts in `build/`. Wijzig `build/data.py`
(producten, categorieën, blog) en draai opnieuw:
```bash
cd build
python3 make_assets.py   # (her)genereert placeholder-beelden
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
