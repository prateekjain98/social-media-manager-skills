# Create Post

Generate a complete social media post with image for LinkedIn and/or X.

## Skill: `/create-post`

**This is the primary skill for creating persona-specific content. Use this instead of `/caption` or `/hooks`.**

---

## Phase 1: Topic & Angle

### Input
Accept one of:
- A specific topic from the user
- A trending post/article to react to
- "Create a viral post" (requires trend discovery first)

### If no topic given — Discover trending content
1. Browse LinkedIn feed via Safari/Chrome to find posts with high engagement (500+ reactions)
2. Check Hacker News, TechMeme, or X trending for AI/tech news
3. Look for posts from target accounts: @karpathy, @sama, @lennysan, @levelsio, @GregIsenberg
4. Pick something Prateek can add a unique angle to from real production experience

### Determine post type
| Type | When to use | Example |
|------|------------|---------|
| Builder Story | You built/broke/shipped something | "Our AI agent emailed the same lead 47 times" |
| Hot Take | Strong opinion backed by experience | "90% of our codebase is SaaS plumbing" |
| Data Drop | You have specific numbers | "Cost breakdown: model API 23%, infra 31%..." |
| News Reaction | Trending AI/tech news within 4 hours | "Lenny just shared numbers from OpenAI..." |
| Humor | Relatable engineering observation | "Most satisfying: AI logic. Actual job: HubSpot webhooks" |
| Ultra-short | One punchy observation | "200 lines of code. 180 are error handling. This is the job." |

### Determine format
- Mini-essay (300-600 chars) — max 4/week
- Ultra-short (under 200 chars) — at least 2/week
- Data/numbers drop — at least 1/week
- Humor-first — at least 1/week

**Rule: Must differ from last 2 posts in format.**

---

## Phase 2: Write the Post

### Voice — The Single Test

Read your draft out loud. Does it sound like you're texting a smart friend about work?

If it sounds like a LinkedIn thought leader on stage, rewrite it.

### Gold Standard Examples

**Builder Story:**
```
Our AI agent emailed the same lead 47 times in one night.

Race condition in the task queue. Two workers grabbed the same job. Both completed it. Both triggered retries.

The fix? One line — an idempotency key. Twenty minutes of work.

AI doesn't just run your bugs. It amplifies them. A normal bug creates a bad database entry. An agent bug spams your entire lead list while you sleep.

I still think about that lead sometimes.

#AIEngineering #StartupLife #ProductionBugs
```

**Ultra-short:**
```
Shipped a feature last week. 200 lines of code.

180 of them are error handling.

This is the job.

#Engineering #AIAgents
```

**Hot Take:**
```
90% of our codebase at SalesMonk is the same stuff every SaaS company builds.

Auth. Billing. CRM integrations. RBAC. Webhooks. Rate limiting.

The AI part — the model calls, the agent logic — is maybe 10% of the code.

Nobody talks about this because "I spent 3 weeks on OAuth" doesn't get likes. But it's the actual job. The AI is the easy part.

#AIStartup #SaaS #StartupReality
```

**Humor:**
```
Most satisfying part of my job: building the AI agent logic.

Actual majority of my job: figuring out why a webhook from HubSpot stopped firing on Tuesdays specifically.

#Engineering #SaaS #StartupLife
```

**News Reaction:**
```
Lenny just shared numbers from OpenAI's engineering team. 95% of their engineers use Codex. They run 10-20 coding agents in parallel. PR reviews dropped from 15 minutes to 3.

I've been running parallel Claude agents at SalesMonk for months now. The productivity jump is real. Stuff that took me a month ships in a week.

The weird part isn't the speed. It's how fast you stop noticing. You adjust in days and then the old way of working just feels broken.

Most engineers I talk to still aren't using AI for actual production code. Not side projects. Not demos. Real work. That gap is going to matter a lot very soon.

#AI #Engineering #Coding #StartupLife #OpenAI
```

**Career/Personal:**
```
I went from CTO to "founding engineer."

Everyone assumed it was a step down.

At EvolvFit I ran everything — product, fundraising, hiring, ops. I was CTO because there was nobody else. But the best code I wrote was always when I wasn't also worrying about payroll.

So I picked a role where I build 100% of the time.

Titles are just words. The actual question is: are you doing work that makes you better, or work that just looks good on LinkedIn?

#CareerGrowth #StartupLife #FounderLife
```

