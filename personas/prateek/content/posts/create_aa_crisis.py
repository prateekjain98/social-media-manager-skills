#!/usr/bin/env python3
"""
American Airlines Crisis — Bold typographic poster style.
NOT a dark tech infographic. Vivid gradient background, big hero number.
2x supersampling + LANCZOS.
"""
from PIL import Image, ImageDraw, ImageFont
import math

HEADING = "/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf"
BODY = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
BODY_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

S = 2
FW, FH = 1200, 675
W, H = FW * S, FH * S

# ── GRADIENT BACKGROUND ──
# Deep navy to warm crimson — crisis feel
img = Image.new('RGB', (W, H))
pixels = img.load()
c1 = (15, 23, 42)     # deep navy (top-left)
c2 = (127, 29, 29)    # warm crimson (bottom-right)

for y in range(H):
    for x in range(W):
        # Diagonal gradient
        ratio = (x / W * 0.4 + y / H * 0.6)
        r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
        g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
        b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
        pixels[x, y] = (r, g, b)

draw = ImageDraw.Draw(img)

def fh(px): return ImageFont.truetype(HEADING, px * S)
def fb(px): return ImageFont.truetype(BODY, px * S)
def fr(px): return ImageFont.truetype(BODY_REG, px * S)
def s(v): return v * S

# Colors on gradient
WHITE = (255, 255, 255)
LIGHT = (230, 230, 235)
DIM   = (180, 180, 195)
ACCENT = (255, 107, 107)  # soft red accent

L = s(80)
R = W - s(80)

# ── HERO NUMBER ──
hero_font = fh(160)
hero_y = s(56)
draw.text((L, hero_y), "28,000", fill=WHITE, font=hero_font)

# ── MAIN STATEMENT ──
stmt_y = hero_y + s(168)
draw.text((L, stmt_y), "flight attendants voted", fill=LIGHT, font=fb(32))
draw.text((L, stmt_y + s(44)), "NO CONFIDENCE", fill=ACCENT, font=fh(48))
draw.text((L, stmt_y + s(100)), "in their CEO.", fill=LIGHT, font=fb(32))

# ── THIN DIVIDER ──
div_y = stmt_y + s(152)
draw.line([(L, div_y), (L + s(120), div_y)], fill=ACCENT, width=s(3))

# ── THE TAKE ──
take_y = div_y + s(24)
draw.text((L, take_y), "Every complaint was an operations problem.", fill=WHITE, font=fb(22))
draw.text((L, take_y + s(36)), "AI agents can solve all of them today.", fill=DIM, font=fr(20))

# ── HANDLE (bottom right) ──
handle_font = fr(16)
hw = draw.textlength("@Prateek9jain8", font=handle_font)
draw.text((R - hw, H - s(48)), "@Prateek9jain8", fill=DIM, font=handle_font)

# ── DOWNSCALE ──
img = img.resize((FW, FH), Image.LANCZOS)
img.save(
    '/Users/prateekjain/conductor/workspaces/social-media-manager-skills/madison/personas/prateek/content/posts/aa_automation_crisis.png',
    format="PNG", optimize=True, dpi=(144, 144),
)
print("Saved!")
