# LinkedIn Image Templates

10 templates based on actual viral LinkedIn posts, researched via Safari browser in Feb 2026.

## Templates

### 01 — Leadership Quote
- **File:** `01-leadership-quote.html` / `.png`
- **Inspired by:** Leslie Lockhart, Ed.D — "Leadership doesn't start at the top of the org chart"
- **Engagement:** 2,212 reactions · 61 comments · 451 reposts
- **Why it went viral:** Universal truth about leadership being a behavior, not a title. Resonates with both managers and individual contributors. Short, quotable format encourages resharing.
- **Template style:** Quote card with 3 insight points

### 02 — Work Sustainability Data
- **File:** `02-work-sustainability.html` / `.png`
- **Inspired by:** Vinu Varghese (GPHR, SHRM-SCP) — "Rigid work designs are failing high-skill employees"
- **Engagement:** 1,828 reactions · 36 comments · 20 reposts
- **Why it went viral:** Backed by cognitive psychology research. Challenges the default 9-to-5 model with data. Appeals to both employees wanting flexibility and HR leaders seeking retention strategies.
- **Template style:** 4-stat grid with takeaway bar

### 03 — Office vs Remote Work
- **File:** `03-office-vs-remote.html` / `.png`
- **Inspired by:** LYKAJIGARI SIDDHARTHA — "Office Work vs Remote Work — Same Job, Two Very Different Lives"
- **Post link:** https://www.linkedin.com/feed/update/urn:li:activity:7425004405059563522/
- **Engagement:** 1,527 reactions · 63 comments · 73 reposts
- **Why it went viral:** Side-by-side comparison format is instantly scannable. Emotional contrast (cold lunchbox vs warm meals, missed dinners vs family time) triggers strong reactions. Relatable to anyone who's worked both modes.
- **Template style:** 8-row comparison with takeaway

### 04 — ChatGPT App Distribution
- **File:** `04-chatgpt-distribution.html` / `.png`
- **Inspired by:** Lenny Rachitsky — "You can build a ChatGPT app in 30 minutes that reaches 800 million users"
- **Post link:** https://www.linkedin.com/feed/update/urn:li:activity:7419429429040455680/
- **Engagement:** 637 reactions · 100 comments · 27 reposts
- **Why it went viral:** Actionable opportunity with specific numbers (800M users, 30 minutes). Compares to historical distribution moments (App Store 2008, SEO 2003). Creates urgency — early mover advantage.
- **Template style:** Hero stat + timeline + 4-step how-to grid

### 05 — India Salary Guide
- **File:** `05-salary-guide.html` / `.png`
- **Inspired by:** Shiv Shivakumar — "India Salary Guide 2026 — Michael Page Report"
- **Post link:** https://www.linkedin.com/feed/update/urn:li:activity:7425757730960863232/
- **Engagement:** 577 reactions · 22 comments · 44 reposts
- **Why it went viral:** Salary data is always high-interest on LinkedIn. Covers 14 sectors with specific ranges. Shared by a respected industry leader (Operating Partner at Advent International), lending credibility.
- **Template style:** 8-sector salary grid with 3 insight stats

### 06 — Secret AI Websites
- **File:** `06-secret-websites.html` / `.png`
- **Inspired by:** Swapnil Tighare — "10 Secret websites that feel like they are illegal!"
- **Engagement:** 390 reactions · 60 comments · 27 reposts
- **Why it went viral:** Clickbait-style title ("feel illegal") creates curiosity. Numbered list format is easy to scan. AI tools are high-interest topic. Each tool solves a specific pain point.
- **Template style:** 10-item list with category badges

### 07 — Resignation Red Flags
- **File:** `07-resignation-redflags.html` / `.png`
- **Inspired by:** Ager Fredrick — "Resigning Before Getting Another Job Offer"
- **Post link:** https://www.linkedin.com/feed/update/urn:li:activity:7419155708673163264/
- **Engagement:** 384 reactions · 32 comments · 89 reposts
- **Why it went viral:** Flips the narrative — resignation without a backup isn't about the employee, it's a message about the company. 6 specific red flags give managers a framework to self-assess. High repost count (89) shows strong reshare behavior.
- **Template style:** 6-item numbered list with descriptions + takeaway

### 08 — Resume Email Templates
- **File:** `08-resume-email.html` / `.png`
- **Inspired by:** Gowducheruvu Jaswanth Reddy — "How you email your resume matters more than you think"
- **Engagement:** 359 reactions · 28 comments · 23 reposts
- **Why it went viral:** Actionable templates people can save and use immediately. Addresses a common blind spot — most job seekers focus on the resume but neglect the email. 5 ready-to-use templates cover the full application cycle.
- **Template style:** 5-card email template list with subject lines + pro tip

### 09 — Interview Mistakes
- **File:** `09-interview-mistakes.html` / `.png`
- **Inspired by:** Kotha NandaKumari — "10 Things You Should Never Say in a Job Interview"
- **Engagement:** 346 reactions · 25 comments · 12 reposts
- **Why it went viral:** "Never say" format creates urgency and FOMO. Each mistake is specific and relatable. PDF carousel format (12 pages) drives saves and shares. Universal relevance across industries.
- **Template style:** 2-column grid of 10 mistakes with reasons + pro tip

### 10 — AI Tool Cheat Sheet
- **File:** `10-ai-cheatsheet.html` / `.png`
- **Inspired by:** Jonathan Parsons — "The Ultimate AI Tool Cheat Sheet — 50+ tools organized by actual use case"
- **Engagement:** 283 reactions · 78 comments · 34 reposts
- **Why it went viral:** Solves tool overwhelm — organizes 50+ tools by use case instead of hype. High comment count (78) suggests strong engagement and discussion. "Bookmark this" CTA drives saves.
- **Template style:** 8-category grid with 3 tools each + CTA bar

## Usage

Each template is an HTML file (1080x1080px) that can be screenshotted using Playwright:

```bash
cd .context
node screenshot.js templates/<filename>.html
```

The generated PNG is saved as `linkedin_post_image.png` in the `.context` directory.

## Viral Patterns Observed

1. **Data-backed claims** outperform opinion-only posts (templates 02, 05)
2. **Numbered lists** (10 things, 5 templates) drive saves and shares (06, 08, 09)
3. **Comparison formats** are instantly scannable and shareable (03)
4. **"Secret" / "Illegal"** clickbait in titles drives curiosity clicks (06)
5. **Salary/compensation data** is always high-interest on LinkedIn (05)
6. **Flipped narratives** ("it's not about the employee, it's about the company") create debate (07)
7. **Actionable templates** people can use immediately get saved and reshared (08, 10)
8. **Leadership quotes** with universal truths get mass reshared (01)