### DO vs DON'T

| DON'T write this | DO write this |
|---|---|
| "In the rapidly evolving landscape of AI..." | "We switched our LLM 3 times this year." |
| "Here are 5 key takeaways from my experience:" | "5 things nobody tells you about shipping AI agents:" |
| "It's crucial to prioritize error handling" | "180 of 200 lines are error handling. This is the job." |
| "I'm excited to share my insights on..." | [Just start with the insight. No preamble.] |
| "What do you think? Let me know in the comments!" | "What's the hardest 'no' you've had to give on a product decision?" |
| Arrow bullet points (→ Point 1 → Point 2) | Short paragraphs. Varied rhythm. Sentence fragments. |
| "Remember: the journey starts with a single step" | End with a punchline, question, or trailing thought |
| "As a founder, I've learned that..." | "I spent 6 months building the wrong thing. Here's how I knew." |
| "This is a game-changer for the industry" | "This changes how I think about [specific thing]" |
| Perfect parallel structure in every list | Messy, real, varied. Like actual speech. |

### Banned Phrases (instant rewrite if any appear)

- "game-changer", "cutting-edge", "leverage", "synergy", "robust", "seamless"
- "excited to share", "thrilled to announce", "in today's world", "in this era"
- "let's dive in", "without further ado", "it's important to note"
- "unlock your potential", "take it to the next level", "empower"
- Any motivational closer ("Remember, the journey is...", "You just need to start")
- Any sentence starting with "As a founder..." or "As an engineer..."
- "At the end of the day...", "The bottom line is..."
- "Needless to say", "It goes without saying"

### Structural Rules

1. **First 2 lines = everything.** This is all that shows before "see more." Make them specific and surprising.
2. **One idea per line.** Never write a wall of text.
3. **Max 3 sentences per paragraph.** Anything longer gets skipped.
4. **White space is your friend.** Blank lines between every 1-2 sentences.
5. **300-600 characters** for most posts. Earn the right to go longer.
6. **"I" not "we"** — you're a person, not a company blog.
7. **Specific > generic.** "We spent 3 weeks on error recovery" beats "Error handling is important."
8. **3-5 hashtags at end.** Not inline.
9. **Vary endings:** ~50% question, ~25% strong statement, ~25% punchline/trailing thought.

### Self-Check Before Moving On

- [ ] First 2 lines pass the "would I click see more?" test
- [ ] Grounded in specific experience or number (not generic opinion)
- [ ] No banned phrases anywhere
- [ ] Doesn't sound like ChatGPT wrote it (read it out loud)
- [ ] Different format from last 2 posts
- [ ] Under 1500 characters (ideally 300-600)
- [ ] Would I actually want to read this if someone else posted it?

---

## Phase 3: Choose Image Strategy

### Does this post need an image?

| Post type | Image? | Why |
|-----------|--------|-----|
| Data/numbers | YES | Stat card or data viz amplifies the numbers |
| News reaction with stats | YES | Visualize the key data point |
| Builder story | MAYBE | Only if there's a stat, comparison, or timeline to show |
| Hot take | MAYBE | Only if backed by data worth visualizing |
| Humor / ultra-short | NO | Text-only is fine. Image dilutes the punchline. |
| Career/personal | NO | Story is the content. Image adds nothing. |

### The Image Content Rule (CRITICAL)

**The image must ADD information that the post text does NOT contain.**

| Post text says... | Image should show... |
|---|---|
| "Our AI agent costs more than you think" | Actual cost breakdown: API 23%, Infra 31%, etc. |
| "95% of OpenAI engineers use Codex" | Stat card with 95% hero + supporting stats |
| "90% of our code is SaaS plumbing" | Code breakdown visualization: 90% SaaS / 10% AI |
| "I switched from CTO to founding engineer" | Timeline of career with titles and dates |
| "AI agent emailed lead 47 times" | Before/after: manual bug = 1 bad entry, agent bug = 47 emails |

