# -*- coding: utf-8 -*-
import os, json, html
from data import (BRAND, CATEGORIES, PRODUCTS, BLOG, eur, cat_by_slug,
                  products_in_cat)

import os as _os
ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), ".."))
DOMAIN = BRAND["domain"]

# --------------------------------------------------------------------------- #
#  icons (inline stroke SVG)                                                   #
# --------------------------------------------------------------------------- #
def svg(body, vb="0 0 24 24", extra=""):
    return ('<svg viewBox="%s" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" %s>%s</svg>' % (vb, extra, body))

IC = {
    "cart": svg('<path d="M6 6h15l-1.5 9h-12z"/><path d="M6 6L5 3H2"/><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/>'),
    "search": svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'),
    "menu": svg('<path d="M3 6h18M3 12h18M3 18h18"/>'),
    "close": svg('<path d="M6 6l12 12M18 6L6 18"/>'),
    "chev": svg('<path d="M2 4l4 4 4-4"/>', vb="0 0 12 12"),
    "arrow": svg('<path d="M4 10h12M11 5l5 5-5 5"/>', vb="0 0 20 20"),
    "check": svg('<path d="M20 6L9 17l-5-5"/>'),
    "leaf": svg('<path d="M11 20A7 7 0 0 1 4 13c0-5 5-9 16-9 0 8-4 13-9 13z"/><path d="M11 20c0-5 2-8 6-10"/>'),
    "moon": svg('<path d="M12 3a6 6 0 1 0 9 9 9 9 0 1 1-9-9z"/>'),
    "star": svg('<path d="M12 3l2.2 5.5L20 9l-4 3.8L17 19l-5-3-5 3 1-6.2L4 9l5.8-.5z"/>'),
    "truck": svg('<path d="M3 6h11v9H3zM14 9h4l3 3v3h-7z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/>'),
    "sparkle": svg('<path d="M12 3v6M12 15v6M3 12h6M15 12h6"/><path d="M6 6l3 3M15 15l3 3M18 6l-3 3M9 15l-3 3"/>'),
    "shield": svg('<path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6z"/><path d="M9 12l2 2 4-4"/>'),
    "heart": svg('<path d="M12 20s-7-4.5-9-9c-1.3-3 .6-6 3.5-6C8.5 5 12 8 12 8s3.5-3 5.5-3c2.9 0 4.8 3 3.5 6-2 4.5-9 9-9 9z"/>'),
    "drop": svg('<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>'),
}

def star_svg(color="#A87E34", size=26):
    return ('<svg width="%d" height="%d" viewBox="0 0 40 40" fill="none" '
            'stroke="%s" stroke-width="1.3"><path d="M20 4l4 12 12 4-12 4-4 12-4-12-12-4 12-4z"/>'
            '<path d="M20 8l3 9 9 3-9 3-3 9-3-9-9-3 9-3z" opacity=".5"/></svg>' % (size, size, color))

# --------------------------------------------------------------------------- #
#  path helpers                                                               #
# --------------------------------------------------------------------------- #
def rel_prefix(depth):
    return "../" * depth

def href(rel, folder):
    """internal link that also resolves on file:// (explicit index.html)."""
    if folder == "":
        return rel + "index.html"
    return rel + folder + "index.html"

def asset(rel, path):
    return rel + "assets/" + path

def canon(folder):
    return DOMAIN + "/" + folder

def esc(s):
    return html.escape(s, quote=True)

# --------------------------------------------------------------------------- #
#  <head>                                                                      #
# --------------------------------------------------------------------------- #
def head(rel, title, desc, folder, og_type="website", jsonld=None, og_image=None):
    canonical = canon(folder)
    ogimg = og_image or (DOMAIN + "/assets/img/og-image.jpg")
    parts = ['<!doctype html>', '<html lang="nl">', '<head>',
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<title>%s</title>' % esc(title),
        '<meta name="description" content="%s">' % esc(desc),
        '<link rel="canonical" href="%s">' % canonical,
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        '<meta name="theme-color" content="#2A251F">',
        '<meta name="format-detection" content="telephone=no">',
        # Open Graph
        '<meta property="og:type" content="%s">' % og_type,
        '<meta property="og:site_name" content="CALMMINI">',
        '<meta property="og:locale" content="nl_NL">',
        '<meta property="og:title" content="%s">' % esc(title),
        '<meta property="og:description" content="%s">' % esc(desc),
        '<meta property="og:url" content="%s">' % canonical,
        '<meta property="og:image" content="%s">' % ogimg,
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % esc(title),
        '<meta name="twitter:description" content="%s">' % esc(desc),
        '<meta name="twitter:image" content="%s">' % ogimg,
        # perf: preconnect + fonts
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap">',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" media="all">',
        '<link rel="preload" as="image" href="%s" fetchpriority="high">' % (asset(rel,"img/hero.jpg")) if folder=="" else "",
        '<link rel="stylesheet" href="%s">' % asset(rel, "css/style.css"),
        '<link rel="icon" href="%s" type="image/svg+xml">' % (rel + "favicon.svg"),
        '<link rel="apple-touch-icon" href="%s">' % asset(rel, "img/og-image.jpg"),
        '<link rel="manifest" href="%s">' % (rel + "site.webmanifest"),
        '<link rel="sitemap" type="application/xml" href="%s">' % (rel + "sitemap.xml"),
    ]
    if jsonld:
        for block in jsonld:
            parts.append('<script type="application/ld+json">%s</script>'
                         % json.dumps(block, ensure_ascii=False))
    parts.append('</head>')
    return "\n".join([p for p in parts if p != ""])

