# -*- coding: utf-8 -*-
import os
"""Generate elegant, on-brand placeholder imagery for CALMMINI.
Every image is a real raster file so it can be swapped 1:1 for a real photo
later (keep the same filename). Look: warm 'riad' palette + Moorish arch motif."""
import math, os
from PIL import Image, ImageDraw, ImageFont
from data import PRODUCTS, CATEGORIES, BLOG, BRAND

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
SS = 2  # supersample for crisp anti-aliased strokes

# ---- palette ----
SAND      = (241, 234, 219)
CREAM     = (251, 246, 236)
SAND_DEEP = (233, 222, 200)
GOLD      = (168, 126, 52)
GOLD_SOFT = (216, 192, 138)
GOLD_LT   = (198, 167, 106)
OLIVE     = (110, 115, 85)
ESPRESSO  = (36, 29, 21)
ESP_SOFT  = (52, 44, 33)
INK       = (43, 36, 28)
INK_SOFT  = (110, 98, 85)

SERIF   = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS    = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def vgradient(w, h, top, bottom):
    base = Image.new("RGB", (w, h), top)
    top_r, top_g, top_b = top
    dr, dg, db = bottom[0]-top[0], bottom[1]-top[1], bottom[2]-top[2]
    px = base.load()
    for y in range(h):
        t = y / max(1, h-1)
        c = (int(top_r+dr*t), int(top_g+dg*t), int(top_b+db*t))
        for x in range(w):
            px[x, y] = c
    return base

def arch_points(cx, yb, hw, spring, r_factor=1.28, steps=90):
    """Outline points of a tall Moorish arch (base + sides + circular top)."""
    r = hw * r_factor
    yc = spring
    y_meet = yc - math.sqrt(max(0.0, r*r - hw*hw))
    pts = [(cx - hw, yb), (cx - hw, y_meet)]
    for i in range(steps+1):
        x = (cx - hw) + (2*hw) * (i/steps)
        dx = x - cx
        y = yc - math.sqrt(max(0.0, r*r - dx*dx))
        pts.append((x, y))
    pts += [(cx + hw, y_meet), (cx + hw, yb)]
    return pts

def draw_star(draw, cx, cy, rr, color, width):
    """8-point khatam star as two overlapping squares (outline)."""
    for rot in (0, math.pi/4):
        p = []
        for k in range(4):
            a = rot + k*math.pi/2
            p.append((cx + rr*math.cos(a), cy + rr*math.sin(a)))
        p.append(p[0])
        draw.line(p, fill=color, width=width, joint="curve")

