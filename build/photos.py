# -*- coding: utf-8 -*-
"""Place real CALMMINI product photos (with harmonised backgrounds),
build category images, and process the real logo + hero photo."""
import os, glob
import numpy as np
from PIL import Image, ImageFilter
from data import PRODUCTS, CATEGORIES
import make_assets as MA

UP = "/mnt/user-data/uploads"
IMG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
PROD = os.path.join(IMG, "products")
CATS = os.path.join(IMG, "categories")

SRC = sorted(glob.glob(os.path.join(UP, "ChatGPT_Image_*.png")))
LOGO_SRC = os.path.join(UP, "WhatsApp_Image_2026-08-31_at_11_37_01.jpeg")
HERO_SRC = os.path.join(UP, "WhatsApp_Image_2026-08-31_at_13_15_10.jpeg")

# slug -> index in SRC (verified via montage)
PHOTO = {
    "sabon-beldi-eucalyptus": 0, "rode-klei": 1, "ghassoul-oranjebloesem": 2,
    "ghassoul-roos": 4, "groene-klei": 5, "saffloerolie": 6, "abrikozenpitolie": 7,
    "sabon-beldi-nila": 8, "aloe-vera-olie": 9, "hammamkruiden-lichaam": 10,
    "shea-butter": 11, "sabon-beldi-naturel": 12, "sabon-beldi-aker-fassi": 13,
    "sabon-beldi-musk": 14,
}
CAT_HERO = {
    "sabon-beldi": "sabon-beldi-naturel",
    "ghassoul-klei": "ghassoul-roos",
    "hammampoeder": "hammamkruiden-lichaam",
    "verzorgingsolien": "saffloerolie",
    "butter-scrub": "shea-butter",
    "accessoires": None,
}

# one consistent, warm cream background for every product photo
TARGET_BG = np.array([244.0, 238.0, 227.0])

def clean(d):
    for f in glob.glob(os.path.join(d, "*.jpg")):
        os.remove(f)

def normalise_bg(im):
    """Recolour the (light) studio background to one uniform cream so all
    product photos match, while keeping the product and its soft shadow."""
    a = np.asarray(im.convert("RGB"), dtype=np.float32)
    h, w, _ = a.shape
    # sample background from the four corners
    c = np.array([16, 16])
    corners = np.stack([a[c[0], c[1]], a[c[0], w-c[1]], a[h-c[0], c[1]], a[h-c[0], w-c[1]]])
    bg = corners.mean(axis=0)
    shift = TARGET_BG - bg
    shifted = a + shift
    dist = np.sqrt(((a - bg) ** 2).sum(axis=2))
    # w=0 near background (use shifted), w=1 on product (keep original)
    D0, D1 = 22.0, 58.0
    wmask = np.clip((dist - D0) / (D1 - D0), 0.0, 1.0)[..., None]
    out = shifted * (1 - wmask) + a * wmask
    out = np.clip(out, 0, 255).astype(np.uint8)
    return Image.fromarray(out, "RGB")

def save_product_photo(slug, src_path):
    im = Image.open(src_path).convert("RGB")
    im = normalise_bg(im)
    im = im.resize((900, 1125), Image.LANCZOS)
    im.save(os.path.join(PROD, slug + ".jpg"), "JPEG", quality=88, optimize=True)

def category_shelf(slug, hero_slug):
    src = os.path.join(PROD, hero_slug + ".jpg")   # use the normalised photo
    im = Image.open(src).convert("RGB")
    W, H = 1200, 800
    canvas = Image.new("RGB", (W, H), tuple(int(x) for x in TARGET_BG))
    th = int(H * 0.92); tw = int(th * im.width / im.height)
    canvas.paste(im.resize((tw, th), Image.LANCZOS), ((W - tw)//2, (H - th)//2))
    canvas.save(os.path.join(CATS, slug + ".jpg"), "JPEG", quality=88, optimize=True)

def build_logo():
    im = Image.open(LOGO_SRC).convert("RGB")
    a = np.asarray(im, dtype=np.float32)
    d = 255.0 - a.min(axis=2)              # 0 = pure white
    alpha = np.clip(d * 14.0, 0, 255).astype(np.uint8)
    rgba = np.dstack([a.astype(np.uint8), alpha])
    out = Image.fromarray(rgba, "RGBA")
    # trim to content bbox
    bbox = Image.fromarray(alpha, "L").point(lambda v: 255 if v > 12 else 0).getbbox()
    if bbox:
        pad = 24
        l, t, r, b = bbox
        out = out.crop((max(0, l-pad), max(0, t-pad), min(im.width, r+pad), min(im.height, b+pad)))
    out.save(os.path.join(IMG, "logo.png"))
    # white/knockout version for dark footer (keep gold, it reads on dark)
    return out

def _crop_to(im, ratio_w, ratio_h):
    w, h = im.size
    target = ratio_w / ratio_h
    if w / h > target:            # too wide -> crop sides
        nw = int(h * target); x = (w - nw)//2
        return im.crop((x, 0, x+nw, h))
    nh = int(w / target); y = (h - nh)//2
    return im.crop((0, y, w, y+nh))

def build_hero_and_og():
    im = Image.open(HERO_SRC).convert("RGB")
    # hero: portrait 4:5 for the arch frame
    hero = _crop_to(im, 4, 5).resize((1000, 1250), Image.LANCZOS)
    hero.save(os.path.join(IMG, "hero.jpg"), "JPEG", quality=86, optimize=True)
    # sfeer: landscape for the "van badkamer" section
    sfeer = _crop_to(im, 5, 4).resize((1100, 880), Image.LANCZOS)
    sfeer.save(os.path.join(IMG, "sfeer.jpg"), "JPEG", quality=86, optimize=True)
    # og: 1200x630 social card
    og = _crop_to(im, 1200, 630).resize((1200, 630), Image.LANCZOS)
    og.save(os.path.join(IMG, "og-image.jpg"), "JPEG", quality=85, optimize=True)

def main():
    os.makedirs(PROD, exist_ok=True); os.makedirs(CATS, exist_ok=True)
    clean(PROD); clean(CATS)
    slugs = {p["slug"] for p in PRODUCTS}
    for slug, idx in PHOTO.items():
        assert slug in slugs, "unknown slug " + slug
        save_product_photo(slug, SRC[idx])
    for p in PRODUCTS:
        if p["slug"] not in PHOTO:
            MA.framed_placeholder(os.path.join(PROD, p["slug"] + ".jpg"),
                                  900, 1125, p["name"], kicker="CALMMINI",
                                  dark=False, footer="Productfoto volgt")
    for c in CATEGORIES:
        hero = CAT_HERO.get(c["slug"])
        if hero:
            category_shelf(c["slug"], hero)
        else:
            MA.framed_placeholder(os.path.join(CATS, c["slug"] + ".jpg"),
                                  1200, 800, c["name"], kicker="Categorie", dark=True, footer="")
    build_logo()
    build_hero_and_og()
    print("photos: %d products, %d categories, logo+hero+og done" %
          (len(glob.glob(PROD+'/*.jpg')), len(glob.glob(CATS+'/*.jpg'))))

if __name__ == "__main__":
    main()