# --------------------------------------------------------------------------- #
#  header / footer                                                            #
# --------------------------------------------------------------------------- #
def brand_block(rel, footer=False):
    cls = "footer-brand" if footer else "brand"
    return ('<a href="%s" class="%s" aria-label="CALMMINI Hammamrituelen home">'
            '<img src="%s" alt="CALMMINI Hammamrituelen" class="brand-logo" '
            'width="240" height="110" %s></a>'
            % (href(rel, ""), cls, asset(rel, "img/logo.png"),
               'loading="lazy"' if footer else 'fetchpriority="high"'))

def header(rel, active=""):
    cat_links = "".join(
        '<a href="%s">%s</a>' % (href(rel, "categorie/%s/" % c["slug"]), esc(c["menu"]))
        for c in CATEGORIES)
    nav_item = lambda folder, label, key: (
        '<a href="%s"%s>%s</a>' % (href(rel, folder), ' aria-current="page"' if active==key else "", label))
    return """
<div class="topbar"><span>Marokkaanse hammamverzorging — natuurlijk &amp; traditioneel</span></div>
<header class="site-header">
  <div class="header-inner">
    {brand}
    <nav class="main-nav" aria-label="Hoofdmenu">
      {home}
      <div class="has-menu">
        <button class="menu-toggle" aria-haspopup="true" aria-expanded="false">Producten {chev}</button>
        <div class="dropdown" role="menu">
          <a href="{allprod}"><strong>Alle producten</strong></a>
          {cats}
        </div>
      </div>
      {blog}
      {over}
      {contact}
    </nav>
    <div class="header-actions">
      <button class="icon-btn" data-open-search aria-label="Zoeken">{search}</button>
      <a class="icon-btn" href="{cart}" aria-label="Winkelwagen">{carticon}<span class="cart-count" data-cart-count hidden>0</span></a>
      <button class="icon-btn nav-burger" data-open-nav aria-label="Menu openen">{menu}</button>
    </div>
  </div>
  <div class="search-panel">
    <form action="{allprod}" method="get" role="search">
      <input type="search" name="q" placeholder="Zoek naar sabon beldi, ghassoul, kruiden…" aria-label="Zoekterm">
      <button class="btn btn-primary" type="submit">Zoeken</button>
    </form>
  </div>
</header>
<div class="scrim" data-close></div>
<aside class="mobile-nav" aria-label="Mobiel menu">
  <div class="m-head">{brand2}<button class="icon-btn" data-close aria-label="Sluiten">{close}</button></div>
  {home}
  {blog}
  {over}
  {contact}
  <div class="m-sub">Categorieën</div>
  <a href="{allprod}">Alle producten</a>
  {cats}
</aside>
""".format(
        brand=brand_block(rel), brand2=brand_block(rel),
        home=nav_item("", "Home", "home"),
        blog=nav_item("gebruik-en-ritueel/", "Gebruik &amp; ritueel", "guide"),
        over=nav_item("over-calmmini/", "Over Calmmini", "over"),
        contact=nav_item("contact/", "Contact", "contact"),
        allprod=href(rel, "producten/"),
        cats=cat_links, chev=IC["chev"], search=IC["search"],
        cart=href(rel, "winkelwagen/"), carticon=IC["cart"],
        menu=IC["menu"], close=IC["close"])

def footer(rel):
    cat_links = "".join('<a href="%s">%s</a>' % (href(rel,"categorie/%s/"%c["slug"]), esc(c["menu"])) for c in CATEGORIES[:6])
    return """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        {brand}
        <p>Rust voor mij. Gewoon thuis. Natuurlijke Marokkaanse hammamverzorging voor haar, lichaam en een rustgevend ritueel thuis.</p>
        <p class="footer-loc">{city} · Nederland</p>
      </div>
      <div class="footer-col">
        <h4>Winkel</h4>
        <a href="{allprod}">Alle producten</a>
        {cats}
      </div>
      <div class="footer-col">
        <h4>Informatie</h4>
        <a href="{over}">Over Calmmini</a>
        <a href="{blog}">Gebruik &amp; ritueel</a>
        <a href="{faq}">Veelgestelde vragen</a>
        <a href="{ship}">Verzending &amp; retour</a>
        <a href="{contact}">Contact</a>
      </div>
      <div class="footer-col">
        <h4>Klantenservice</h4>
        <a href="mailto:{email}">{email}</a>
        <a href="{contact}">Stuur een bericht</a>
        <a href="{privacy}">Privacybeleid</a>
        <a href="{terms}">Algemene voorwaarden</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {year} CALMMINI Hammamrituelen · Alle rechten voorbehouden</span>
      <span class="pay"><span>iDEAL</span><span>Bancontact</span><span>Visa</span><span>Mastercard</span><span>PayPal</span></span>
    </div>
  </div>
</footer>
""".format(brand=brand_block(rel, footer=True), allprod=href(rel,"producten/"),
           cats=cat_links, over=href(rel,"over-calmmini/"), blog=href(rel,"gebruik-en-ritueel/"),
           faq=href(rel,"veelgestelde-vragen/"), ship=href(rel,"verzending-en-retour/"),
           contact=href(rel,"contact/"), privacy=href(rel,"privacybeleid/"),
           terms=href(rel,"algemene-voorwaarden/"), email=BRAND["email"],
           city=BRAND["city"], year=2026)

