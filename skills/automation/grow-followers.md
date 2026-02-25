# Grow Followers — Execution Skill

## Skill: `/grow-followers`

An executable growth session runbook. When invoked, the agent runs all phases sequentially: research → engage → grow → track. No manual steps — everything is automated via Safari JavaScript injection.

**Prerequisites**: Read these before executing:
- `strategy/_core-principles.md` — anti-AI detection rules
- `personas/[name]/strategy/active/_persona.md` — persona identity and voice
- `strategy/_growth-algorithm.md` — canonical safety limits, content review gate
- `skills/automation/agent-browser.md` — Critical Safari Rules section

---

## CRITICAL AUTOMATION RULES

- **ONLY** use `osascript -e 'tell application "Safari" to do JavaScript "..." in front document'` for ALL browser interaction
- **NEVER** use System Events, cliclick, AppleScript `activate`, or any focus/keyboard/mouse stealing
- **NEVER** use `tell application "Safari" to activate` — steals focus
- Navigation: `tell application "Safari" to set URL of front document to "..."` (doesn't steal focus)
- All text input via JS: Draft.js `execCommand` for X, `innerHTML` on `.ql-editor` for LinkedIn
- All clicks via JS: `.click()` on DOM elements
- All file uploads via `DataTransfer` API on `input[type=file]`
- **Apostrophe escaping**: When using `osascript -e '...'`, apostrophes/single-quotes in text will break the shell quoting. Either use `heredoc` (`osascript <<'APPLESCRIPT'`) or replace `'` with backtick/remove from text. Write `"does not"` instead of `"doesn't"`.
- **X text injection requires click+focus+delay**: `editor.click(); editor.focus(); setTimeout(() => execCommand("insertText", false, text), 300)`. Without this, Draft.js silently ignores the text.
- **Verify after injection**: Check `editor.innerText.length` — if it's `1`, text didn't inject. Retry or reload page.
- **LinkedIn: ALWAYS navigate to the individual post URL first** — NEVER comment from the feed. The feed DOM shifts as it loads, and clicking "Comment" on one post can open the editor for a completely different post. Navigate to `https://www.linkedin.com/feed/update/urn:li:activity:XXXXXXX/` first, then comment.
- **LinkedIn: VERIFY post content before commenting** — After navigating to the post URL, extract the post text and confirm it matches the topic you're commenting on. If the post text doesn't match, STOP and don't comment.
- **LinkedIn: VERIFY comment landed on correct post** — After submitting, check the page to confirm your comment appears under the correct post. If it doesn't, delete it immediately.

---

## SESSION INITIALIZATION

### 1. Check Time Window

| Window | IST | US ET | Priority |
|--------|-----|-------|----------|
| Morning | 8:00–9:30 AM | 9:30–11 PM (prev day) | India + LinkedIn |
| **Money Window** | **8:00–10:00 PM** | **9:30 AM–1:30 PM** | **Primary. US tech peak.** |
| Late Night | 10:30 PM–12:00 AM | 12:00–1:30 PM | Ride US momentum |

If outside all windows, still proceed but note reduced reach.

### 2. Load Session State

Read `personas/prateek/metrics.md` to check today's action counts. Calculate remaining budget:

```
DAILY LIMITS (Phase 1, <500 followers):
  # Canonical limits from strategy/_growth-algorithm.md
  Replies:           20/day
  Follows:           15/day
  Likes:             40/day
  LinkedIn comments: 12/day

SESSION COUNTERS:
  replies_remaining = max(0, 20 - replies_today)
  follows_remaining = max(0, 15 - follows_today)
  likes_remaining   = max(0, 40 - likes_today)
```

---

## PHASE 1 — RESEARCH (10-15 min)

Execute steps sequentially. Collect all targets before engaging.

### Step 1a: Check X Notifications (2-3 min)

Navigate and extract recent notifications for reciprocal engagement:

```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://x.com/notifications"'
```

Wait 4 seconds, then extract:

```bash
osascript -e 'tell application "Safari" to do JavaScript "
  JSON.stringify(Array.from(document.querySelectorAll(\"article\")).slice(0,10).map(function(el) {
    return {
      text: (el.textContent || \"\").substring(0, 200).replace(/\\s+/g, \" \"),
      link: (el.querySelector(\"a[href*=/status/]\") || {}).href || \"\"
    };
  }))
" in front document'
```

Flag any notifications that need a reply (someone replied to your post, quote-tweeted you, etc.).

### Step 1b: Hunt Viral Posts on X (5-7 min)

Execute these searches sequentially. For each, extract top 5-10 posts.

**Search 1 — Low-reply gold mines (highest priority):**
```
https://x.com/search?q=min_faves%3A5000%20-filter%3Areplies&f=top
```

**Search 2 — Fresh viral (today only):**
```
https://x.com/search?q=min_faves%3A1000%20since%3AYYYY-MM-DD&f=top
```
(Use today's date)

**Search 3 — Cross-domain viral (humor, culture, sports):**
Scroll the "For You" feed. Cross-domain posts get 20x better engagement than AI-only.

**Search 4 — AI/Tech viral:**
```
https://x.com/search?q=min_faves%3A1000%20(AI%20OR%20Claude%20OR%20GPT%20OR%20agents%20OR%20coding)&f=top
```

**Extraction pattern for each search:**
```bash
osascript -e 'tell application "Safari" to do JavaScript "
  JSON.stringify(Array.from(document.querySelectorAll(\"article\")).slice(0,10).map(function(el) {
    var tweetText = el.querySelector(\"[data-testid=tweetText]\");
    var userLink = el.querySelector(\"a[href*=/status/]\");
    var likeBtn = el.querySelector(\"[data-testid=like] span, [data-testid=unlike] span\");
    var replyBtn = el.querySelector(\"[data-testid=reply] span\");
    return {
      text: tweetText ? tweetText.textContent.substring(0, 200) : \"\",
      url: userLink ? userLink.href : \"\",
      likes: likeBtn ? likeBtn.textContent : \"0\",
      replies: replyBtn ? replyBtn.textContent : \"0\"
    };
  }))
" in front document'
```

**Selection criteria — rank posts by:**
1. Likes:replies ratio > 50:1 (less competition)
2. Post age < 2 hours (top reply placement)
3. Parent post likes > 5K (maximum visibility)
4. Cross-domain > AI-only (proven 20x)
5. Target account post (relationship building)

### Step 1c: Check Target Accounts (3-5 min)

Check Tier 1 accounts for fresh posts (<2 hours old):

**Tier 1 targets:** @sama, @karpathy, @levelsio, @rauchg, @GregIsenberg, @t3dotgg, @ThePrimeagen, @swyx

For each account:
```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://x.com/sama"'
```
Wait 3s, then:
```bash
osascript -e 'tell application "Safari" to do JavaScript "
  var article = document.querySelector(\"article\");
  if (!article) return \"NO_TWEETS\";
  var time = article.querySelector(\"time\");
  var text = article.querySelector(\"[data-testid=tweetText]\");
  var link = article.querySelector(\"a[href*=/status/]\");
  JSON.stringify({
    time: time ? time.getAttribute(\"datetime\") : null,
    text: text ? text.textContent.substring(0, 200) : \"\",
    url: link ? link.href : \"\"
  })
" in front document'
```

If post is <2 hours old, flag as HIGH PRIORITY reply target.

### Step 1d: Hacker News Check (2 min)

```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://news.ycombinator.com"'
```
Wait 3s, extract top 10:
```bash
osascript -e 'tell application "Safari" to do JavaScript "
  JSON.stringify(Array.from(document.querySelectorAll(\".titleline a\")).slice(0,10).map(function(el) {
    return { title: el.textContent, url: el.href };
  }))
" in front document'
```

Note trending topics that overlap with Prateek's content pillars (AI agents, production engineering, startup, Indian tech).

### Step 1d2: Research for Original Content (3-5 min)

**This step is MANDATORY.** Don't skip it. Original content based on real research gets 5-10x more engagement than generic hot takes.

1. **Pick 1-2 trending topics** from HN, X trending, or target account posts
2. **Actually read the source material** — fetch the article, blog post, or announcement
3. **Extract specific data points** — numbers, quotes, comparisons that most people won't read
4. **Find the non-obvious angle** — what is everyone missing? What's the second-order effect?
5. **Identify who to tag** — who created this? Who does it affect? Who has opinions on it?

```bash
# Fetch and read source article
osascript -e 'tell application "Safari" to set URL of front document to "ARTICLE_URL"'
# Wait 4s, extract key content
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var title = document.title;
    var ogImage = (document.querySelector('meta[property=\"og:image\"]') || {}).content || '';
    var article = document.querySelector('article') || document.querySelector('main') || document.body;
    var text = article ? article.innerText.substring(0, 3000) : '';
    JSON.stringify({title: title, ogImage: ogImage, text: text});
  " in front document
end tell
APPLESCRIPT
```

**Content Research Checklist:**
- [ ] Read the actual source (not just the headline)
- [ ] Extracted 2-3 specific data points or quotes
- [ ] Identified who to tag (@handles of people/companies involved)
- [ ] Found source URL for self-reply
- [ ] Identified the non-obvious angle or second-order effect

### Step 1e: LinkedIn Feed Scan (3 min)

```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://www.linkedin.com/feed/"'
```
Wait 4s, scroll main to top, extract:
```bash
osascript -e 'tell application "Safari" to do JavaScript "
  var main = document.querySelector(\"main\");
  if (main) main.scrollTop = 0;
  JSON.stringify(Array.from(document.querySelectorAll(\"[data-urn]\")).slice(0,8).map(function(el) {
    var text = el.textContent.substring(0, 200).replace(/\\s+/g, \" \");
    return { text: text, urn: el.getAttribute(\"data-urn\") };
  }))
" in front document'
```

Flag posts with high reactions from people in AI/tech/startup space.

---

## PHASE 2 — ENGAGE (20-30 min)

### TAGGING & CITATION RULES (applies to ALL content)

**Tagging (@mentions):**
- **Tag people/companies you reference** — e.g., if you mention Anthropic's new feature, tag `@AnthropicAI`. If discussing what Sam Altman said, tag `@sama`.
- **Tag in original posts and quote tweets** — tags send notifications → engagement → visibility
- **Tag in replies ONLY when adding to the conversation** — don't tag random people in replies for attention
- **Max 2-3 tags per post** — more than that looks spammy
- **Tag the ORIGINAL AUTHOR when referencing their work** — gives credit and gets their attention
- **Never tag someone just to get a follow** — only tag when genuinely relevant

**Links & Citations:**
- **NEVER put links in the main tweet body** — X algorithm suppresses posts with links (~50% less distribution)
- **PUT LINKS IN A SELF-REPLY** — Post the tweet, then immediately reply to yourself with the link
- **Always cite sources** — "according to [Source]" or "Source: [Publication]" in the tweet text
- **For news reactions**: Name the article/source in the tweet, put the URL in the self-reply
- **For data drops**: Name the study/report and year in the tweet text
- **For referencing someone's work**: Tag them + mention what they said/built

**Self-Reply Pattern (for links, context, or CTA):**
After posting the main tweet, immediately reply to it with:
- Link to the source article/reference
- Additional context that didn't fit in the main post
- A question to bootstrap engagement ("What are you seeing?")
- A call to action ("Follow for more production AI takes")

### X Replies (10-15 replies per session)

<!-- SYNC: X Draft.js text injection pattern mirrors agent-browser.md > "X (Twitter) — Draft.js Editor (Safari)".
     If you update the pattern here, also update agent-browser.md, and vice versa. -->

For each selected post:

**1. Navigate to the post:**
```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://x.com/USER/status/TWEETID"'
```

**2. Read the post + existing replies** to understand context. Generate a reply using the Content Review Gate:

| Check | Rule |
|-------|------|
| Value | Does it TEACH, INFORM, REFRAME, ENTERTAIN, or DROP DATA? |
| Crutch | Is this just experience-anchoring? (max 30% of replies can be) |
| Context | Does it address the SPECIFIC content? |
| Anti-AI | No banned phrases, no perfect parallel structure |
| Length | 8-25 words. Short + punchy wins. |
| **Humor** | **Humor replies get 20x more engagement. PRIORITIZE.** |
| **Tags** | **Tag the OP if adding to their point. Tag relevant people/companies mentioned.** |
| **Data** | **Cite specific numbers, sources, or links when dropping data.** |

**Reply types that work (in order of effectiveness):**
1. **Humor** — dry wit, self-deprecating builder humor, unexpected angle
2. **Reframe** — flip the perspective with a non-obvious take
3. **Data drop** — cite a specific number, source, or benchmark (name the source!)
4. **Explainer** — explain HOW/WHY, not THAT it works
5. **Experience** — only when genuinely unique (max 30%)

**3. Click reply button:**
```bash
osascript -e 'tell application "Safari" to do JavaScript "
  document.querySelector(\"[data-testid=reply]\").click();
" in front document'
```

**4. Wait 2s, then type reply:**

**IMPORTANT**: Draft.js requires `click()` + `focus()` + a `setTimeout` delay before `execCommand("insertText")` works. Without the click+delay, the editor silently ignores the text. This is because Draft.js only enters its editing state after a real click activates its internal handlers.

```bash
osascript -e 'tell application "Safari" to do JavaScript "
  var editor = document.querySelector(\"[data-testid=tweetTextarea_0]\");
  if (!editor) { var editors = document.querySelectorAll(\"[role=textbox]\"); editor = editors[editors.length - 1]; }
  if (editor) {
    editor.click();
    editor.focus();
    setTimeout(function() {
      document.execCommand(\"insertText\", false, \"REPLY_TEXT_HERE\");
      window._replyLen = editor.innerText.length;
    }, 300);
  }
" in front document'
```

Then verify (wait 1s):
```bash
osascript -e 'tell application "Safari" to do JavaScript "window._replyLen" in front document'
```
If result is `1` (empty), the text didn't inject — retry or reload the page.

**5. Wait 1s, then click post:**
```bash
osascript -e 'tell application "Safari" to do JavaScript "
  var btn = document.querySelector(\"[data-testid=tweetButtonInline]\") || document.querySelector(\"[data-testid=tweetButton]\");
  if (btn) btn.click();
" in front document'
```

**6. Wait 45-120 seconds** (random) before next reply.

**7. After every 3-4 replies**, take a 2-5 minute break.

### LinkedIn Comments (5-8 per session)

<!-- SYNC: LinkedIn TipTap/ProseMirror commenting pattern mirrors agent-browser.md > "LinkedIn — TipTap/ProseMirror Editor (Safari)".
     If you update the pattern here, also update agent-browser.md, and vice versa. -->

**CRITICAL: NEVER comment from the feed.** The feed DOM shifts as it loads, and commenting from the feed has caused comments to land on the WRONG POST. Always navigate to the individual post URL first.

For each selected LinkedIn post:

**1. Navigate to the INDIVIDUAL POST URL (mandatory):**

Extract the activity URN from the feed scan, then navigate to it directly:
```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://www.linkedin.com/feed/update/urn:li:activity:ACTIVITY_ID/"'
```
Wait 4s for the page to fully load.

**2. VERIFY you are on the correct post (mandatory):**

Before doing ANYTHING else, extract the post text and confirm it matches the topic you intend to comment on:
```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var main = document.querySelector('main');
    var postText = main ? main.innerText.substring(0, 500) : '';
    postText;
  " in front document
end tell
APPLESCRIPT
```

**CHECK:** Does the extracted post text match the topic you are commenting on? If NOT, STOP. Do not comment. Move to the next post.

**3. Generate comment** using persona voice. The comment MUST be specifically about the content of the post you just verified. LinkedIn comments should be 2-4 sentences and add real value.

**4. Click Comment button on the post:**

```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var btns = document.querySelectorAll('button');
    for (var i = 0; i < btns.length; i++) {
      if (btns[i].textContent.trim() === 'Comment' && btns[i].getBoundingClientRect().width > 50 && btns[i].getBoundingClientRect().y > 0) {
        btns[i].click(); break;
      }
    }
  " in front document
end tell
APPLESCRIPT
```

**5. Wait 2s, find ProseMirror/TipTap editor, scroll to it, inject text:**

LinkedIn uses TipTap (ProseMirror) for comment editors. The editor is often off-screen — must `scrollIntoView` first.

```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var editor = document.querySelector('.tiptap.ProseMirror[contenteditable=true]');
    if (editor) {
      editor.scrollIntoView({behavior: 'instant', block: 'center'});
      setTimeout(function() {
        editor.focus();
        editor.innerHTML = '<p>COMMENT_TEXT_HERE</p>';
        editor.dispatchEvent(new Event('input', {bubbles: true}));
        window._commentLen = editor.innerText.length;
      }, 500);
    }
  " in front document
end tell
APPLESCRIPT
```

Verify: `window._commentLen` should match text length.

**6. Wait 1s, click submit button (the "Comment" button BELOW the editor):**

The submit button is a `<button>` with text "Comment" positioned just below the editor. Find it by proximity to `editor.getBoundingClientRect().bottom`.

```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var editor = document.querySelector('.tiptap.ProseMirror[contenteditable=true]');
    var editorBottom = editor.getBoundingClientRect().bottom;
    var btns = document.querySelectorAll('button');
    for (var i = 0; i < btns.length; i++) {
      var r = btns[i].getBoundingClientRect();
      if (r.y > editorBottom - 20 && r.y < editorBottom + 100 && btns[i].textContent.trim() === 'Comment') {
        btns[i].click(); break;
      }
    }
  " in front document
end tell
APPLESCRIPT
```

**7. VERIFY comment landed correctly:**
Wait 2s, then check that your comment appears on the post:
```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var comments = document.querySelectorAll('.comments-comment-item');
    var found = false;
    for (var i = 0; i < comments.length; i++) {
      if (comments[i].textContent.indexOf('FIRST_FEW_WORDS_OF_COMMENT') !== -1) {
        found = true; break;
      }
    }
    found ? 'VERIFIED' : 'NOT_FOUND';
  " in front document
end tell
APPLESCRIPT
```

If NOT_FOUND, check if the comment ended up somewhere else and delete it.

**6. Wait 2-5 minutes** between LinkedIn comments.

---

## PHASE 2B — ORIGINAL CONTENT (15-20 min)

Post 2-3 original posts per session. This is the **#1 lever for follower conversion** — replies get visibility but original content gives people a reason to follow.

> **For posts with images/infographics:** Use `skills/content/create-post.md` (Phase 4) for template selection, filling, and screenshot generation. Templates are in `skills/content/templates/linkedin/`, design specs in `skills/content/design-system.md`.

### Research Before Writing

**NEVER write a hot take from nothing.** Always research first:

1. **Check HN front page** — find a trending story in your content pillars
2. **Check X trending** — what are people talking about right now?
3. **Check recent announcements** — new product launches, funding rounds, open source releases
4. **Read the actual source** — fetch the article/blog post/paper, don't just react to a headline

```bash
# Fetch article content for research
osascript -e 'tell application "Safari" to set URL of front document to "ARTICLE_URL"'
# Wait 3s, then extract key points
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var title = document.title;
    var meta = document.querySelector('meta[name=\"description\"]');
    var desc = meta ? meta.content : '';
    var body = document.querySelector('article') || document.querySelector('main') || document.body;
    var text = body ? body.innerText.substring(0, 2000) : '';
    JSON.stringify({title: title, desc: desc, text: text});
  " in front document
end tell
APPLESCRIPT
```

### Original Post Structure

Every original post should follow this structure:

```
[HOOK — first line that stops the scroll]

[BODY — 2-5 lines of insight, data, or story]

[TAGS — @mention relevant people/companies, 1-3 max]
```

**Then immediately self-reply with:**
```
[SOURCE LINK — article/reference URL]
[ADDITIONAL CONTEXT — anything that didn't fit]
[CTA — "follow for more [topic]" or a question to bootstrap replies]
```

### Tagging Strategy for Original Posts

| Content Type | Who to Tag | Example |
|-------------|-----------|---------|
| News reaction | The company + the person who broke the news | "@AnthropicAI just shipped..." or "cc @sama" |
| Quoting someone | The person you're quoting | "@karpathy said X and he's right because..." |
| Comparing products | Both companies | "@OpenAI vs @AnthropicAI — here's what matters..." |
| Referencing a thread | The thread author | "expanding on what @swyx said about..." |
| Build in public | Tools/platforms you used | "built this with @vercel and @anthropic's Claude..." |

### Post to X Communities (Phase 1: <3K followers)

All original content should go to Communities, not main feed. Communities bypass the cold-start problem.

**Navigate to compose with community:**
```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://x.com/compose/post"'
```

Wait 3s, then activate editor and inject text:
```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var editor = document.querySelector('[data-testid=\"tweetTextarea_0\"]');
    if (!editor) { var editors = document.querySelectorAll('[role=\"textbox\"][contenteditable=\"true\"]'); editor = editors[editors.length - 1]; }
    if (editor) {
      editor.click();
      editor.focus();
      setTimeout(function() {
        document.execCommand('insertText', false, 'POST_TEXT_HERE');
        window._postLen = editor.innerText.length;
      }, 300);
    }
  " in front document
end tell
APPLESCRIPT
```

Verify text injected, then post:
```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var btn = document.querySelector('[data-testid=\"tweetButton\"]');
    if (btn) btn.click();
  " in front document
end tell
APPLESCRIPT
```

### Self-Reply (immediately after posting)

Navigate to your profile, find the just-posted tweet, click reply, and add:
- Source link
- Additional context
- A question to bootstrap engagement

```bash
# Navigate to profile to find the new post
osascript -e 'tell application "Safari" to set URL of front document to "https://x.com/Prateek9jain8"'
# Wait 3s, then click into the first tweet, click reply, inject self-reply text with link
```

---

## PHASE 3 — GROWTH ACTIONS (5-10 min)

### Strategic Follows (3-5 per session)

Follow people who are engaging with target accounts' content — they're in your potential audience.

```bash
osascript -e 'tell application "Safari" to set URL of front document to "https://x.com/TARGET_USER"'
```
Wait 3s:
```bash
osascript -e 'tell application "Safari" to do JavaScript "
  var btn = document.querySelector(\"[data-testid$=-follow]\");
  if (btn && btn.textContent.trim() === \"Follow\") { btn.click(); return \"FOLLOWED\"; }
  return \"ALREADY_FOLLOWING_OR_NOT_FOUND\";
" in front document'
```

**Wait 60-180 seconds** between follows.

### Strategic Likes (5-10 per session)

Like posts from growth cohort members, replies on your own posts, and strategic content from target accounts.

```bash
osascript -e 'tell application "Safari" to do JavaScript "
  var btn = document.querySelector(\"[data-testid=like]\");
  if (btn) btn.click();
" in front document'
```

**Wait 15-45 seconds** between likes.

---

## PHASE 4 — CROSS-POST (optional, 5 min)

Check if any LinkedIn post from the past week has 20+ reactions. If so, repurpose for X:
1. Shorten to <280 chars (punchier, more casual)
2. Remove LinkedIn-specific hashtags
3. Add 0-2 X-appropriate hashtags
4. Post using the X Draft.js method from Phase 2

Alternatively, use `/create-post` for a fresh cross-platform post.

---

## PHASE 5 — TRACK

### Log to `personas/prateek/metrics.md`

Append a session entry matching the existing format:

```markdown
### Session: YYYY-MM-DD HH:MM IST — [Window Name]

**Duration:** XX min

| Action | Platform | Count | Limit | Remaining |
|--------|----------|-------|-------|-----------|
| Replies | X | N | 20 | Y |
| Comments | LinkedIn | N | 12 | Y |
| Follows | X | N | 15 | Y |
| Likes | X | N | 40 | Y |

**Replies posted:**
| Target | Post Topic | Reply | Parent Likes |
|--------|-----------|-------|-------------|
| @user | topic | "reply text" | 5.2K |

**Key learnings:** [what worked, what didn't]
```

### Session Output

Print a summary:

```
GROWTH SESSION COMPLETE
━━━━━━━━━━━━━━━━━━━━━━
Date: YYYY-MM-DD
Window: [Morning / Money Window / Late Night]
Duration: XX min

RESEARCH: Found N viral posts, N fresh target posts, N LinkedIn posts
REPLIES: N/20 (X) + N/12 (LinkedIn)
FOLLOWS: N/15
LIKES: N/40

Top reply: "@user — REPLY_TEXT" (parent: XK likes)
```

---

## TIMING & SAFETY REFERENCE

```
BETWEEN ACTIONS:
  X replies:          45-120 seconds (random)
  X follows:          60-180 seconds (random)
  X likes:            15-45 seconds (random)
  LinkedIn comments:  2-5 minutes (random)
  Long break:         Every 3-4 actions, pause 2-5 min

NEVER:
  ✗ Same reply text to multiple posts
  ✗ Reply to same account 3+ times per session
  ✗ Follow then unfollow
  ✗ Act at perfectly regular intervals
  ✗ Skip the long breaks
  ✗ Use System Events, cliclick, or any focus-stealing automation
```

---

## PERSONA QUICK REFERENCE (Prateek)

**Voice:** Conversational, opinionated, occasionally funny. Like texting a smart friend.

**Humor style:** Dry engineering humor, self-deprecating builder stories, unglamorous truth.

**Content pillars:** AI agents in production, engineering & shipping, startup life, Indian tech scene, hot takes, humor.

**Key stories:** 47-email incident, crypto 90+ API integrations, Swiggy Rs 60K savings, career zigzag (M&A → Swiggy → NAV → EvolvFit → SalesMonk).

**Handles:** @Prateek9jain8 (X) | prateekjain98 (LinkedIn) | u/prateek63 (Reddit)
