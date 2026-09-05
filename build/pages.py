# -*- coding: utf-8 -*-
import os, json
from data import (BRAND, CATEGORIES, PRODUCTS, BLOG, TERMS, eur, cat_by_slug, products_in_cat)
import generate as G
from generate import (ROOT, DOMAIN, IC, star_svg, href, asset, canon, esc, rel_prefix,
                      breadcrumb, product_grid, product_card, page, write, footer, header,
                      scripts, head)

# --------------------------------------------------------------------------- #
#  HOME                                                                        #
# --------------------------------------------------------------------------- #
def build_home():
    rel = rel_prefix(0)
    featured = [p for p in PRODUCTS if p["badge"] == "Bestseller"][:4]
    if len(featured) < 4:
        featured += [p for p in PRODUCTS if p not in featured][:4-len(featured)]

    # category tiles (all six)
    cat_tiles = "".join("""
    <a class="cat-card reveal" href="{url}">
      <img src="{img}" alt="{name} — CALMMINI" loading="lazy" width="1200" height="800">
      <span class="cap"><b>{name}</b><span class="pill">Ontdek {arrow}</span></span>
    </a>""".format(url=href(rel,"categorie/%s/"%c["slug"]),
                   img=asset(rel,"img/categories/%s.jpg"%c["slug"]),
                   name=esc(c["name"]), arrow=IC["arrow"]) for c in CATEGORIES)

    body = """
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">Calmmini &middot; Hammamrituelen</span>
      <h1>Rust voor mij.<br>Gewoon thuis.</h1>
      <p class="lead">Calmmini is geen groot ritueel ver weg. Het is dat kleine moment in je eigen badkamer, waarop het warme water loopt, de geur van hammam vrijkomt en je voelt: even niets moeten.</p>
      <p class="hero-poem"><em>Calm</em> staat voor rust. <em>Mini</em> voor klein, dichtbij en thuis. <em>Ini</em> voor mij, voor jezelf. Samen is Calmmini precies dat: een klein moment van rust, helemaal van jou.</p>
      <div class="hero-cta">
        <a class="btn btn-primary btn-lg" href="{allprod}">Bekijk onze producten</a>
        <a class="btn btn-ghost btn-lg" href="{guide}">Het ritueel</a>
      </div>
      <div class="hero-trust">
        <span>{leaf} Natuurlijke ingredienten</span>
        <span>{moon} Marokkaanse traditie</span>
        <span>{shield} Zorgvuldig geselecteerd</span>
      </div>
    </div>
    <div class="hero-media reveal">
      <div class="arch-frame"><img src="{hero}" alt="Marokkaanse hammamingredienten: nila, rozen en kruiden" fetchpriority="high" width="1000" height="1250"></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap feature">
    <div class="feature-media reveal"><div class="arch-frame landscape"><img src="{sfeer}" alt="Van badkamer naar hammammoment" loading="lazy" width="1100" height="880"></div></div>
    <div>
      <span class="eyebrow">Het idee</span>
      <h2>Van badkamer naar hammammoment</h2>
      <p class="lead">Soms heb je geen hele dag nodig om op adem te komen. Soms begint het al met zwarte zeep op een warme huid. Met klei die zacht opdroogt. Met scrub die je huid wakker maakt. Met olie die de geur van verzorging nog even laat hangen.</p>
      <p>Calmmini brengt de warmte van Marokkaanse hammamverzorging naar huis. Niet ingewikkeld, niet afstandelijk, maar vertrouwd, warm en dichtbij.</p>
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow center">Onze producten</span>
      <h2>Alles voor jouw ritueel</h2>
      <p class="lead" style="text-align:center;margin-inline:auto">Onze collectie bestaat uit zorgvuldig gekozen hammamproducten zoals zwarte zeep, ghassoul, klei, scrub, olien en accessoires. Producten met een Marokkaanse basis, zachte geuren en een verzorgend gevoel voor huid en haar.</p>
    </div>
    <div class="cat-grid">{cattiles}</div>
    <div class="center" style="margin-top:2.4rem"><a class="btn btn-primary btn-lg" href="{allprod}">Bekijk onze producten</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="row">
      <div><span class="eyebrow">Favorieten</span><h2>Meest gekozen</h2></div>
      <a class="link-more" href="{allprod}">Alle producten {arrow}</a>
    </div></div>
    {featured}
  </div>
</section>

<section class="section dark">
  <div class="wrap narrow center">
    <span class="eyebrow center">Gebruik &amp; ritueel</span>
    <h2 style="color:var(--cream)">Een ritueel dat klein mag zijn</h2>
    <p class="lead" style="margin-inline:auto;color:rgba(255,250,245,.82)">Een hammammoment hoeft niet perfect te zijn. Het mag klein zijn. Eenvoudig. Op jouw manier. Daarom leggen we stap voor stap uit hoe je onze producten gebruikt, zodat je thuis rustig je eigen verzorgingsritueel kunt opbouwen.</p>
    <a class="btn btn-primary btn-lg" href="{guide}" style="margin-top:1.6rem">Ontdek jouw ritueel</a>
  </div>
</section>

<section class="section">
  <div class="wrap feature">
    <div class="feature-media reveal"><div class="arch-frame"><img src="{over_img}" alt="Over Calmmini" loading="lazy" width="900" height="1125"></div></div>
    <div>
      <span class="eyebrow">Over Calmmini</span>
      <h2>Verzorging die iets met je doet</h2>
      <p class="lead">Calmmini is ontstaan vanuit liefde voor Marokkaanse verzorging, hammamrituelen en het gevoel dat je na een goed verzorgingsmoment weer helemaal bij jezelf komt.</p>
      <p>Voor ons is verzorging niet alleen wat je op je huid doet. Het is ook wat het met je doet.</p>
      <a class="btn btn-ghost" href="{over}" style="margin-top:.6rem">Lees meer over Calmmini</a>
    </div>
  </div>
</section>
{homeseo}
<section class="section dark">
  <div class="wrap narrow cta-band">
    <span class="eyebrow center">Contact</span>
    <h2>Bestellen of advies nodig?</h2>
    <p class="lead">Twijfel je welk product bij jou past of wil je een bestelling plaatsen? We denken graag met je mee.</p>
    <a class="btn btn-primary btn-lg" href="{contact}" style="margin-top:1.4rem">Stuur ons een bericht</a>
  </div>
</section>
""".format(allprod=href(rel,"producten/"), guide=href(rel,"gebruik-en-ritueel/"),
           hero=asset(rel,"img/hero.jpg"), sfeer=asset(rel,"img/sfeer.jpg"),
           over_img=asset(rel,"img/products/sabon-beldi-naturel.jpg"),
           leaf=IC["leaf"], moon=IC["moon"], shield=IC["shield"],
           cattiles=cat_tiles, featured=product_grid(rel, featured), arrow=IC["arrow"],
           over=href(rel,"over-calmmini/"), contact=href(rel,"contact/"),
           homeseo=seo_block("Natuurlijke Marokkaanse hammamverzorging voor thuis", [
               "CALMMINI brengt de Marokkaanse hammam naar je eigen badkamer. Ontdek sabon beldi "
               "(Marokkaanse zwarte zeep of savon noir), kant-en-klare ghassoul en klei, "
               "hammampoeder, verzorgingsoli\u00ebn, shea butter, scrub en accessoires \u2014 alles voor "
               "een compleet, natuurlijk hammamritueel voor haar en lichaam.",
               "Of je nu op zoek bent naar Marokkaanse haar- en huidverzorging of losse onderdelen "
               "van het ritueel: bij CALMMINI stel je eenvoudig je eigen ritueel samen. Vanuit "
               "Amersfoort, besteld en bezorgd in heel Nederland."]))

    org = {"@context":"https://schema.org","@type":"Organization","name":"CALMMINI",
           "url":DOMAIN,"logo":DOMAIN+"/assets/img/logo.png","email":BRAND["email"],
           "description":"Natuurlijke Marokkaanse hammamverzorging voor haar en lichaam.",
           "areaServed":"NL"}
    website = {"@context":"https://schema.org","@type":"WebSite","name":"CALMMINI",
               "url":DOMAIN,"inLanguage":"nl-NL",
               "potentialAction":{"@type":"SearchAction",
                   "target":{"@type":"EntryPoint","urlTemplate":DOMAIN+"/producten/?q={search_term_string}"},
                   "query-input":"required name=search_term_string"}}
    page("", 0,
         "CALMMINI Hammamrituelen — Marokkaanse hammamverzorging voor thuis",
         "Rust voor mij. Gewoon thuis. Natuurlijke Marokkaanse hammamverzorging: sabon beldi, "
         "ghassoul, klei, hammampoeder, scrubs en olien. Het hammamritueel thuis.",
         body, active="home", jsonld=[org, website])