def scripts(rel):
    return ('<script>window.CALMMINI_BASE="%s";</script>'
            '<script src="%s"></script>'
            '<script src="%s"></script>'
            % (rel, asset(rel,"js/data.js"), asset(rel,"js/app.js")))

# --------------------------------------------------------------------------- #
#  reusable blocks                                                             #
# --------------------------------------------------------------------------- #
def breadcrumb(rel, trail):
    """trail = list of (label, folder|None). Last item = current."""
    items, ld = [], []
    for i, (label, folder) in enumerate(trail):
        if folder is None or i == len(trail)-1:
            items.append('<span aria-current="page">%s</span>' % esc(label))
        else:
            items.append('<a href="%s">%s</a>' % (href(rel, folder), esc(label)))
        if i < len(trail)-1:
            items.append('<span class="sep">/</span>')
        ld.append({"@type":"ListItem","position":i+1,"name":label,
                   "item": canon(folder) if folder is not None else canon(trail[i][1] or "")})
    nav = '<nav class="crumb wrap" aria-label="Kruimelpad">%s</nav>' % "".join(items)
    ld_block = {"@context":"https://schema.org","@type":"BreadcrumbList",
                "itemListElement":[{"@type":"ListItem","position":i+1,"name":t[0],
                    "item":canon(t[1])} for i,t in enumerate(trail) if t[1] is not None]}
    return nav, ld_block

def product_card(rel, p, index):
    cats = " ".join([p["cat"]] + p["extra_cats"])
    badge = ""
    if p["badge"]:
        cls = "badge gold" if p["badge"] in ("Bestseller","Nieuw") else "badge"
        badge = '<span class="%s">%s</span>' % (cls, esc(p["badge"]))
    cat_name = cat_by_slug(p["cat"])["name"]
    return """
<article class="card reveal" data-cat="{cats}" data-price="{price:.2f}" data-name="{name}" data-index="{index}" data-qty-scope>
  <div class="card-media">
    {badge}
    <a href="{url}" aria-label="{name}"><img src="{img}" alt="{name} — {catname} van CALMMINI" loading="lazy" width="900" height="1125"></a>
    <div class="card-quick"><button class="btn btn-primary btn-block" data-add="{slug}">In winkelwagen</button></div>
  </div>
  <div class="card-body">
    <div class="card-cat">{catname}</div>
    <h3 class="card-title"><a href="{url}">{name}</a></h3>
    <p class="card-blurb">{blurb}</p>
    <div class="card-foot"><span class="price">{eur}</span>
      <a class="link-more" href="{url}">Bekijk {arrow}</a></div>
  </div>
</article>""".format(
        cats=cats, price=p["price"], name=esc(p["name"]), index=index, badge=badge,
        url=href(rel,"product/%s/"%p["slug"]), img=asset(rel,"img/products/%s.jpg"%p["slug"]),
        slug=p["slug"], catname=esc(cat_name), blurb=esc(p["blurb"]), eur=eur(p["price"]),
        arrow=IC["arrow"])

def product_grid(rel, prods, cols3=False, start=0):
    cls = "prod-grid cols-3" if cols3 else "prod-grid"
    cards = "".join(product_card(rel, p, start+i) for i, p in enumerate(prods))
    return '<div class="%s" data-grid>%s</div>' % (cls, cards)

# --------------------------------------------------------------------------- #
#  write helper                                                               #
# --------------------------------------------------------------------------- #
def write(folder, html_str, filename="index.html"):
    d = os.path.join(ROOT, folder)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, filename), "w", encoding="utf-8") as f:
        f.write(html_str)

def page(folder, depth, title, desc, body, active="", jsonld=None, og_type="website",
         og_image=None, filename="index.html"):
    rel = rel_prefix(depth)
    doc = (head(rel, title, desc, folder, og_type=og_type, jsonld=jsonld, og_image=og_image)
           + '\n<body>\n' + header(rel, active) + '\n<main id="main">\n'
           + body + '\n</main>\n' + footer(rel) + '\n' + scripts(rel) + '\n</body>\n</html>')
    write(folder, doc, filename)