**NEVER** make an image that just restates the post text in a pretty font.

---

## Phase 4: Generate Image

### Template Picker

Match your post content to a proven template from `skills/content/templates/linkedin/`:

| Post has... | Template | Source file |
|---|---|---|
| One big stat + 3-4 supporting stats | Stat Grid | `02-work-sustainability.html` |
| Two things to compare side-by-side | Comparison | `03-office-vs-remote.html` |
| A hero stat + step-by-step process | Hero + Steps | `04-chatgpt-distribution.html` |
| Multi-category data (sectors, roles) | Data Grid | `05-salary-guide.html` |
| Numbered list (5-10 items) | List | `06-secret-websites.html` |
| Numbered list with descriptions | Described List | `07-resignation-redflags.html` |
| Quotable one-liner + supporting points | Quote Card | `01-leadership-quote.html` |
| Multiple templates/examples to show | Card List | `08-resume-email.html` |
| Grid of tips/mistakes (2 columns) | 2-Column Grid | `09-interview-mistakes.html` |
| Categorized tool/resource list | Category Grid | `10-ai-cheatsheet.html` |
| Single hero number (big %) | Custom Stat Card | Use `personas/prateek/content/images/2026-02-13-junior-ladder.html` as reference |

### How to Fill a Template

1. **Read** the matching template HTML file
2. **Keep ALL CSS/styling unchanged** — these are proven designs
3. **Replace ONLY the text content** inside HTML elements
4. Keep the same number of items/rows (add/remove rows following the pattern if needed)
5. Change the accent color ONLY if the topic demands it (e.g., blue for tech, green for money, red for warnings)
6. Update any source/citation text at the bottom
7. **MANDATORY: Every image MUST include the persona handle** — `prateekjain98` for LinkedIn, `@Prateek9jain8` for X. All LinkedIn templates already have the handle baked in as a `.handle` div (absolute-positioned, bottom-right). When filling a template, do NOT remove it — only update the handle text if posting to X instead of LinkedIn.

### Save and Screenshot

```bash
# Save filled template
# Path: personas/prateek/content/images/YYYY-MM-DD-slug.html

# Generate PNG
cd .context && node screenshot.js ../personas/prateek/content/images/YYYY-MM-DD-slug.html
# Output: .context/linkedin_post_image.png

# Then move/copy to the images directory
cp .context/linkedin_post_image.png ../personas/prateek/content/images/YYYY-MM-DD-slug.png
```

### Visual Verification

After generating the PNG, READ the image file to verify:
- Text is readable at LinkedIn/X feed size
- No text overflow or clipping
- Colors and contrast are good
- Data is correct and properly sourced

---

## Phase 5: Publish

### LinkedIn Posting (via Chrome CDP)

1. Navigate to LinkedIn feed: `agent-browser --cdp 9222 open "https://www.linkedin.com/feed/"`
2. Click "Start a post": `agent-browser --cdp 9222 click @e<ref>`
3. Find the `.ql-editor` inside shadow DOM and set innerHTML with `<p>` tags and `<p><br></p>` for blank lines
4. Click "Add media" and use `agent-browser upload` to attach the image
5. Click "Post"

### X Posting (via Safari AppleScript)

1. Navigate to X compose
2. Use `document.execCommand('insertText')` for Draft.js editor
3. Upload image via base64 → Blob → File → DataTransfer approach
4. Click post button

### Post-Publish

- Stay online 60 min after posting, reply to every comment
- Check engagement after 1 hour and 24 hours
- Save post content to `personas/prateek/content/posts/` for reference

---

## Platform Adaptation

### LinkedIn → X conversion

When creating for both platforms:

| LinkedIn | X |
|----------|---|
| 300-600 chars | Under 280 chars (or short thread) |
| Paragraphs with line breaks | Compressed, punchier |
| 3-5 hashtags | 0-2 hashtags, use @mentions instead |
| Source citations inline | "Source: @handle" at end |
| Professional but conversational | More casual, can be edgier |

### X-specific rules
- Tag relevant accounts with @mentions
- Keep it under 280 chars for single tweets (threads for longer)
- More personality, less polish
- Reply-bait: leave a gap for people to fill in