# --------------------------------------------------------------------------- #
#  COLLECTION (all products) + CATEGORY pages                                  #
# --------------------------------------------------------------------------- #
def filters_sidebar(rel, active_cat=None):
    cat_boxes = "".join(
        '<label><input type="checkbox" data-filter-cat value="%s"%s> %s</label>'
        % (c["slug"], ' checked' if active_cat==c["slug"] else '', esc(c["menu"]))
        for c in CATEGORIES)
    return """
<aside class="filters" aria-label="Filters">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem">
    <strong style="font-family:var(--serif);font-size:1.2rem">Filters</strong>
    <button class="icon-btn" data-close aria-label="Sluiten" style="display:none">{close}</button>
  </div>
  <div class="fgroup"><h4>Categorie</h4>{cats}</div>
  <div class="fgroup"><h4>Prijs</h4>
    <label><input type="radio" name="price" data-filter-price value="all" checked> Alle prijzen</label>
    <label><input type="radio" name="price" data-filter-price value="lt10"> Tot € 10</label>
    <label><input type="radio" name="price" data-filter-price value="10to20"> € 10 – € 20</label>
    <label><input type="radio" name="price" data-filter-price value="gt20"> Boven € 20</label>
  </div>
  <button class="btn btn-ghost btn-block" data-clear-filters>Filters wissen</button>
</aside>""".format(cats=cat_boxes, close=IC["close"])

def toolbar(rel, count):
    return """
<div class="toolbar">
  <span class="count" data-count>{n} producten</span>
  <div style="display:flex;gap:.6rem;align-items:center">
    <button class="btn btn-ghost filter-toggle" data-open-filters>Filters</button>
    <label style="font-size:.86rem;color:var(--ink-soft)">Sorteren
      <select data-sort aria-label="Sorteren">
        <option value="featured">Aanbevolen</option>
        <option value="price-asc">Prijs oplopend</option>
        <option value="price-desc">Prijs aflopend</option>
        <option value="name">Naam A–Z</option>
      </select></label>
  </div>
</div>""".format(n=count)

def seo_block(title, paras):
    ps = "".join("<p>%s</p>" % p for p in paras)
    return ('<section class="section tint"><div class="wrap prose narrow">'
            '<h2>%s</h2>%s</div></section>' % (title, ps))