def wrap(draw, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= maxw:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def spaced(s, n=1):
    return (" "*n).join(list(s))

def wordmark(draw, cx, y, size, color, track=6):
    f = font(SANS, size)
    txt = spaced(BRAND["name"], 1)
    # manual letter spacing
    letters = list(BRAND["name"])
    widths = [draw.textlength(c, font=f) for c in letters]
    total = sum(widths) + track*(len(letters)-1)
    x = cx - total/2
    for c, wc in zip(letters, widths):
        draw.text((x, y), c, font=f, fill=color)
        x += wc + track

def base_canvas(w, h, top, bottom):
    return vgradient(w*SS, h*SS, top, bottom)

def finish(img, w, h, path):
    img = img.resize((w, h), Image.LANCZOS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.convert("RGB").save(path, "JPEG", quality=88, optimize=True)

def framed_placeholder(path, w, h, title, kicker=None, dark=False, footer="Productfoto volgt"):
    W, H = w*SS, h*SS
    if dark:
        img = base_canvas(w, h, ESP_SOFT, ESPRESSO)
        arch_col, star_col, title_col, kick_col, foot_col, wm_col = (
            GOLD_LT, GOLD, CREAM, GOLD_SOFT, (150,138,120), GOLD_SOFT)
    else:
        img = base_canvas(w, h, CREAM, SAND_DEEP)
        arch_col, star_col, title_col, kick_col, foot_col, wm_col = (
            GOLD, GOLD, INK, GOLD, INK_SOFT, GOLD)
    d = ImageDraw.Draw(img)

    # thin inner border frame
    m = int(min(W, H) * 0.055)
    d.rectangle([m, m, W-m, H-m], outline=arch_col, width=max(2, SS))

    # central Moorish arch
    hw = W * 0.24
    cx = W/2
    yb = H*0.72
    spring = H*0.5
    pts = arch_points(cx, yb, hw, spring, r_factor=1.3, steps=120)
    d.line(pts + [pts[0]], fill=arch_col, width=SS*2, joint="curve")
    # faint second inner arch
    pts2 = arch_points(cx, yb-6*SS, hw*0.8, spring+H*0.04, r_factor=1.32, steps=120)
    d.line(pts2 + [pts2[0]], fill=arch_col, width=SS, joint="curve")


    # kicker
    if kicker:
        fk = font(SANS, int(H*0.028))
        kt = spaced(kicker.upper(), 1)
        d.text((cx - d.textlength(kt, font=fk)/2, H*0.135), kt, font=fk, fill=kick_col)

    # title (serif, wrapped) below arch
    ft = font(SERIF, int(H*0.062))
    lines = wrap(d, title, ft, W*0.72)
    ty = yb + H*0.045
    for ln in lines:
        d.text((cx - d.textlength(ln, font=ft)/2, ty), ln, font=ft, fill=title_col)
        ty += int(H*0.075)

    # footer caption
    ff = font(SANS, int(H*0.026))
    fdt = footer
    d.text((cx - d.textlength(fdt, font=ff)/2, H*0.9), fdt, font=ff, fill=foot_col)

    finish(img, w, h, path)

def hero_image(path, w, h):
    W, H = w*SS, h*SS
    img = base_canvas(w, h, (58,50,37), ESPRESSO)
    d = ImageDraw.Draw(img)
    # large offset arch silhouette on the right
    hw = W*0.3
    cx = W*0.72
    pts = arch_points(cx, H*1.02, hw, H*0.52, r_factor=1.35, steps=140)
    d.line(pts + [pts[0]], fill=(120, 92, 44), width=SS*3, joint="curve")
    pts2 = arch_points(cx, H*1.02, hw*0.7, H*0.6, r_factor=1.4, steps=140)
    d.line(pts2 + [pts2[0]], fill=(150, 116, 58), width=SS*2, joint="curve")
    finish(img, w, h, path)

def og_image(path, w, h):
    W, H = w*SS, h*SS
    img = base_canvas(w, h, ESP_SOFT, ESPRESSO)
    d = ImageDraw.Draw(img)
    m = int(min(W,H)*0.06)
    d.rectangle([m, m, W-m, H-m], outline=GOLD_LT, width=SS)
    wordmark(d, W/2, H*0.44, int(H*0.13), CREAM, track=SS*7)
    ft = font(SERIF, int(H*0.075))
    sub = "Hammamrituelen"
    d.text((W/2 - d.textlength(sub, font=ft)/2, H*0.62), sub, font=ft, fill=GOLD_SOFT)
    fk = font(SANS, int(H*0.042))
    tag = spaced("MAROKKAANSE NATUURLIJKE VERZORGING", 1)
    d.text((W/2 - d.textlength(tag, font=fk)/2, H*0.75), tag, font=fk, fill=(150,138,120))
    finish(img, w, h, path)

# ---------------------------------------------------------------------------
def main():
    # products (portrait)
    for p in PRODUCTS:
        framed_placeholder(f"{OUT}/products/{p['slug']}.jpg", 900, 1125,
                           p["name"], kicker="CALMMINI", footer="Productfoto volgt")
    # categories (landscape)
    for c in CATEGORIES:
        framed_placeholder(f"{OUT}/categories/{c['slug']}.jpg", 1200, 800,
                           c["name"], kicker="Categorie", dark=True, footer="Sfeerbeeld volgt")
    # blog (landscape)
    for b in BLOG:
        short = b["title"].split(":")[0]
        framed_placeholder(f"{OUT}/blog/{b['slug']}.jpg", 1200, 760,
                           short, kicker="Journal", footer="Beeld volgt")
    # hero + secondary lifestyle
    hero_image(f"{OUT}/hero.jpg", 1600, 1150)
    framed_placeholder(f"{OUT}/ritueel.jpg", 1000, 1150, "Het Ritueel",
                       kicker="Hammam", dark=True, footer="Sfeerbeeld volgt")
    framed_placeholder(f"{OUT}/verhaal.jpg", 1000, 900, "Ons Verhaal",
                       kicker="CALMMINI", footer="Sfeerbeeld volgt")
    framed_placeholder(f"{OUT}/ingredienten.jpg", 1000, 900, "Natuurlijke Basis",
                       kicker="Ingrediënten", dark=True, footer="Sfeerbeeld volgt")
    og_image(f"{OUT}/og-image.jpg", 1200, 630)
    print("images done")

if __name__ == "__main__":
    main()
