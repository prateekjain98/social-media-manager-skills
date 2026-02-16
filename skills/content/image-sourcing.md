# Image Sourcing for X/Twitter Posts

## Overview
This guide provides command-line methods for sourcing relevant images for X/Twitter posts via browser automation. All methods work without GUI interaction and can be integrated into automated posting workflows.

## Prerequisites
- `curl` and `jq` (installed)
- `sips` (built-in macOS tool)
- `agent-browser` with CDP on port 9222
- Python 3 available (for optional Pillow-based text overlays)

---

## Method 1: Free Stock Images via API

### A. Unsplash API (RECOMMENDED)

**Setup:**
1. Sign up at https://unsplash.com/join
2. Create app at https://unsplash.com/developers
3. Get API key (Client-ID)
4. Store key: `export UNSPLASH_API_KEY="your_key_here"`

**Search & Download:**
```bash
# Search for images by keyword
curl -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
  "https://api.unsplash.com/search/photos?query=artificial+intelligence&per_page=5" | jq .

# Get random image by topic
curl -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
  "https://api.unsplash.com/photos/random?query=technology" | jq .

# Download image (extract URL from API response)
IMAGE_URL=$(curl -s -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
  "https://api.unsplash.com/photos/random?query=startup" | jq -r '.urls.regular')

curl -L "$IMAGE_URL" -o /tmp/post_image.jpg

# Trigger download endpoint (REQUIRED by Unsplash API terms)
DOWNLOAD_ENDPOINT=$(curl -s -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
  "https://api.unsplash.com/photos/random?query=startup" | jq -r '.links.download_location')

curl -H "Authorization: Client-ID $UNSPLASH_API_KEY" "$DOWNLOAD_ENDPOINT"
```

**Rate Limits:**
- Free tier: 50 requests/hour
- Must trigger download endpoint for each use

**Best for:**
- High-quality professional photos
- Tech/startup/office imagery
- Abstract concepts (AI, innovation, growth)

### B. Pexels API (Alternative)

**Setup:**
1. Sign up at https://www.pexels.com
2. Get API key from https://www.pexels.com/api/
3. Store key: `export PEXELS_API_KEY="your_key_here"`

**Search & Download:**
```bash
# Search for images
curl -H "Authorization: $PEXELS_API_KEY" \
  "https://api.pexels.com/v1/search?query=technology&per_page=5" | jq .

# Download image
IMAGE_URL=$(curl -s -H "Authorization: $PEXELS_API_KEY" \
  "https://api.pexels.com/v1/search?query=AI&per_page=1" | jq -r '.photos[0].src.large')

curl -L "$IMAGE_URL" -o /tmp/post_image.jpg
```

**Rate Limits:**
- Free: 200 requests/hour, 20,000/month
- Unlimited available for qualified uses

**Best for:**
- Similar to Unsplash
- Larger free rate limits

### C. Startup Stock Photos (No API, Direct Links)

**Direct Download:**
Visit https://startupstockphotos.com/ manually to browse, then:

```bash
# Download specific image (example)
curl -L "https://startupstockphotos.com/images/photo.jpg" -o /tmp/post_image.jpg
```

**Best for:**
- Tech office environments
- Startup culture imagery
- Team/collaboration shots

---

## Method 2: Extract Images from News Articles

### Extract og:image Meta Tag

```bash
# Method 1: Using grep (simple)
URL="https://techcrunch.com/some-article"
curl -s "$URL" | grep -oP '(?<=<meta property="og:image" content=")[^"]*'

# Method 2: Using xmllint (more robust, requires libxml2)
curl -s "$URL" | xmllint --html --xpath 'string(/html/head/meta[@property="og:image"]/@content)' - 2>/dev/null

# Full workflow: Extract and download
OG_IMAGE=$(curl -s "$URL" | grep -oP '(?<=<meta property="og:image" content=")[^"]*' | head -1)
curl -L "$OG_IMAGE" -o /tmp/post_image.jpg
```

**Best for:**
- News-reactive posts
- Sharing articles with context
- Tech blog commentary