def build_collection():
    rel = rel_prefix(1)
    crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Producten","producten/")])
    grid = product_grid(rel, PRODUCTS)
    body = """
<div class="page-hero"><div class="wrap">
  <span class="eyebrow">Webshop</span>
  <h1>Onze producten</h1>
  <p class="lead">Onze collectie bestaat uit zorgvuldig geselecteerde hammamproducten zoals zwarte zeep, ghassoul, klei, scrub, oliën en accessoires. Producten met een herkenbare Marokkaanse basis, warme uitstraling en aandacht voor huid- en haarverzorging.</p>
</div></div>
{crumb}
<div class="wrap collection">
  {filters}
  <div>
    {toolbar}
    {grid}
  </div>
</div>
{seo}
""".format(crumb=crumb, filters=filters_sidebar(rel), toolbar=toolbar(rel, len(PRODUCTS)),
           grid=grid,
           seo=seo_block("Natuurlijke Marokkaanse verzorgingsproducten kopen", [
               "Bij CALMMINI vind je natuurlijke verzorgingsproducten uit de Marokkaanse traditie. "
               "Het assortiment is opgebouwd rond het hammamritueel: van reiniging met savon noir en de "
               "gommage-scrub, tot verzorging met ghassoul, hammamkruiden en natuurlijke oliën.",
               "Of je nu op zoek bent naar Marokkaanse haarverzorging, natuurlijke lichaamsverzorging of "
               "de losse onderdelen van een hammamritueel — je stelt eenvoudig je eigen ritueel samen. "
               "Gebruik de filters om per categorie of prijs te zoeken.",
           ]))
    itemlist = {"@context":"https://schema.org","@type":"ItemList",
        "itemListElement":[{"@type":"ListItem","position":i+1,
            "url":canon("product/%s/"%p["slug"]),"name":p["name"]} for i,p in enumerate(PRODUCTS)]}
    page("producten/", 1,
         "Alle producten — Marokkaanse natuurlijke verzorging | CALMMINI",
         "Bekijk alle natuurlijke Marokkaanse verzorgingsproducten van CALMMINI: ghassoul, savon noir, "
         "hammamkruiden, scrubs, oliën en meer. Voor haar en lichaam.",
         body, active="", jsonld=[crumb_ld, itemlist])

