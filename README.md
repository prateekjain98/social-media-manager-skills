# Social Media Manager

A multi-persona social media growth system with 30 reusable Claude skills, research-backed growth algorithms, and stealth browser automation. Run multiple client accounts in parallel.

---

## Prerequisites

### Required
- [Claude Code](https://claude.ai/claude-code) (or any AI agent that runs shell commands)
- Node.js 18+ (`node --version`)

### Browser Automation (CloakBrowser + agent-browser)

```bash
# One-command setup
bash setup.sh

# Or manually:
npm install -g agent-browser cloakbrowser playwright-core
```

CloakBrowser is a stealth Chromium binary with 25 C++ level anti-detection patches (canvas, WebGL, AudioContext, navigator properties). It's the only browser used for automation in this repo — passes Cloudflare Turnstile, FingerprintJS, BrowserScan 30/30, reCAPTCHA v3 (0.9 score).

See `skills/automation/agent-browser.md` for full setup and multi-client parallel automation.

### Image Generation (optional)
- Python 3.9+ with Pillow: `pip install Pillow`

---

## Quick Start: Create Your Persona

```bash
# 0. Install tools (first time only)
bash setup.sh

# 1. Copy the template
cp -r personas/_template personas/yourname

# 2. Fill in your persona files (start with _persona.md)
# Edit personas/yourname/strategy/_persona.md
# Edit personas/yourname/strategy/_growth-algorithm.md
# Edit personas/yourname/strategy/_news-and-tools.md

# 3. Set up credentials
cp .credentials.example.md .credentials.md
# Edit .credentials.md with your accounts — NEVER commit this file

# 4. Launch browser for your persona
bash launch-browsers.sh yourname

# 5. Start engaging using the growth agent
# Reference your persona: personas/yourname/strategy/
```

See `personas/_template/README.md` for detailed setup instructions.

---

## Repo Structure

```
├── personas/                  ← Each person gets their own folder
│   ├── _template/             ← Copy this to create a new persona
│   │   ├── strategy/          ← Persona template files
│   │   ├── content/           ← Empty (fills over time)
│   │   └── metrics.md         ← Empty tracking template
│   └── prateek/               ← Example: filled-in persona
│       ├── strategy/active/   ← Active strategy files
│       ├── strategy/archive/  ← Old strategy versions
│       ├── content/           ← Posts, analyses, samples
│       └── metrics.md         ← Engagement tracking
├── skills/                    ← 30 reusable skills (shared by all personas)
│   ├── platforms/             ← X, LinkedIn, Reddit, Instagram, TikTok, etc.
│   ├── content/               ← Captions, hooks, threads, video scripts
│   ├── analysis/              ← Strategy audit, competitor analysis, KPIs
│   ├── engagement/            ← Responses, crisis, community guidelines
│   └── automation/            ← Agent browser, growth agent
├── strategy/                  ← Shared strategy (applies to all personas)
│   └── _core-principles.md   ← Anti-AI detection rules
├── .credentials.example.md   ← Credentials template
├── setup.sh                  ← One-command install (agent-browser + CloakBrowser)
├── launch-browsers.sh        ← Launch CloakBrowser per persona
└── .gitignore
```

### What's Shared vs Per-Persona

| Shared (all personas) | Per-Persona |
|-----------------------|-------------|
| `skills/` — 30 reusable skills | `personas/[name]/strategy/` — Identity, algorithm, targets |
| `strategy/_core-principles.md` — Anti-AI rules | `personas/[name]/content/` — Posts, analyses |
| `skills/automation/agent-browser.md` — Browser setup | `personas/[name]/metrics.md` — Engagement log |
| `.credentials.example.md` — Creds template | |

---

## Core Principles

**Read `strategy/_core-principles.md` before using any skill.**

- All content must be **undetectable as AI-generated**
- Sound like a real person with opinions, quirks, imperfections
- Match the culture of each platform
- Never reveal AI identity

---

## Skills (30 Total)

### Content Creation (7)
`/caption` `/hooks` `/carousel` `/thread` `/video-script` `/ad-copy` `/image-sourcing`

### Strategy & Analysis (10)
`/content-pillars` `/content-calendar` `/competitor-analysis` `/trend-analysis` `/strategy-audit` `/kpi-framework` `/social-report` `/hashtag-strategy` `/brand-voice` `/bio-optimizer`

### Engagement (5)
`/response` `/community-guidelines` `/crisis-response` `/influencer-brief` `/repurpose`

### Platform-Specific (7)
`/x` `/linkedin` `/reddit` `/instagram` `/tiktok` `/youtube-shorts` `/threads`

### Automation (2)
`/agent-browser` `/growth-agent`

See `skills/README.md` for full details on each skill.

---

## Credentials Setup

```bash
cp .credentials.example.md .credentials.md
# Edit with your accounts — NEVER commit this file
```

See `skills/automation/agent-browser.md` for browser automation setup (CloakBrowser + agent-browser).