**Example use case:**
```bash
# Reacting to TechCrunch article
ARTICLE_URL="https://techcrunch.com/2026/02/09/new-ai-breakthrough"
OG_IMAGE=$(curl -s "$ARTICLE_URL" | grep -oP '(?<=<meta property="og:image" content=")[^"]*' | head -1)
curl -L "$OG_IMAGE" -o /tmp/article_image.jpg

# Now post to X with this image
```

---

## Method 3: HTML + Playwright Screenshots (RECOMMENDED for LinkedIn)

> **For LinkedIn/X posts: ALWAYS use the proven templates in `skills/content/templates/linkedin/`.**
> See `skills/content/create-post.md` Phase 4 for the template picker and filling instructions.
> Do NOT generate HTML from scratch — adapt an existing template.

Browser-quality rendering with anti-aliasing, kerning, and subpixel text. Uses HTML templates + Playwright to generate PNG screenshots.

### Setup

Save this as `.context/screenshot.js`:

```javascript
const { chromium } = require('/Users/prateekjain/.nvm/versions/node/v22.14.0/lib/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const templates = [
  // LinkedIn (10)
  { file: 'templates/linkedin-01-stat-card.html', width: 1080, height: 1350 },
  { file: 'templates/linkedin-02-comparison.html', width: 1080, height: 1080 },
  { file: 'templates/linkedin-03-framework.html', width: 1080, height: 1080 },
  { file: 'templates/linkedin-04-myth-reality.html', width: 1080, height: 1350 },
  { file: 'templates/linkedin-05-quote.html', width: 1080, height: 1350 },
  { file: 'templates/linkedin-06-dashboard.html', width: 1080, height: 1080 },
  { file: 'templates/linkedin-07-listicle.html', width: 1080, height: 1350 },
  { file: 'templates/linkedin-08-before-after.html', width: 1080, height: 1350 },
  { file: 'templates/linkedin-09-checklist.html', width: 1080, height: 1080 },
  { file: 'templates/linkedin-10-bold-statement.html', width: 1080, height: 1080 },
  // Twitter (10)
  { file: 'templates/twitter-01-hot-take.html', width: 1600, height: 900 },
  { file: 'templates/twitter-02-data-chart.html', width: 1080, height: 1080 },
  { file: 'templates/twitter-03-terminal.html', width: 1600, height: 900 },
  { file: 'templates/twitter-04-thread-starter.html', width: 1600, height: 900 },
  { file: 'templates/twitter-05-single-stat.html', width: 1080, height: 1080 },
  { file: 'templates/twitter-06-quote.html', width: 1600, height: 900 },
  { file: 'templates/twitter-07-comparison.html', width: 1600, height: 900 },
  { file: 'templates/twitter-08-fake-tweet.html', width: 1200, height: 675 },
  { file: 'templates/twitter-09-tip-card.html', width: 1080, height: 1080 },
  { file: 'templates/twitter-10-kpi-dashboard.html', width: 1600, height: 900 },
  // Reddit (10)
  { file: 'templates/reddit-01-data-viz.html', width: 1080, height: 1080 },
  { file: 'templates/reddit-02-cool-guide.html', width: 1080, height: 1080 },
  { file: 'templates/reddit-03-comparison-table.html', width: 1080, height: 1080 },
  { file: 'templates/reddit-04-terminal.html', width: 1200, height: 900 },
  { file: 'templates/reddit-05-tldr.html', width: 1080, height: 1080 },
  { file: 'templates/reddit-06-flowchart.html', width: 1080, height: 1080 },
  { file: 'templates/reddit-07-myth-busting.html', width: 1080, height: 1080 },
  { file: 'templates/reddit-08-annotated-chart.html', width: 1200, height: 900 },
  { file: 'templates/reddit-09-research-summary.html', width: 1080, height: 1080 },
  { file: 'templates/reddit-10-scorecard.html', width: 1080, height: 1080 },
];

const singleFile = process.argv[2];

(async () => {
  const browser = await chromium.launch({
    args: ['--force-device-scale-factor=1']
  });
  const toProcess = singleFile
    ? [{ file: singleFile, width: 1080, height: 1080 }]
    : templates;

  for (const tmpl of toProcess) {
    const htmlPath = path.resolve(__dirname, tmpl.file);
    if (!fs.existsSync(htmlPath)) {
      console.log(`Skipping ${tmpl.file} (not found)`);
      continue;
    }

    const html = fs.readFileSync(htmlPath, 'utf8');
    const wMatch = html.match(/body\s*\{[^}]*width:\s*(\d+)px/s);
    const hMatch = html.match(/body\s*\{[^}]*height:\s*(\d+)px/s);
    const MAX_DIM = 2000; // Claude API rejects images > 2000px in multi-image requests
    const w = Math.min(wMatch ? parseInt(wMatch[1]) : tmpl.width, MAX_DIM);
    const h = Math.min(hMatch ? parseInt(hMatch[1]) : tmpl.height, MAX_DIM);

    const page = await browser.newPage({
      viewport: { width: w, height: h },
      deviceScaleFactor: 1
    });

    await page.goto('file://' + htmlPath);
    await page.waitForTimeout(800);

    const outName = singleFile
      ? 'linkedin_post_image.png'
      : tmpl.file.replace('templates/', '').replace('.html', '.png');
    const outPath = path.resolve(__dirname, singleFile ? outName : 'templates/' + outName);

    await page.screenshot({
      path: outPath,
      type: 'png',
      clip: { x: 0, y: 0, width: w, height: h }
    });

    await page.close();
    console.log(`  ${outName} (${w}x${h}px)`);
  }

  await browser.close();
  console.log('Done!');
})();
```