def build_categories():
    for c in CATEGORIES:
        rel = rel_prefix(2)
        prods = products_in_cat(c["slug"])
        crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Producten","producten/"),
                                           (c["name"],"categorie/%s/"%c["slug"])])
        grid = product_grid(rel, prods)
        # related blog
        related = [b for b in BLOG if b["cat_link"]==c["slug"]]
        rel_html = ""
        if related:
            b = related[0]
            rel_html = """
<section class="section"><div class="wrap"><div class="article-cta">
  <div><span class="eyebrow">Lezen</span><b>{t}</b></div>
  <a class="btn btn-primary" href="{u}">Lees het artikel</a>
</div></div></section>""".format(t=esc(b["title"]), u=href(rel,"blog/%s/"%b["slug"]))
        # per-category FAQ (with schema)
        faq_html = faq_ld = ""
        cfaq = c.get("faq") or []
        if cfaq:
            items = "".join(
                '<details%s><summary>%s</summary><div class="acc-body">%s</div></details>'
                % (" open" if i==0 else "", esc(q), esc(a)) for i,(q,a) in enumerate(cfaq))
            faq_html = ('<section class="section"><div class="wrap narrow">'
                        '<h2>Veelgestelde vragen over %s</h2>'
                        '<div class="acc faq-list">%s</div></div></section>'
                        % (esc(c["name"]), items))
            faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
                {"@type":"Question","name":q,
                 "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in cfaq]}
        body = """
<div class="page-hero"><div class="wrap">
  <span class="eyebrow">{tag}</span>
  <h1>{name}</h1>
  <p class="lead">{intro}</p>
</div></div>
{crumb}
<div class="wrap collection">
  {filters}
  <div>
    {toolbar}
    {grid}
  </div>
</div>
{relblog}
{faq}
{seo}
""".format(tag=esc(c["tagline"]), name=esc(c["name"]), intro=esc(c["intro"]), crumb=crumb,
           filters=filters_sidebar(rel, active_cat=c["slug"]),
           toolbar=toolbar(rel, len(prods)), grid=grid, relblog=rel_html, faq=faq_html,
           seo=seo_block("Over %s" % c["name"], [esc(p) for p in c["body"]]))
        blocks = [crumb_ld]
        if faq_ld: blocks.append(faq_ld)
        page("categorie/%s/"%c["slug"], 2, c["seo_title"], c["seo_desc"],
             body, active="", jsonld=blocks)

# --------------------------------------------------------------------------- #
#  PRODUCT DETAIL                                                              #
# --------------------------------------------------------------------------- #
def build_products():
    for p in PRODUCTS:
        rel = rel_prefix(2)
        c = cat_by_slug(p["cat"])
        crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Producten","producten/"),
            (c["name"],"categorie/%s/"%c["slug"]),(p["name"],"product/%s/"%p["slug"])])
        img = asset(rel,"img/products/%s.jpg"%p["slug"])
        thumbs = "".join(
            '<button class="%s"><img src="%s" alt="%s afbeelding %d"></button>'
            % ("active" if i==0 else "", img, esc(p["name"]), i+1) for i in range(4))
        related = [x for x in products_in_cat(p["cat"]) if x["slug"]!=p["slug"]][:4]
        if len(related) < 4:
            related += [x for x in PRODUCTS if x["slug"]!=p["slug"] and x not in related][:4-len(related)]
        inhoud_row = ('<div class="row">%s Inhoud: %s</div>' % (IC["drop"], esc(p["inhoud"]))) if p["inhoud"] else ""
        tip_box = ('<div class="tip-note">%s <span>%s</span></div>'
                   % (IC["sparkle"], esc(c["tip"]))) if c.get("tip") else ""
        bewaar = ""
        if p["inhoud"]:
            bewaar += "<p>Inhoud: %s.</p>" % esc(p["inhoud"])
        if c["slug"] == "verzorgingsolien" and c.get("tip"):
            bewaar += "<p>%s</p>" % esc(c["tip"])
        if not bewaar:
            bewaar = '<p class="ph">Inhoud en bewaaradvies worden per product aangevuld.</p>'
        body = """
{crumb}
<div class="wrap pdp" data-gallery data-qty-scope>
  <div class="pdp-gallery">
    <div class="main"><img src="{img}" alt="{name} — {catname} van CALMMINI" width="900" height="1125"></div>
    <div class="pdp-thumbs">{thumbs}</div>
  </div>
  <div class="pdp-info">
    <div class="pdp-cat">{catname}</div>
    <h1>{name}</h1>
    <div class="pdp-price">{eur} <small>incl. btw{inhoudlabel}</small></div>
    <p class="pdp-desc">{blurb}</p>
    <div class="pdp-actions">
      <div class="qty"><button data-step="-1" aria-label="Minder">–</button>
        <input value="1" readonly aria-label="Aantal"><button data-step="1" aria-label="Meer">+</button></div>
      <button class="btn btn-primary btn-lg" data-add="{slug}">In winkelwagen</button>
    </div>
    <p class="price-note">Voorbeeldprijs — definitieve prijzen worden door CALMMINI ingesteld.</p>
    {tipbox}
    <div class="pdp-meta">
      <div class="row">{leaf} {voordeel}</div>
      {inhoudrow}
      <div class="row">{truck} Bezorging in heel Nederland</div>
      <div class="row">{shield} Zorgvuldig geselecteerd door CALMMINI</div>
    </div>
    <div class="acc">
      <details open><summary>Productbeschrijving</summary>
        <div class="acc-body"><p>{blurb}</p><p><strong>Waar goed voor:</strong> {voordeel}</p></div></details>
      <details><summary>Ingrediënten / basis</summary>
        <div class="acc-body"><p>{ingredienten}</p></div></details>
      <details><summary>Gebruik</summary>
        <div class="acc-body"><p>{gebruik}</p></div></details>
      <details><summary>Inhoud &amp; bewaren</summary>
        <div class="acc-body">{bewaar}</div></details>
      <details><summary>Verzending &amp; retour</summary>
        <div class="acc-body"><p>Je bestelling wordt in heel Nederland bezorgd. Bekijk de <a href="{ship}">verzend- en retourvoorwaarden</a>.</p></div></details>
    </div>
    <p class="fineprint">{disclaimer}</p>
  </div>
</div>

<section class="section tint"><div class="wrap">
  <div class="section-head"><div class="row"><div><span class="eyebrow">Misschien ook interessant</span><h2>Past bij jouw ritueel</h2></div>
  <a class="link-more" href="{caturl}">Meer uit {catname} {arrow}</a></div></div>
  {related}
</div></section>
""".format(crumb=crumb, img=img, name=esc(p["name"]), catname=esc(c["name"]), eur=eur(p["price"]),
           inhoudlabel=(" · %s" % esc(p["inhoud"])) if p["inhoud"] else "",
           blurb=esc(p["blurb"]), slug=p["slug"], thumbs=thumbs, leaf=IC["leaf"], truck=IC["truck"],
           shield=IC["shield"], ship=href(rel,"verzending-en-retour/"),
           voordeel=esc(p["voordeel"]), ingredienten=esc(p["ingredienten"]), gebruik=esc(p["gebruik"]),
           inhoudrow=inhoud_row, tipbox=tip_box, bewaar=bewaar, disclaimer=esc(BRAND["disclaimer"]),
           caturl=href(rel,"categorie/%s/"%p["cat"]), arrow=IC["arrow"],
           related=product_grid(rel, related))

        prod_ld = {"@context":"https://schema.org","@type":"Product","name":p["name"],
            "image":[DOMAIN+"/assets/img/products/%s.jpg"%p["slug"]],
            "description":"%s %s" % (p["blurb"], p["voordeel"]),"brand":{"@type":"Brand","name":"CALMMINI"},
            "category":c["name"],"url":canon("product/%s/"%p["slug"]),
            "offers":{"@type":"Offer","price":"%.2f"%p["price"],"priceCurrency":"EUR",
                "availability":"https://schema.org/InStock","url":canon("product/%s/"%p["slug"]),
                "itemCondition":"https://schema.org/NewCondition","seller":{"@type":"Organization","name":"CALMMINI"}}}
        _md = "%s kopen bij CALMMINI. %s" % (p["name"], p["blurb"])
        _tail = " Marokkaanse verzorging, bezorgd in heel Nederland."
        if len(_md) + len(_tail) <= 158:
            _md += _tail
        elif len(_md) > 158:
            _md = _md[:155].rstrip(" ,.;:") + "…"
        page("product/%s/"%p["slug"], 2,
             "%s kopen | CALMMINI" % p["name"],
             _md,
             body, active="", jsonld=[crumb_ld, prod_ld], og_type="product",
             og_image=DOMAIN+"/assets/img/products/%s.jpg"%p["slug"])

