# Social Media Manager

A multi-persona social media growth system with 30 reusable Claude skills, research-backed growth algorithms, and browser automation.

---

## Quick Start: Create Your Persona

```bash
# 1. Copy the template
cp -r personas/_template personas/yourname

# 2. Fill in your persona files (start with _persona.md)
# Edit personas/yourname/strategy/_persona.md
# Edit personas/yourname/strategy/_growth-algorithm.md
# Edit personas/yourname/strategy/_news-and-tools.md

# 3. Set up credentials
cp .credentials.example.md .credentials.md
# Edit .credentials.md with your accounts — NEVER commit this file

# 4. Start engaging using the growth agent
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

See `skills/automation/agent-browser.md` for browser automation setup (Chrome DevTools Protocol).