### CRITICAL: The MAX_DIM = 2000 Clamp

The `Math.min(..., MAX_DIM)` on lines for `w` and `h` is **mandatory**. Without it, HTML templates with body dimensions > 2000px will produce oversized PNGs that cause Claude API 400 errors:

```
INVALID_REQUEST_ERROR: AT LEAST ONE OF THE IMAGE DIMENSIONS EXCEED MAX ALLOWED SIZE FOR MANY-IMAGE REQUESTS: 2000 PIXELS
```

**Never remove this clamp. Never set body width or height > 2000px in HTML templates.**

### HTML Template Rules

When writing HTML templates for screenshots:
- Body `width` and `height` must be ≤ 2000px
- Safe sizes: `1080x1080`, `1080x1350`, `1600x900`, `1200x675`
- Use `deviceScaleFactor: 1` (not 2) to avoid doubling dimensions
- **MANDATORY: Every image MUST include the persona handle** — add a `.handle` div with `position: absolute; bottom: 24px; right: 40px; font-size: 16px; font-weight: 600; color: rgba(255,255,255,0.3);`. Use `prateekjain98` for LinkedIn, `@Prateek9jain8` for X.

---

## Method 4: Create Images with Python + Pillow

### Install Pillow

```bash
pip3 install Pillow
```

### macOS Font Paths (CRITICAL)

**Working fonts on macOS:**
- `/System/Library/Fonts/SFNS.ttf` — San Francisco (primary, use this)
- `/System/Library/Fonts/SFNSRounded.ttf` — San Francisco Rounded (softer look)