# --------------------------------------------------------------------------- #
#  CART                                                                        #
# --------------------------------------------------------------------------- #
def build_cart():
    rel = rel_prefix(1)
    crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Winkelwagen","winkelwagen/")])
    body = """
<div class="page-hero"><div class="wrap"><h1>Winkelwagen</h1></div></div>
{crumb}
<div class="wrap">
  <div data-cart-empty hidden class="empty-state">
    {cartic}
    <h2>Je winkelwagen is leeg</h2>
    <p class="lead" style="margin-inline:auto">Ontdek onze natuurlijke Marokkaanse verzorgingsproducten en stel je eigen ritueel samen.</p>
    <a class="btn btn-primary btn-lg" href="{allprod}" style="margin-top:1rem">Naar de webshop</a>
  </div>
  <div data-cart-wrap hidden class="cart-layout">
    <div>
      <div data-cart-lines></div>
      <a class="link-more" href="{allprod}" style="margin-top:1.4rem">{arrow} Verder winkelen</a>
    </div>
    <aside class="summary">
      <h3>Overzicht</h3>
      <div class="row"><span>Subtotaal</span><span data-subtotal>€ 0,00</span></div>
      <div class="row"><span>Verzending</span><span>Berekend bij afrekenen</span></div>
      <div class="row total"><span>Totaal</span><span data-total>€ 0,00</span></div>
      <a class="btn btn-primary btn-block btn-lg" href="{checkout}" style="margin-top:1.2rem">Afrekenen</a>
      <p class="note">Prijzen zijn inclusief btw. Verzendkosten worden berekend bij het afrekenen.</p>
    </aside>
  </div>
</div>
<div style="height:3rem"></div>
""".format(crumb=crumb, cartic=IC["cart"], allprod=href(rel,"producten/"),
           arrow=IC["arrow"], checkout=href(rel,"afrekenen/"))
    page("winkelwagen/", 1, "Winkelwagen | CALMMINI",
         "Bekijk je winkelwagen bij CALMMINI en reken eenvoudig af.", body, jsonld=[crumb_ld])

# --------------------------------------------------------------------------- #
#  CHECKOUT                                                                    #
# --------------------------------------------------------------------------- #
def build_checkout():
    rel = rel_prefix(1)
    crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Winkelwagen","winkelwagen/"),("Afrekenen","afrekenen/")])
    body = """
<div class="page-hero"><div class="wrap"><h1>Afrekenen</h1></div></div>
{crumb}
<div class="wrap">
  <div data-order-confirm hidden class="empty-state">
    {check}
    <h2>Bedankt voor je bestelling!</h2>
    <p class="lead" style="margin-inline:auto">Dit is een demonstratie van de checkout. Koppel hier je betaal- en bestelsysteem (bijvoorbeeld Mollie of Stripe) om echte bestellingen te verwerken.</p>
    <a class="btn btn-primary btn-lg" href="{allprod}" style="margin-top:1rem">Verder winkelen</a>
  </div>
  <form data-checkout-form data-checkout-wrap class="checkout">
    <div>
      <div class="form-card">
        <h3>Contactgegevens</h3>
        <div class="field full"><label>E-mailadres</label><input type="email" required placeholder="naam@voorbeeld.nl"></div>
      </div>
      <div class="form-card">
        <h3>Bezorgadres</h3>
        <div class="frow">
          <div class="field"><label>Voornaam</label><input required></div>
          <div class="field"><label>Achternaam</label><input required></div>
        </div>
        <div class="frow">
          <div class="field"><label>Postcode</label><input required placeholder="1234 AB"></div>
          <div class="field"><label>Huisnummer</label><input required></div>
        </div>
        <div class="field full"><label>Straat</label><input required></div>
        <div class="field full"><label>Plaats</label><input required></div>
        <div class="field full"><label>Land</label><select><option>Nederland</option><option>België</option></select></div>
      </div>
      <div class="form-card">
        <h3>Betaalmethode</h3>
        <div class="pay-methods">
          <label class="pay-opt"><input type="radio" name="pay" checked> iDEAL</label>
          <label class="pay-opt"><input type="radio" name="pay"> Bancontact</label>
          <label class="pay-opt"><input type="radio" name="pay"> Creditcard</label>
          <label class="pay-opt"><input type="radio" name="pay"> PayPal</label>
        </div>
      </div>
    </div>
    <aside class="summary">
      <h3>Je bestelling</h3>
      <div data-checkout-lines></div>
      <div class="row" style="margin-top:1rem"><span>Subtotaal</span><span data-subtotal>€ 0,00</span></div>
      <div class="row"><span>Verzending</span><span>Nader te bepalen</span></div>
      <div class="row total"><span>Totaal</span><span data-total>€ 0,00</span></div>
      <button class="btn btn-primary btn-block btn-lg" type="submit" style="margin-top:1.2rem">Bestelling plaatsen</button>
      <p class="note">Demo-checkout — er wordt geen betaling verwerkt.</p>
    </aside>
  </form>
</div>
<div style="height:3rem"></div>
""".format(crumb=crumb, check=IC["check"], allprod=href(rel,"producten/"))
    page("afrekenen/", 1, "Afrekenen | CALMMINI",
         "Rond je bestelling af bij CALMMINI.", body, jsonld=[crumb_ld])

