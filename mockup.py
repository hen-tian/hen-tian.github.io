#!/usr/bin/env python3
"""Cookie mockup v5 - mirror + heavy rotation to hide duplication."""
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random

c1 = Image.open('assets/classic-cookie-single.png').convert('RGBA')
c2 = Image.open('assets/classic-cookie-2.png').convert('RGBA')

target_w = 260
def scale_cookie(img):
    r = target_w / img.width
    return img.resize((target_w, int(img.height * r)), Image.LANCZOS)

c1 = scale_cookie(c1)
c2 = scale_cookie(c2)

# Create mirrored versions
c1_flip = c1.transpose(Image.FLIP_LEFT_RIGHT)
c2_flip = c2.transpose(Image.FLIP_LEFT_RIGHT)

# Canvas
pkg_w, pkg_h = 800, 600
pkg = Image.new('RGBA', (pkg_w, pkg_h), (35, 32, 30, 255))
draw = ImageDraw.Draw(pkg)

for y in range(pkg_h):
    v = int(30 + 15 * (y / pkg_h))
    draw.line([(0, y), (pkg_w, y)], fill=(v, v-2, v-4, 255))

# Tray
tray_margin = 35
tw, th = pkg_w - tray_margin*2, pkg_h - tray_margin*2 - 50
tray = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
td = ImageDraw.Draw(tray)
td.rounded_rectangle([0, 0, tw-1, th-1], radius=16, fill=(45, 42, 38, 255))
for i in range(6):
    alpha = int(18 - i * 3)
    if alpha <= 0: break
    td.rounded_rectangle([i, i, tw-1-i, th-1-i], radius=16-i, outline=(75, 70, 65, alpha), width=1)
pkg.paste(tray, (tray_margin, tray_margin), tray)

# 4 cookies: each unique (original, flipped, different variant)
# Top-left: c1 original, rotated
# Top-right: c2 flipped, rotated differently
# Bottom-left: c2 original, rotated
# Bottom-right: c1 flipped, rotated
cookie_variants = [
    (c1,       -18, 1.0),   # shape A original
    (c2_flip,  12,  0.96),  # shape B mirrored
    (c2,       22,  0.93),  # shape B original
    (c1_flip,  -8,  0.98),  # shape A mirrored
]

positions = [
    (250, 180),
    (540, 175),
    (240, 380),
    (550, 385),
]

for i, ((src, angle, scale), (cx, cy)) in enumerate(zip(cookie_variants, positions)):
    rot = src.rotate(angle, expand=True, resample=Image.BICUBIC)
    nw, nh = int(rot.width * scale), int(rot.height * scale)
    rot = rot.resize((nw, nh), Image.LANCZOS)
    
    # Shadow
    glow = Image.new('RGBA', (nw + 40, nh + 40), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gcx, gcy = (nw + 40) // 2, (nh + 40) // 2 + 15
    for r in range(55, 0, -2):
        a = int(7 * (1 - r/55))
        gd.ellipse([gcx - r*2, gcy - r//2, gcx + r*2, gcy + r//2], fill=(0, 0, 0, a))
    glow = glow.filter(ImageFilter.GaussianBlur(8))
    
    gx = cx - (nw + 40) // 2
    gy = cy - (nh + 40) // 2
    pkg.paste(glow, (gx, gy), glow)
    
    px = cx - nw // 2
    py = cy - nh // 2
    pkg.paste(rot, (px, py), rot)
    print(f"  Cookie {i+1}: variant={'A' if src in (c1, c1_flip) else 'B'} "
          f"{'mirrored' if src in (c1_flip, c2_flip) else 'original'} "
          f"angle={angle}°")

# Label
try:
    from PIL import ImageFont
    font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
except:
    font_big = font_sm = None

draw = ImageDraw.Draw(pkg)
ly = pkg_h - 50
draw.text((tray_margin + 5, ly), "HEN TIÁN", fill=(120, 140, 125, 255), font=font_sm)
draw.text((pkg_w // 2, ly - 2), "CLASSIC COOKIE", fill=(220, 215, 205, 255), font=font_big, anchor="mt")
draw.text((pkg_w - tray_margin - 5, ly), "Isi 4 pcs", fill=(120, 140, 125, 255), font=font_sm, anchor="rt")

final = pkg.convert('RGB')
final.save('assets/classic-cookie-mockup.png', 'PNG', optimize=True)
final.save('assets/classic-cookie-mockup.webp', 'WEBP', quality=88)
print(f"\nSaved: classic-cookie-mockup ({pkg_w}x{pkg_h})")
