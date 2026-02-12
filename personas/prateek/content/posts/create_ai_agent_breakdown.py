#!/usr/bin/env python3
"""
AI Agent Time Breakdown — horizontal bar chart infographic.
All spacing multiples of 8. 2x supersampling + LANCZOS. WCAG AA.
"""
from PIL import Image, ImageDraw, ImageFont

HEADING = "/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf"
BODY = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

S = 2
FW, FH = 1200, 675
W, H = FW * S, FH * S
img = Image.new('RGB', (W, H), (13, 17, 23))
draw = ImageDraw.Draw(img)

def fh(px): return ImageFont.truetype(HEADING, px * S)
def fb(px): return ImageFont.truetype(BODY, px * S)
def s(v): return v * S

# Colors (GitHub Dark, WCAG AA)
TXT1 = (240, 246, 252)   # primary text
TXT2 = (201, 209, 217)   # secondary text
TXT3 = (139, 148, 158)   # tertiary text
RED  = (248, 81, 73)     # infrastructure accent
GRN  = (63, 185, 80)     # model accent
BRD  = (48, 54, 61)      # dividers
BAR_TRACK = (30, 37, 46) # bar background track

# Data — descending by effort
data = [
    ("Error handling & retries", 25, RED),
    ("API integrations & OAuth", 22, RED),
    ("Edge cases & validation", 18, RED),
    ("Monitoring & debugging", 15, RED),
    ("Prompt engineering", 10, GRN),
]

L = s(64)          # left margin
R = W - s(64)      # right edge
CW = R - L         # content width

# ── TITLE ──
T = s(40)
draw.text((L, T), "Building AI Agents", fill=TXT1, font=fh(32))
draw.text((L, T + s(40)), "Where the time actually goes", fill=TXT3, font=fb(16))
hf = fb(16)
hw = draw.textlength("@Prateek9jain8", font=hf)
draw.text((R - hw, T + s(8)), "@Prateek9jain8", fill=TXT3, font=hf)
title_div = T + s(64)
draw.line([(L, title_div), (R, title_div)], fill=BRD, width=s(1))

# ── BOTTOM TAKEAWAY ──
B = H - s(40)
bot_div = B - s(56)
draw.line([(L, bot_div), (R, bot_div)], fill=BRD, width=s(1))
draw.text((L, bot_div + s(16)), "The model is the easy part.", fill=TXT1, font=fh(20))
draw.text((L, bot_div + s(40)), "Everything around it is where you win or lose.", fill=TXT3, font=fb(16))

# ── CONTENT ZONE ──
zone_top = title_div + s(24)
zone_bot = bot_div - s(24)

# Row layout (all 1x values, multiples of 8):
#   text line at y (22px font for pct, 16px for label)
#   bar at y + 32 (32px gap from text top to bar top)
#   bar height: 16px
#   row content: 48px
#   stride: 64px (48 content + 16 gap)
STRIDE = 64
ROW_CONTENT = 48
ROWS = len(data)
total_h = (ROWS - 1) * STRIDE + ROW_CONTENT  # 4*64 + 48 = 304

# Vertical centering
zone_h_1x = (zone_bot - zone_top) // S  # 427
offset = ((zone_h_1x - total_h) // 2 // 8) * 8  # round to 8 = 64
content_y = zone_top + s(offset)

# Bar scale: 25% fills 75% of content width
BAR_MAX = int(CW * 0.75)
MAX_PCT = 25

for i, (label, pct, color) in enumerate(data):
    y = content_y + i * s(STRIDE)

    # Percentage number (left, bold, colored)
    pct_font = fh(22)
    pct_str = f"{pct}%"
    draw.text((L, y), pct_str, fill=color, font=pct_font)

    # Category label (after percentage, white)
    label_x = L + s(56)
    draw.text((label_x, y), label, fill=TXT2, font=fb(16))

    # Bar track (full width, dim)
    bar_y = y + s(32)
    bh = s(16)
    r = s(8)
    draw.rounded_rectangle(
        [(L, bar_y), (L + BAR_MAX, bar_y + bh)],
        radius=r, fill=BAR_TRACK,
    )

    # Bar fill (proportional)
    bw = int(BAR_MAX * pct / MAX_PCT)
    draw.rounded_rectangle(
        [(L, bar_y), (L + bw, bar_y + bh)],
        radius=r, fill=color,
    )

# ── DOWNSCALE ──
img = img.resize((FW, FH), Image.LANCZOS)
img.save(
    '/Users/prateekjain/conductor/workspaces/social-media-manager-skills/madison/personas/prateek/content/posts/ai_agent_breakdown.png',
    format="PNG", optimize=True, dpi=(144, 144),
)
print("Saved!")