# --------------------------------------------------------------------------- #
#  BLOG                                                                        #
# --------------------------------------------------------------------------- #
def build_blog_index():
    rel = rel_prefix(1)
    crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Achtergrond","blog/")])
    cards = "".join("""
    <article class="blog-card reveal">
      <a href="{url}"><img src="{img}" alt="{title}" loading="lazy" width="1200" height="760"></a>
      <div class="bc-body">
        <div class="meta">Achtergrond · {read} min lezen</div>
        <h3><a href="{url}">{title}</a></h3>
        <p>{ex}</p>
        <a class="link-more" href="{url}" style="margin-top:1rem">Lees verder {arrow}</a>
      </div>
    </article>""".format(url=href(rel,"blog/%s/"%b["slug"]),
        img=asset(rel,"img/blog/%s.jpg"%b["slug"]), title=esc(b["title"]),
        read=b["read"], ex=esc(b["excerpt"]), arrow=IC["arrow"]) for b in BLOG)
    body = """
<div class="page-hero"><div class="wrap">
  <span class="eyebrow">Achtergrond</span>
  <h1>Rituelen &amp; verzorging</h1>
  <p class="lead">Verhalen, gidsen en achtergrond over Marokkaanse verzorging, het hammamritueel en natuurlijke producten voor haar en lichaam.</p>
</div></div>
{crumb}
<section class="section"><div class="wrap"><div class="blog-grid">{cards}</div></div></section>
""".format(crumb=crumb, cards=cards)
    page("blog/", 1, "Achtergrond — Marokkaanse verzorging & hammamrituelen | CALMMINI",
         "Lees over het Marokkaanse hammamritueel, ghassoul, sabon beldi (savon noir) en "
         "natuurlijke haar- en lichaamsverzorging bij CALMMINI.", body, active="blog", jsonld=[crumb_ld])

def build_blog_posts():
    for b in BLOG:
        rel = rel_prefix(2)
        crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Achtergrond","blog/"),(b["title"],"blog/%s/"%b["slug"])])
        blocks = ""
        for tag, txt in b["body"]:
            blocks += "<%s>%s</%s>" % (tag, txt, tag)
        # inline product links
        plinks = [p for p in PRODUCTS if p["slug"] in b["product_links"]]
        prod_html = product_grid(rel, plinks, cols3=(len(plinks)==3)) if plinks else ""
        cta = """
<div class="article-cta">
  <div><span class="eyebrow">Ontdek</span><b>Shop de producten uit dit ritueel</b></div>
  <a class="btn btn-primary" href="{u}">Bekijk categorie</a>
</div>""".format(u=href(rel,"categorie/%s/"%b["cat_link"]))
        body = """
<article class="article">
  {crumb}
  <div class="wrap">
    <div class="narrow" style="text-align:center;margin-bottom:1.5rem">
      <span class="eyebrow center">Achtergrond · {read} min lezen</span>
      <h1 style="font-size:clamp(2rem,5vw,3.4rem)">{title}</h1>
    </div>
    <div class="narrow article-hero"><img src="{img}" alt="{title}" width="1200" height="760"></div>
    <div class="article-body">
      <p style="font-size:1.15rem;color:var(--ink)"><em>{ex}</em></p>
      {blocks}
      {cta}
    </div>
  </div>
  <section class="section" style="padding-top:3rem"><div class="wrap">
    <div class="section-head"><h2>Producten bij dit artikel</h2></div>
    {prods}
  </div></section>
</article>
""".format(crumb=crumb, read=b["read"], title=esc(b["title"]),
           img=asset(rel,"img/blog/%s.jpg"%b["slug"]), ex=esc(b["excerpt"]),
           blocks=blocks, cta=cta, prods=prod_html)
        art_ld = {"@context":"https://schema.org","@type":"Article",
            "headline":b["title"],"description":b["excerpt"],"inLanguage":"nl-NL",
            "image":DOMAIN+"/assets/img/blog/%s.jpg"%b["slug"],
            "datePublished":b["date"],"dateModified":b["date"],
            "author":{"@type":"Organization","name":"CALMMINI"},
            "publisher":{"@type":"Organization","name":"CALMMINI",
                "logo":{"@type":"ImageObject","url":DOMAIN+"/assets/img/og-image.jpg"}},
            "mainEntityOfPage":canon("blog/%s/"%b["slug"])}
        page("blog/%s/"%b["slug"], 2, b["seo_title"], b["seo_desc"],
             body, active="blog", jsonld=[crumb_ld, art_ld], og_type="article",
             og_image=DOMAIN+"/assets/img/blog/%s.jpg"%b["slug"])

# --------------------------------------------------------------------------- #
#  STATIC PAGES                                                                #
# --------------------------------------------------------------------------- #
def simple_page(folder, title, desc, h1, lead, inner, active="", crumbtrail=None):
    rel = rel_prefix(1)
    crumb_html, crumb_ld = ("", None)
    if crumbtrail:
        crumb_html, crumb_ld = breadcrumb(rel, crumbtrail)
    body = """
<div class="page-hero"><div class="wrap">
  <h1>{h1}</h1>{lead}
</div></div>
{crumb}
<section class="section"><div class="wrap prose narrow">{inner}</div></section>
""".format(h1=esc(h1), lead=('<p class="lead">%s</p>'%esc(lead)) if lead else "",
           crumb=crumb_html, inner=inner)
    page(folder, 1, title, desc, body, active=active, jsonld=[crumb_ld] if crumb_ld else None)

