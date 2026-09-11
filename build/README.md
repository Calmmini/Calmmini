# CALMMINI — buildscripts

De HTML in deze webshop is gegenereerd met deze scripts. Paden zijn relatief
t.o.v. deze map (`build/` staat in de siteroot).

## HTML/teksten/prijzen aanpassen en opnieuw genereren
1. Pas `data.py` aan (producten, categorieen, prijzen, teksten, FAQ, voorwaarden).
2. Draai vanuit deze map:

    python3 run.py

Dit (her)genereert alle HTML, sitemap.xml, robots.txt en de webmanifest.
De bestaande afbeeldingen in `assets/img/` blijven ongewijzigd.

## Afbeeldingen opnieuw genereren (optioneel)
`photos.py` verwerkt de originele productfoto's + logo/hero en `make_assets.py`
maakt de placeholder-beelden. Deze hebben de originele bronbestanden nodig en
zijn dus alleen relevant bij een nieuwe fotoset.

Bestanden: data.py (inhoud), generate.py (layout/SEO/head), pages.py (pagina's),
run.py (build + sitemap), photos.py + make_assets.py (beeld).