**DO NOT USE** (these don't exist or cause errors):
- `SFPro-Bold.otf` — does NOT exist
- `Helvetica.ttc` — may not work on all macOS versions

**Font helper pattern:**
```python
from PIL import ImageFont

def font(size):
    return ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)
```

### Image Standards
- **Size:** 1200x675 (16:9 ratio, optimal for X/Twitter)
- **Format:** PNG at quality=95
- **CRITICAL: Max dimension 2000px** — Both width and height must be ≤ 2000 pixels. Claude API returns 400 error for images exceeding 2000px in multi-image requests. This applies to ALL image generation methods (Pillow, HTML/Playwright screenshots, etc.)
- **Rule: Images must ADD information** — never just restate the tweet text
- **Rule: Visual variety** — never use the same template/colors for consecutive posts

### Layout Rules (CRITICAL — Common Mistakes)
- **Labels and badges must be on the SAME ROW** — place them at the same y-coordinate, not stacked
- **Bottom text boxes need 20px+ padding** from all edges — text touching box borders looks terrible
- **Always visually verify** the generated image before posting

---

### Template 1: Data Comparison Card (Dark Theme)

Two-column layout comparing metrics. Good for AI vs humans, before/after, tool comparisons.

```python
#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def font(size):
    return ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)

width, height = 1200, 675
img = Image.new('RGB', (width, height), color=(10, 15, 30))
draw = ImageDraw.Draw(img)

# Gradient accent bar at top
for x in range(width):
    r = int(59 + (147 - 59) * x / width)
    g = int(130 + (51 - 130) * x / width)
    b = int(246 + (234 - 246) * x / width)
    draw.line([(x, 0), (x, 5)], fill=(r, g, b))

# Title
draw.text((60, 28), "AI vs Engineers: The Real Scorecard", fill=(255, 255, 255), font=font(40))
draw.line([(60, 82), (1140, 82)], fill=(40, 50, 70), width=1)

# LEFT COLUMN: Items with progress bars
draw.text((60, 98), "WHERE AI WINS", fill=(34, 197, 94), font=font(18))
ai_items = [("LeetCode Hard", 94), ("Code Generation", 89), ("Algorithm Design", 91), ("Syntax Accuracy", 97)]
y = 130
for label, pct in ai_items:
    draw.text((60, y), label, fill=(180, 190, 210), font=font(24))
    bar_x, bar_y, bar_w, bar_h = 60, y + 32, 460, 18
    draw.rounded_rectangle([(bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h)], radius=5, fill=(25, 35, 55))
    fill_w = int(bar_w * pct / 100)
    draw.rounded_rectangle([(bar_x, bar_y), (bar_x + fill_w, bar_y + bar_h)], radius=5, fill=(34, 197, 94))
    draw.text((bar_x + fill_w + 10, bar_y - 2), f"{pct}%", fill=(34, 197, 94), font=font(18))
    y += 62

# RIGHT COLUMN: Items with badges ON SAME ROW as labels
draw.text((640, 98), "WHERE HUMANS WIN", fill=(249, 115, 22), font=font(18))
human_items = [
    ("Debugging prod at 2am", "Unmatched"),
    ("Understanding context", "Critical"),
    ("Stakeholder translation", "Essential"),
    ("System design tradeoffs", "Irreplaceable"),
]
y = 130
for label_text, rating in human_items:
    # Label on the left
    draw.text((640, y + 10), label_text, fill=(180, 190, 210), font=font(24))
    # Badge on the RIGHT, SAME ROW (same y-position!)
    tw = draw.textlength(rating, font=font(18))
    badge_x = 1140 - tw - 16
    draw.rounded_rectangle([(badge_x, y + 10), (badge_x + tw + 16, y + 36)], radius=6, fill=(60, 30, 10))
    draw.text((badge_x + 8, y + 12), rating, fill=(249, 155, 72), font=font(18))
    y += 62

# Bottom insight box with PROPER PADDING (20px+ from all edges)
draw.line([(60, 390), (1140, 390)], fill=(40, 50, 70), width=1)
box_top, box_bottom = 410, 540
draw.rounded_rectangle([(60, box_top), (1140, box_bottom)], radius=12, fill=(18, 25, 45))
draw.rounded_rectangle([(60, box_top), (1140, box_bottom)], radius=12, outline=(40, 55, 85), width=1)
draw.text((85, box_top + 18), "The hiring gap:", fill=(255, 255, 255), font=font(20))
draw.text((85, box_top + 50), "Companies still test for what AI does best (algorithms)", fill=(140, 150, 170), font=font(22))
draw.text((85, box_top + 80), "instead of what humans do best (chaos management)", fill=(140, 150, 170), font=font(22))

# Attribution
draw.text((60, 570), "Based on 2025-26 coding benchmark data", fill=(60, 70, 90), font=font(18))
draw.text((1010, 570), "@Prateek9jain8", fill=(80, 100, 140), font=font(18))

img.save('/tmp/data_comparison.png', quality=95)
```

---

### Template 2: Before/After Policy Card (Warm Theme)

Good for policy changes, product updates, industry shifts.

```python
#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def font(size):
    return ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)

width, height = 1200, 675
img = Image.new('RGB', (width, height), color=(255, 250, 240))  # Warm cream
draw = ImageDraw.Draw(img)

# Amber accent bar
for x in range(width):
    r, g, b = 217, 119, 6
    draw.line([(x, 0), (x, 5)], fill=(r, g, b))

# Badge
draw.rounded_rectangle([(60, 20), (250, 50)], radius=8, fill=(217, 119, 6))
draw.text((72, 24), "POLICY UPDATE", fill=(255, 255, 255), font=font(18))

# Title
draw.text((60, 65), "India Extends Startup Recognition", fill=(30, 30, 30), font=font(36))
draw.text((60, 110), "for Deep-Tech Companies", fill=(30, 30, 30), font=font(36))

# BEFORE box (red tones)
box_y = 165
draw.rounded_rectangle([(60, box_y), (570, box_y + 180)], radius=16, fill=(254, 242, 242))
# Header band INSIDE the rounded rect (not overlapping)
draw.rectangle([(60, box_y + 16), (570, box_y + 50)], fill=(220, 38, 38))
draw.text((80, box_y + 20), "BEFORE", fill=(255, 255, 255), font=font(20))
draw.text((150, box_y + 70), "10", fill=(220, 38, 38), font=font(72))
draw.text((240, box_y + 90), "years", fill=(220, 38, 38), font=font(36))
draw.text((80, box_y + 150), "Built for consumer apps", fill=(120, 60, 60), font=font(18))

# AFTER box (green tones)
draw.rounded_rectangle([(630, box_y), (1140, box_y + 180)], radius=16, fill=(240, 253, 244))
draw.rectangle([(630, box_y + 16), (1140, box_y + 50)], fill=(22, 163, 74))
draw.text((650, box_y + 20), "AFTER", fill=(255, 255, 255), font=font(20))
draw.text((720, box_y + 70), "20", fill=(22, 163, 74), font=font(72))
draw.text((810, box_y + 90), "years", fill=(22, 163, 74), font=font(36))
draw.text((650, box_y + 150), "Built for deep-tech & AI", fill=(30, 100, 50), font=font(18))

# "Why this matters" section
why_y = 380
draw.text((60, why_y), "Why this matters:", fill=(30, 30, 30), font=font(22))
points = [
    "Most AI companies still finding PMF at year 3",
    "Hardware/biotech startups take even longer",
    "Covers: AI, robotics, space tech, quantum, green hydrogen",
]
for i, pt in enumerate(points):
    draw.text((80, why_y + 35 + i * 32), f"  {pt}", fill=(80, 80, 80), font=font(20))

# Source and attribution
draw.text((60, 560), "Source: startupnews.fyi", fill=(140, 140, 140), font=font(16))
draw.text((1010, 560), "@Prateek9jain8", fill=(180, 140, 80), font=font(18))

img.save('/tmp/before_after.png', quality=95)
```

---

### Template 3: Simple Text on Solid Background

Good for quotes, stats, announcements.

```python
#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import sys

def font(size):
    return ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)

def create_text_image(text, output_path, width=1200, height=675):
    img = Image.new('RGB', (width, height), color=(10, 15, 30))
    draw = ImageDraw.Draw(img)

    # Calculate text position (centered)
    bbox = draw.textbbox((0, 0), text, font=font(80))
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(position, text, fill='white', font=font(80))
    img.save(output_path, quality=95)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 create_text_image.py 'Your text here' output.png")
        sys.exit(1)
    create_text_image(sys.argv[1], sys.argv[2])
```

---

### Template 4: Text Overlay on Photo Background

```python
#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def font(size):
    return ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)

def create_text_overlay(background_path, text, output_path):
    img = Image.open(background_path)
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 128))
    img = img.convert('RGBA')
    img = Image.alpha_composite(img, overlay)

    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text, font=font(60))
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
    draw.text(position, text, fill='white', font=font(60))

    img = img.convert('RGB')
    img.save(output_path, quality=95)
```

---

### Uploading Images to X via Clipboard Paste

```bash
# 1. Copy image to clipboard (PNG)
osascript -e 'set the clipboard to (read (POSIX file "/tmp/post_image.png") as «class PNGf»)'

# 2. For JPG images
osascript -e 'set the clipboard to (read (POSIX file "/tmp/post_image.jpg") as «class JPEGf»)'

# 3. Click the compose textbox in browser
agent-browser --cdp 9222 click @REF

# 4. Paste image
agent-browser --cdp 9222 press Meta+v
```

---

## Method 5: macOS Native Image Processing (sips)

**sips** is built into macOS - no installation needed.

### Convert & Resize Images

```bash
# Convert JPG to PNG
sips -s format png input.jpg --out output.png

# Resize to Twitter's optimal size (1200x675)
sips -Z 1200 input.jpg --out resized.jpg

# Crop to specific dimensions
sips -c 675 1200 input.jpg --out cropped.jpg

# Rotate image
sips -r 90 input.jpg --out rotated.jpg
```

### Batch Process Images

```bash
# Convert all PNG to JPG
for i in *.png; do
  sips -s format jpeg -s formatOptions 70 "${i}" --out "${i%png}jpg"
done

# Resize all images to Twitter size
for i in *.jpg; do
  sips -Z 1200 "$i" --out "resized_${i}"
done
```

**Best for:**
- Format conversion
- Batch resizing
- Quick image adjustments
- No external dependencies needed

---

## Recommended Workflow by Post Type

### 1. News-Reactive Posts
**Best image source:** Article's og:image

```bash
# Extract and use article's featured image
ARTICLE_URL="https://techcrunch.com/article"
OG_IMAGE=$(curl -s "$ARTICLE_URL" | grep -oP '(?<=<meta property="og:image" content=")[^"]*' | head -1)
curl -L "$OG_IMAGE" -o /tmp/post_image.jpg
```

**Why:** Adds visual context, looks professional, credits source implicitly

### 2. Opinion/Hot Take Posts
**Best image source:** Stock photo or simple text graphic

```bash
# Option A: Relevant stock image
IMAGE_URL=$(curl -s -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
  "https://api.unsplash.com/photos/random?query=debate" | jq -r '.urls.regular')
curl -L "$IMAGE_URL" -o /tmp/post_image.jpg

# Option B: Bold text statement
./create_text_image.py "Hot take: AI agents will\nreplace 80% of SaaS tools" /tmp/post_image.png
```

**Why:** Text graphics get attention, stock images add professionalism

### 3. Career/Personal Posts
**Best image source:** Relevant stock photo (office, team, growth themes)

```bash
# Office/startup imagery
IMAGE_URL=$(curl -s -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
  "https://api.unsplash.com/photos/random?query=startup+office" | jq -r '.urls.regular')
curl -L "$IMAGE_URL" -o /tmp/post_image.jpg
```

**Why:** Humanizes content, adds relatability

### 4. Educational/Tutorial Posts
**Best image source:** Screenshot or diagram (manual), or text summary graphic

```bash
# Create summary graphic
./create_text_image.py "3 lessons from\nbuilding AI agents\n\n1. Ship fast\n2. Iterate\n3. Listen" /tmp/post_image.png
```

**Why:** Text graphics work as visual summaries, drive engagement

### 5. Humor/Meme Posts
**Best image source:** Meme templates or quirky stock photos

```bash
# Find unexpected/quirky images
IMAGE_URL=$(curl -s -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
  "https://api.unsplash.com/photos/random?query=surprised+face" | jq -r '.urls.regular')
curl -L "$IMAGE_URL" -o /tmp/post_image.jpg
```

**Why:** Visual humor increases shareability

---

## Complete Automation Example

```bash
#!/bin/bash
# auto_image_for_post.sh - Get relevant image based on post type

POST_TYPE=$1  # news, opinion, career, educational, humor
KEYWORD=$2    # search term

UNSPLASH_API_KEY="your_key_here"

case $POST_TYPE in
  news)
    # Use article's og:image (requires article URL)
    ARTICLE_URL=$KEYWORD
    OG_IMAGE=$(curl -s "$ARTICLE_URL" | grep -oP '(?<=<meta property="og:image" content=")[^"]*' | head -1)
    curl -L "$OG_IMAGE" -o /tmp/post_image.jpg
    ;;

  opinion|career)
    # Stock photo
    IMAGE_URL=$(curl -s -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
      "https://api.unsplash.com/photos/random?query=$KEYWORD" | jq -r '.urls.regular')
    curl -L "$IMAGE_URL" -o /tmp/post_image.jpg
    ;;

  educational)
    # Text graphic (requires text as KEYWORD)
    python3 create_text_image.py "$KEYWORD" /tmp/post_image.png
    ;;

  humor)
    # Quirky stock photo
    IMAGE_URL=$(curl -s -H "Authorization: Client-ID $UNSPLASH_API_KEY" \
      "https://api.unsplash.com/photos/random?query=funny+$KEYWORD" | jq -r '.urls.regular')
    curl -L "$IMAGE_URL" -o /tmp/post_image.jpg
    ;;
esac

echo "Image saved to /tmp/post_image.{jpg,png}"
```

**Usage:**
```bash
# Get image for news post
./auto_image_for_post.sh news "https://techcrunch.com/article"

# Get image for opinion post
./auto_image_for_post.sh opinion "artificial intelligence"

# Create text graphic for educational post
./auto_image_for_post.sh educational "Ship fast, iterate faster"
```

---

## Best Practices

1. **Image Dimensions:**
   - **HARD LIMIT: 2000px max per side** — Claude API rejects images > 2000px in multi-image requests (400 error). Never generate images exceeding this.
   - Optimal for X: 1200x675 (16:9 ratio)
   - Optimal for LinkedIn: 1080x1080 or 1080x1350
   - Minimum: 600x335
   - Safe sizes: 1080x1080, 1080x1350, 1600x900, 1200x675

2. **File Size:**
   - Keep under 5MB for fast uploads
   - Use JPG for photos, PNG for graphics with text

3. **Relevance > Quality:**
   - A relevant stock photo beats a beautiful but irrelevant one
   - og:image from article is ALWAYS relevant for news posts

4. **Text Overlays:**
   - Keep text SHORT (5-10 words max)
   - Use high contrast (white on dark, dark on light)
   - Avoid small fonts - must be readable on mobile

5. **Copyright Compliance:**
   - Unsplash/Pexels: Free for commercial use, attribution appreciated but not required
   - og:image from articles: Fair use for commentary/sharing
   - Always trigger Unsplash download endpoint per API terms

---

## Integration with Posting Workflow

```bash
# 1. Get image based on post content
./auto_image_for_post.sh opinion "startup growth"

# 2. Copy to clipboard
osascript -e 'set the clipboard to (read (POSIX file "/tmp/post_image.jpg") as «class JPEGf»)'

# 3. Open X compose (via agent-browser)
agent-browser --cdp 9222 open "https://x.com/compose/post"

# 4. Click textbox
agent-browser --cdp 9222 snapshot -i | jq '.interactive[] | select(.role == "textbox")'
agent-browser --cdp 9222 click @123  # Use actual ref from snapshot

# 5. Paste image
agent-browser --cdp 9222 press Meta+v

# 6. Type post text
agent-browser --cdp 9222 fill @123 "Your tweet text here"

# 7. Post
agent-browser --cdp 9222 snapshot -i | jq '.interactive[] | select(.text == "Post")'
agent-browser --cdp 9222 click @456
```

---

## Sources

- [Unsplash API Documentation](https://unsplash.com/documentation)
- [Pexels API](https://www.pexels.com/api/)
- [Startup Stock Photos](https://startupstockphotos.com/)
- [Free Stock Images for Social Media (SocialBee)](https://socialbee.com/blog/free-images-for-social-media/)
- [Best Free Stock Image Libraries for Startups (TechRound)](https://techround.co.uk/startups/best-free-stock-image-libraries-for-startups/)
- [Python Pillow - Writing Text on Images (TutorialsPoint)](https://www.tutorialspoint.com/python_pillow/python_pillow_writing_text_on_image.htm)
- [Adding Text on Image using Python - PIL (GeeksforGeeks)](https://www.geeksforgeeks.org/python/adding-text-on-image-using-python-pil/)
- [sips - Scriptable Image Processing System (SS64)](https://ss64.com/mac/sips.html)
- [Convert Images for Web Using sips (Medium)](https://medium.com/shell-life/convert-images-for-web-using-the-sips-command-line-on-macosx-656c502a67a6)