def build_static():
    # About
    over_inner = """
<p class="lead">Calmmini is ontstaan vanuit liefde voor Marokkaanse hammamrituelen, natuurlijke verzorging en de rust van een goed verzorgingsmoment.</p>
<p>Wij geloven dat verzorging meer mag zijn dan alleen een product gebruiken. Het is een moment om te vertragen, je huid aandacht te geven en even terug te komen bij jezelf. Met Calmmini maken we traditionele hammamproducten toegankelijk voor thuis, met duidelijke uitleg over hoe je ze gebruikt en waar ze goed voor zijn.</p>
<h2>Geïnspireerd op de hammam</h2>
<p>Onze producten zijn geïnspireerd op de warmte van de Marokkaanse hammam: scrub, klei, olie, kruiden en accessoires die samen een vertrouwd ritueel vormen. Alles met een rustige uitstraling, zachte geuren en aandacht voor gebruiksgemak.</p>
<h2>Voor iedereen</h2>
<p>Calmmini is er voor iedereen die op een laagdrempelige manier kennis wil maken met natuurlijke verzorging en hammamrituelen voor thuis.</p>
<p style="margin-top:1.5rem"><a class="btn btn-primary" href="{u}">Bekijk de producten</a></p>
""".format(u=href(rel_prefix(1),"producten/"))
    simple_page("over-calmmini/", "Over Calmmini — Marokkaanse hammamrituelen voor thuis",
        "Lees meer over Calmmini: natuurlijke Marokkaanse verzorging, geïnspireerd op het hammamritueel, voor haar en lichaam.",
        "Over Calmmini", "Rust voor mij. Gewoon thuis.",
        over_inner, active="over", crumbtrail=[("Home",""),("Over Calmmini","over-calmmini/")])

    # Contact
    rel = rel_prefix(1)
    contact_inner = """
<div class="feature" style="align-items:start;gap:2.5rem">
  <div>
    <h2 class="contact-h">Neem contact op</h2>
    <p>Heb je een vraag over een product, je bestelling of het hammamritueel? We helpen je graag verder.</p>
    <p style="margin-top:1.2rem"><strong>E-mail</strong><br><a href="mailto:{email}">{email}</a></p>
    <p><strong>Klantenservice</strong><br>Bereikbaar via e-mail en het contactformulier.</p>
  </div>
  <form class="form-card" onsubmit="event.preventDefault();this.innerHTML='<h3>Bedankt!</h3><p>Je bericht is verzonden (demo). Koppel hier je e-mail- of formulierdienst.</p>';">
    <h3>Stuur een bericht</h3>
    <div class="field"><label>Naam</label><input required></div>
    <div class="field"><label>E-mailadres</label><input type="email" required></div>
    <div class="field"><label>Bericht</label><textarea rows="5" required></textarea></div>
    <button class="btn btn-primary btn-block" type="submit">Versturen</button>
  </form>
</div>
""".format(email=BRAND["email"])
    simple_page("contact/", "Contact | CALMMINI",
        "Neem contact op met CALMMINI voor vragen over producten, bestellingen of het hammamritueel.",
        "Contact", "", contact_inner, active="contact",
        crumbtrail=[("Home",""),("Contact","contact/")])

    # FAQ
    faqs = [
        ("Wat is een hammamritueel?",
         "Het hammamritueel is een traditionele Marokkaanse verzorgingsroutine met een vaste opbouw: opwarmen, reinigen met savon noir, de gommage-scrub, verzorgen met ghassoul en kruiden, en afsluiten met oliën."),
        ("Zijn de producten natuurlijk?",
         "Ons assortiment bestaat uit natuurlijke Marokkaanse verzorgingsproducten. Gedetailleerde ingrediëntinformatie wordt per product toegevoegd."),
        ("Voor welk haar- en huidtype zijn de producten geschikt?",
         "[Wordt per product toegevoegd.] Neem bij twijfel gerust contact met ons op."),
        ("Naar welke landen leveren jullie?",
         "CALMMINI richt zich primair op de Nederlandse markt en bezorgt in heel Nederland. [Overige leverinformatie wordt toegevoegd.]"),
        ("Hoe kan ik betalen?",
         "Je kunt straks betalen met onder andere iDEAL, Bancontact, creditcard en PayPal. [Definitieve betaalmethoden worden gekoppeld.]"),
    ]
    faq_inner = '<div class="acc faq-list">' + "".join(
        '<details%s><summary>%s</summary><div class="acc-body">%s</div></details>'
        % (" open" if i==0 else "", esc(q), esc(a)) for i,(q,a) in enumerate(faqs)) + '</div>'
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    rel = rel_prefix(1)
    crumb_html, crumb_ld = breadcrumb(rel, [("Home",""),("Veelgestelde vragen","veelgestelde-vragen/")])
    faq_body = """
<div class="page-hero"><div class="wrap"><h1>Veelgestelde vragen</h1>
<p class="lead">Antwoorden op de meest gestelde vragen over CALMMINI, onze producten en het hammamritueel.</p></div></div>
{crumb}
<section class="section"><div class="wrap">{inner}</div></section>
""".format(crumb=crumb_html, inner=faq_inner)
    page("veelgestelde-vragen/", 1, "Veelgestelde vragen | CALMMINI",
        "Antwoorden op veelgestelde vragen over CALMMINI, Marokkaanse verzorgingsproducten en het hammamritueel.",
        faq_body, jsonld=[crumb_ld, faq_ld])

    # Shipping/returns (enriched from client's terms), privacy (placeholder), terms (real)
    ph = lambda: '<p><em>[Deze tekst is een placeholder en wordt later door CALMMINI ingevuld.]</em></p>'
    ship_inner = (
        "<h2>Verzending</h2>"
        "<p>CALMMINI bezorgt in heel Nederland. Binnen Nederland gelden vaste verzendkosten. "
        "We streven ernaar je bestelling binnen 5–10 werkdagen na bevestiging te leveren.</p>"
        "<h2>Buiten Nederland</h2>"
        "<p>Bij leveringen buiten de EU zijn eventuele invoerrechten voor rekening van de klant.</p>"
        "<h2>Retourneren &amp; garantie</h2>"
        "<p>Voor consumenten geldt een garantie van 2 jaar dat producten bij levering aan de "
        "overeenkomst voldoen. Neem voor retouren of vragen contact met ons op via "
        "<a href=\"mailto:%s\">%s</a>. De volledige voorwaarden lees je in onze "
        "<a href=\"%s\">algemene voorwaarden</a>.</p>" % (
            BRAND["email"], BRAND["email"], href(rel_prefix(1), "algemene-voorwaarden/")))
    simple_page("verzending-en-retour/", "Verzending & retour | CALMMINI",
        "Informatie over verzending, levertijd en retourneren bij CALMMINI.",
        "Verzending & retour", "Alles over bezorging en retourneren.",
        ship_inner,
        crumbtrail=[("Home",""),("Verzending & retour","verzending-en-retour/")])
    simple_page("privacybeleid/", "Privacybeleid | CALMMINI",
        "Het privacybeleid van CALMMINI.",
        "Privacybeleid", "", "<h2>Privacy</h2>"+ph()+"<h2>Cookies</h2>"+ph()+"<h2>Je rechten</h2>"+ph(),
        crumbtrail=[("Home",""),("Privacybeleid","privacybeleid/")])
    terms_inner = (
        '<p class="lead">CalmMini Hammamrituelen · %s · '
        '<a href="mailto:%s">%s</a></p>' % (BRAND["city"], BRAND["email"], BRAND["email"])
        + '<div class="legal">' + "".join(
            "<h2>%d. %s</h2><p>%s</p>" % (i+1, esc(t), esc(txt))
            for i, (t, txt) in enumerate(TERMS)) + "</div>")
    simple_page("algemene-voorwaarden/", "Algemene voorwaarden | CALMMINI",
        "De algemene voorwaarden van CalmMini Hammamrituelen.",
        "Algemene voorwaarden", "", terms_inner,
        crumbtrail=[("Home",""),("Algemene voorwaarden","algemene-voorwaarden/")])

