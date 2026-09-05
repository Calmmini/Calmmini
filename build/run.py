# -*- coding: utf-8 -*-
import os, json, datetime
from data import BRAND, CATEGORIES, PRODUCTS, BLOG, cat_by_slug
import generate as G
from generate import ROOT, DOMAIN
import pages as PG

def write_root(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)

def build_data_js():
    data = []
    for p in PRODUCTS:
        data.append({"slug":p["slug"],"name":p["name"],"price":p["price"],
                     "cat":[p["cat"]]+p["extra_cats"],"badge":p["badge"]})
    js = "window.CALMMINI_PRODUCTS=" + json.dumps(data, ensure_ascii=False) + ";"
    with open(os.path.join(ROOT,"assets/js/data.js"),"w",encoding="utf-8") as f:
        f.write(js)

def build_sitemap():
    urls = [("", "1.0"), ("producten/", "0.9"), ("gebruik-en-ritueel/", "0.7"),
            ("blog/", "0.6"),
            ("over-calmmini/", "0.5"), ("contact/", "0.4"),
            ("veelgestelde-vragen/", "0.4"), ("verzending-en-retour/", "0.3"),
            ("privacybeleid/", "0.2"), ("algemene-voorwaarden/", "0.2")]
    for c in CATEGORIES: urls.append(("categorie/%s/"%c["slug"], "0.8"))
    for p in PRODUCTS: urls.append(("product/%s/"%p["slug"], "0.7"))
    for b in BLOG: urls.append(("blog/%s/"%b["slug"], "0.6"))
    today = datetime.date.today().isoformat()
    items = ""
    for loc, pr in urls:
        items += ("  <url><loc>%s/%s</loc><lastmod>%s</lastmod>"
                  "<changefreq>weekly</changefreq><priority>%s</priority></url>\n"
                  % (DOMAIN, loc, today, pr))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + items + '</urlset>\n')
    write_root("sitemap.xml", xml)

def build_robots():
    write_root("robots.txt",
        "User-agent: *\nAllow: /\nDisallow: /afrekenen/\nDisallow: /winkelwagen/\n\n"
        "Sitemap: %s/sitemap.xml\n" % DOMAIN)

def build_manifest():
    m = {"name":"CALMMINI","short_name":"CALMMINI","lang":"nl-NL",
         "start_url":"/","display":"standalone","background_color":"#F4ECDD",
         "theme_color":"#2A251F",
         "icons":[{"src":"/favicon.svg","sizes":"any","type":"image/svg+xml"},
                  {"src":"/assets/img/og-image.jpg","sizes":"1200x630","type":"image/jpeg"}]}
    write_root("site.webmanifest", json.dumps(m, ensure_ascii=False, indent=2))

def build_favicon():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" rx="14" fill="#907138"/>'
           '<path d="M43 24a15 15 0 1 0 0 16" fill="none" stroke="#FFFAF5" '
           'stroke-width="4.4" stroke-linecap="round"/>'
           '</svg>')
    write_root("favicon.svg", svg)

def build_readme():
    from photos import PHOTO
    real = set(PHOTO)
    cats = "\n".join("- `/categorie/%s/`" % c["slug"] for c in CATEGORIES)
    prods = "\n".join(
        "- `%s.jpg` — %s%s" % (p["slug"], p["name"],
                               "" if p["slug"] in real else "  **(nog placeholder)**")
        for p in PRODUCTS)
    missing = [p for p in PRODUCTS if p["slug"] not in real]
    missing_list = "\n".join("- `%s.jpg` — %s" % (p["slug"], p["name"]) for p in missing)
    md = """# CALMMINI — Webshop

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
`{domain}`.

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
{cats}

## Productfoto's
De 15 aangeleverde productfoto's zijn geplaatst en aan de juiste producten
gekoppeld. Enkele producten hadden nog geen foto en tonen daarom een nette,
merkgerichte placeholder. Vervang die 1-op-1 (zelfde bestandsnaam) in
`assets/img/products/` — aanbevolen: staand, ~900×1125 px, `.jpg`:

{missing}

Alle productbestanden (echte foto's zijn niet gemarkeerd):

{prods}

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
- **Productfoto's** — voor de {n_missing} hierboven genoemde producten.
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

_Alle canonical/sitemap-URL's gebruiken nu `{domain}` — pas dit aan naar het
definitieve domein._
""".format(domain=DOMAIN, cats=cats, prods=prods, missing=missing_list, n_missing=len(missing))
    write_root("README.md", md)

def main():
    PG.build_home()
    PG.build_collection()
    PG.build_categories()
    PG.build_products()
    PG.build_cart()
    PG.build_checkout()
    PG.build_blog_index()
    PG.build_blog_posts()
    PG.build_static()
    PG.build_guide()
    PG.build_404()
    build_data_js()
    build_sitemap()
    build_robots()
    build_manifest()
    build_favicon()
    build_readme()
    print("build complete")

if __name__ == "__main__":
    main()