def build_guide():
    rel = rel_prefix(1)
    crumb, crumb_ld = breadcrumb(rel, [("Home",""),("Gebruik & ritueel","gebruik-en-ritueel/")])
    secs = []
    for c in CATEGORIES:
        prods = products_in_cat(c["slug"])
        usage = "<p class=\"lead\">%s</p>" % esc(c["intro"])
        if c.get("tip"):
            usage += ('<div class="tip-note"><strong>Tip</strong> %s</div>' % esc(c["tip"]))
        secs.append("""
<section class="section{alt}" id="{slug}">
  <div class="wrap">
    <div class="guide-head">
      <span class="eyebrow">Stap {n}</span>
      <h2>{name}</h2>
      {usage}
      <a class="link-more" href="{caturl}">Bekijk alle {name} {arrow}</a>
    </div>
    {grid}
  </div>
</section>""".format(alt=" tint" if len(secs)%2 else "", slug=c["slug"], n=len(secs)+1,
                     name=esc(c["name"]), usage=usage,
                     caturl=href(rel,"categorie/%s/"%c["slug"]), arrow=IC["arrow"],
                     grid=product_grid(rel, prods)))
    more = "".join(
        '<a class="link-more" href="%s">%s %s</a>' %
        (href(rel,"blog/%s/"%b["slug"]), esc(b["title"]), IC["arrow"]) for b in BLOG)
    body = """
<div class="page-hero"><div class="wrap">
  <span class="eyebrow">Gebruik &amp; ritueel</span>
  <h1>Gebruik &amp; ritueel</h1>
  <p class="lead">Ontdek stap voor stap hoe je onze producten op een fijne en veilige manier gebruikt. Zo haal je het meeste uit jouw hammamritueel thuis.</p>
</div></div>
{crumb}
{secs}
<section class="section"><div class="wrap narrow">
  <div class="fineprint">{disc}</div>
  <h2 style="margin-top:2rem">Meer lezen</h2>
  <div class="more-links">{more}</div>
</div></section>
""".format(crumb=crumb, secs="".join(secs), disc=esc(BRAND["disclaimer"]), more=more)
    page("gebruik-en-ritueel/", 1,
         "Gebruik & ritueel — zo gebruik je onze hammamproducten | CALMMINI",
         "Ontdek stap voor stap hoe je sabon beldi, ghassoul, klei, hammampoeder, oliën, "
         "butter en scrub gebruikt. Zo haal je het meeste uit jouw hammamritueel thuis.",
         body, active="guide", jsonld=[crumb_ld])

def build_404():
    rel = rel_prefix(0)
    body = """
<section class="section"><div class="wrap narrow empty-state">
  <div class="err-code">404</div>
  <h1 style="font-size:clamp(2.4rem,6vw,3.6rem)">Pagina niet gevonden</h1>
  <p class="lead" style="margin-inline:auto">Deze pagina bestaat niet (meer). Keer terug naar de webshop of ontdek het hammamritueel.</p>
  <div class="hero-cta" style="justify-content:center;margin-top:1.4rem">
    <a class="btn btn-primary btn-lg" href="{home}">Naar home</a>
    <a class="btn btn-ghost btn-lg" href="{prod}">Alle producten</a>
  </div>
</div></section>
""".format(home=href(rel,""), prod=href(rel,"producten/"))
    page("", 0, "Pagina niet gevonden | CALMMINI",
         "De opgevraagde pagina is niet gevonden.", body, filename="404.html")
