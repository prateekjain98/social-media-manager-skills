# Growth Algorithm — v1 (ARCHIVED)

> **Active:** Feb 6 – Feb 9, 2026
> **Status:** Superseded by `v2-multi-domain/_growth-algorithm.md`
> **Why archived:** AI-only reply targets and "is it in your niche? No → Skip" decision tree were too restrictive. Expanded to multi-domain engagement.

Executable algorithm for automated social media growth using agent-browser.

---

## Available Actions

### Navigation
| Action | Command | Use Case |
|--------|---------|----------|
| Go to URL | `open <url>` | Navigate anywhere |
| Go back | `back` | Return to previous page |
| Reload | `reload` | Refresh current page |
| Switch tabs | `tab <n>` | Multi-platform work |

### Understanding the Page
| Action | Command | Use Case |
|--------|---------|----------|
| Snapshot | `snapshot` | Get page structure with element refs |
| Snapshot (interactive only) | `snapshot -i` | Only buttons, inputs, links |
| Screenshot | `screenshot [path]` | Visual capture |
| Get text | `get text <sel>` | Extract specific text |
| Get URL | `get url` | Confirm current location |

### Interactions
| Action | Command | Use Case |
|--------|---------|----------|
| Click | `click @ref` | Like, follow, repost, open |
| Fill input | `fill @ref "text"` | Write replies, posts |
| Type | `type @ref "text"` | Type character by character |
| Press key | `press Enter` | Submit forms |
| Scroll | `scroll down 500` | Load more content |
| Hover | `hover @ref` | Reveal hidden elements |
| Wait | `wait 2000` | Pause for loading |

### X-Specific Actions

**Engagement:**
| Action | How to do it |
|--------|--------------|
| Like | Click the heart button |
| Repost | Click repost button → select "Repost" |
| Quote tweet | Click repost → "Quote" → fill → post |
| Reply | Click reply → fill textbox → click "Reply" |
| Bookmark | Click bookmark button |
| Follow | Click "Follow" button on profile |

**Content Creation:**
| Action | How to do it |
|--------|--------------|
| Post tweet | Click "Post" in nav → fill → click "Post" |
| Thread | Post → click "Add another post" → repeat |
| Post with media | Click media icon → upload file → fill → post |

**Discovery:**
| Action | How to do it |
|--------|--------------|
| Search | `open "https://x.com/search?q=keyword&f=live"` |
| View profile | `open "https://x.com/username"` |
| Check notifications | `open "https://x.com/notifications"` |
| Check analytics | `open "https://x.com/username/analytics"` |

---

## Target Account Strategy

### Finding Target Accounts (do once)

1. **Direct competitors/peers** - same niche, similar follower count
2. **Aspirational accounts** - bigger accounts you want to be like
3. **Content curators** - accounts that aggregate content in your niche
4. **Active engagers** - people who reply a lot (good for visibility)

For you (AI Expert positioning):

**TIER 1 - AI Company Executives (Reply within minutes of their posts)**
- @sama (Sam Altman - OpenAI CEO)
- @DarioAmodei (Dario Amodei - Anthropic CEO)
- @satyanadella (Satya Nadella - Microsoft CEO)
- @ClementDelangue (Clement Delangue - HuggingFace CEO)
- @AnthropicAI (Anthropic official)
- @OpenAI (OpenAI official)

**TIER 1 - AI Thought Leaders**
- @karpathy (Andrej Karpathy - ex-Tesla AI, ex-OpenAI)
- @ylecun (Yann LeCun - Meta AI Chief)
- @DrJimFan (Jim Fan - NVIDIA AI)
- @AndrewYNg (Andrew Ng - AI pioneer)
- @ESYudkowsky (Eliezer Yudkowsky - AI Safety)

**TIER 1 - AI Builder/Founders**
- @levelsio (Pieter Levels - ships fast)
- @mckaywrigley (McKay Wrigley - AI tools)
- @jxnlco (Jason Liu - AI eng)
- @hwchase17 (Harrison Chase - LangChain)
- @swyx (Swyx - AI eng/writer)

**TIER 2 - Dev Influencers (Daily check)**
- @theo (Theo Browne)
- @rauchg (Guillermo Rauch - Vercel)
- @ThePrimeagen
- @fireship_dev

**Engagement angle:** You BUILD AI agents in production. Not theory - real workflows that book meetings.

### Target Account Tiers

```
TIER 1: Notification alerts (5-10 accounts)
- Turn on notifications
- Reply within 5 min of their posts
- Highest value for visibility

TIER 2: Daily check (10-20 accounts)
- Check their profile daily
- Reply to best posts

TIER 3: Weekly discovery (ongoing)
- Find new accounts through search
- Find through replies to your targets
```

---

## How Followers Actually Grow

```
FOLLOWER GROWTH FUNNEL:
Your reply on viral post (1K+ likes)
→ Reply gets likes/engagement
→ People click your profile
→ They see good bio + content
→ They follow

KEY INSIGHT: Follows and likes are PASSIVE. They don't grow YOUR followers.
What grows followers:
1. REPLIES on high-visibility posts (biggest ROI)
2. QUOTE TWEETS (your take reaches both audiences)
3. BEING EARLY on big account posts (top reply placement)
4. THREADS showing depth (demonstrates expertise)
5. STRONG TAKES that trigger engagement (controversy = visibility)

PRIORITY ORDER:
1. Reply to viral posts (1K+ likes) — 60% of time
2. Quote tweet trending posts — 15% of time
3. Original posts/threads — 15% of time
4. Everything else (follows, likes, reciprocity) — 10% of time
```

---

## Daily Algorithm

### Session 1: Morning (25-30 min)

```
1. VIRAL POST HUNTING (HIGHEST PRIORITY)
   Search for trending AI topics:
   ├── open "https://x.com/search?q=AI agents OR GPT OR Claude OR Opus&f=top"
   ├── Find posts with 1K+ likes, especially recent ones
   ├── Reply with strong, specific takes (5-15 words)
   ├── Target: 5-8 replies on viral posts
   └── GOAL: Get YOUR reply liked → profile visits → follows

   Post selection criteria:
   ├── 1K+ likes (high visibility)
   ├── Posted <6 hours ago (still getting traffic)
   ├── Topic you have real experience with
   └── Few quality replies yet (your reply can stand out)

2. TARGET ACCOUNT SWEEP
   For each TIER 1 account (5-10):
   ├── open "https://x.com/{username}"
   ├── Check their MOST RECENT post
   ├── If posted <2 hours ago → reply IMMEDIATELY (early = top placement)
   └── Skip if post is old (your reply will be buried)

   Reply rules:
   ├── Max 15 words
   ├── Add specific insight OR humor
   ├── Never: "great post!", generic praise
   └── Be EARLY — first 10 replies get 90% of visibility

3. QUOTE TWEETS (HIGH ROI)
   Find 1-2 posts worth quote tweeting:
   ├── Add a strong take, not just agreement
   ├── Your QT reaches BOTH audiences
   ├── Best for controversial or nuanced takes
   └── "this is true but..." or "adding context:..." angles work

4. POST ORIGINAL CONTENT
   Content types to rotate:
   ├── Hot take (with substance) — best for engagement
   ├── Thread on AI agents from experience (1-2x/week)
   ├── Observation from building at SalesMonk
   └── Contrarian opinion backed by experience
```

### Session 2: Afternoon (15-20 min)

```
5. CHECK YOUR POST PERFORMANCE
   open "https://x.com/{your_handle}"

   For your morning post:
   ├── Reply to every comment (keeps thread active)
   ├── If doing well → quote tweet with extra thought
   └── If not → analyze why and adjust

6. TREND SURFING (VIRAL REPLIES)
   open "https://x.com/search?q={trending_AI_topic}&f=top"

   Hunt for high-visibility reply opportunities:
   ├── Posts with 500+ likes in the last few hours
   ├── Breaking news/announcements (be early)
   ├── Debates where you have a strong position
   └── Target: 5-8 more quality replies

7. QUOTE TWEET something from the afternoon discourse
   ├── 1-2 more QTs with strong takes
   └── Your take > just sharing

8. LIGHT RECIPROCITY (low priority)
   ├── Like/reply to people who engaged with YOU
   └── Only follow accounts that add value to YOUR feed
```

### Session 3: Evening (15-20 min)

```
7. MUTUAL ENGAGEMENT
   Check your "Following" feed
   ├── Engage with mutuals who posted today
   ├── Support people at your level
   └── This builds your "growth cohort"

8. DISCOVERY
   open "https://x.com/search?q={niche_topic}&f=live"

   Find new accounts:
   ├── Who's making good replies to big accounts?
   ├── Who has good content but low followers?
   └── Follow 3-5 quality new accounts

9. OPTIONAL: SECOND POST
   Only if you have something worth saying
   Evening posts can do well (different timezone audience)
```

---

## Reply Decision Tree

```
See a post →
├── Is it in your niche?
│   ├── No → Skip
│   └── Yes ↓
├── Can you add something specific?
│   ├── No (only generic) → Skip
│   └── Yes ↓
├── Is there a humor angle?
│   ├── Yes → Use it (short)
│   └── No → Use experience angle (short)
└── Draft reply → CONTENT REVIEW GATE → Post
```

---

## Content Review Gate (MANDATORY)

**Every piece of content — replies, posts, quote tweets, LinkedIn comments — MUST pass through this review loop before posting.**

The writer drafts content. The editor reviews it. If it fails ANY check, the writer rewrites. This loops until the content passes ALL checks.

```
WRITER → drafts content
    ↓
EDITOR → reviews against checklist
    ↓
PASS? ──→ YES → Post it
    ↓
    NO → Return to WRITER with specific feedback
    ↓
WRITER → rewrites based on feedback
    ↓
EDITOR → reviews again
    ↓
(repeat until PASS)
```

### Editor Checklist (ALL must pass)

**1. Persona Alignment**
- [ ] Sounds like Prateek — senior engineer who ships, not a commentator
- [ ] References real experience (SalesMonk, EvolvFit, NAV, Swiggy) when relevant
- [ ] Matches the voice: direct, opinionated, casual but properly capitalized, no hedging
- [ ] Doesn't sound like a beginner, a teacher, or someone seeking validation
- [ ] Uses "I built/shipped/saw" not "I think/believe/feel"

**2. Context Match (MOST IMPORTANT CHECK)**
- [ ] Reply actually addresses the SPECIFIC content of the post being replied to
- [ ] Adds value — not just agreement, not just restating what they said
- [ ] Angle is relevant (don't talk about sales agents on an unrelated post)
- [ ] Tone matches the conversation (humor on humor, serious on serious)
- [ ] If disagreeing, has substance — not contrarian for the sake of it
- [ ] **IMAGE/VIDEO RULE: If post has image/video you can't see, DO NOT reply — your reply will be generic**
- [ ] **SPECIFICITY TEST: Could this reply go on 10+ similar posts? If yes, it's too generic — rewrite**
- [ ] **CHECK TOP COMMENTS first to learn what angle works on this specific post**

**3. Anti-AI Detection (from _core-principles.md)**
- [ ] Zero banned phrases ("dive in", "game-changer", "leverage", "robust", "seamless", etc.)
- [ ] No perfect parallel structure in lists
- [ ] Not relentlessly positive — has edge, opinion, or nuance
- [ ] Doesn't over-explain or over-qualify
- [ ] Has natural language markers ("honestly", "look", "the thing is")
- [ ] Imperfect but authentic — reads like a text message, not an essay
- [ ] Passes the 95/100 test: 95 out of 100 people would say a human wrote this

**4. Platform-Specific Rules**

*X (Twitter):*
- [ ] Replies: under 280 chars (without Premium), ideally under 15 words
- [ ] No hashtags in replies (looks spammy)
- [ ] Casual tone with proper sentence capitalization (casual ≠ no caps)
- [ ] Original posts: can be longer but still conversational
- [ ] Quote tweets: adds a strong take, not just "this is great"

*LinkedIn:*
- [ ] Professional but human — not corporate-speak
- [ ] Posts: hook in first 2 lines (must pass "see more" test)
- [ ] Comments: add insight, not "great post!"
- [ ] Ending varies — not always a question (max 50% questions)
- [ ] 3-5 relevant hashtags on posts, zero on comments
- [ ] Under 1500 chars unless carousel

**5. Differentiation**
- [ ] Not something 100 other people would also reply
- [ ] Has a unique angle from production experience
- [ ] Stands out in a thread — would you notice this reply scrolling?
- [ ] Doesn't repeat a reply we already made on the same post

### Common Editor Rejections (with fixes)

```
REJECT: "This is so true. We see this all the time in production."
WHY: Generic agreement. No specific detail. Anyone could say this.
FIX: "saw this exact pattern last month. our agent booked 47 duplicate meetings before we added idempotency keys."

REJECT: "Great point about error handling in AI systems."
WHY: Generic praise + AI buzzword combo. Classic AI reply.
FIX: "the error handling part hits home. 90% of our agent codebase is recovery logic."

REJECT: "I completely agree. This is a game-changer for the industry."
WHY: "Completely agree" + "game-changer" = instant AI detection.
FIX: "been saying this for months. the companies solving this win everything."

REJECT: "As someone who works with AI agents, I can confirm this is accurate."
WHY: "As someone who" + "I can confirm" = AI-speak.
FIX: "can confirm. we run agents in production and [specific detail]."

REJECT: "Every founder needs to rewatch this show yearly. It went from comedy to documentary real quick."
WHY: Generic — could be posted on ANY Silicon Valley related post. Doesn't reference the specific clip or content.
FIX: Reference something specific from the video/post, or don't reply if you can't see the media.

REJECT: "Your 20s convince you that FOMO is real. Your late 20s teach you the couch was the right call all along."
WHY: Quote-bait. Reads like a motivational account, not a real person. No personal detail.
FIX: "Used to spend Friday nights at Koramangala pubs trying to network. Now I spend them on my couch debugging side projects. Way happier."

REJECT: "The fact that indie hackers went from shipping SaaS to shipping physical lobster houses for servers is peak 2026."
WHY: Meta-commentary that doesn't engage with the product. Detached observer tone.
FIX: Engage directly with the product — ask a question, make a specific joke about it, or share how you'd use it.

REJECT: "The future of software development is truly exciting."
WHY: Vague, positive, no substance. Zero personality.
FIX: "the future is already here. our agents ship more code than we do."
```

### Review Speed vs Depth

- **Replies (short):** Quick scan — 3 seconds. Check for banned phrases, generic agreement, and persona match.
- **Original posts:** Full checklist review. Every item must pass.
- **Quote tweets:** Medium review. Check that your take adds something the original didn't say.
- **LinkedIn posts:** Full checklist + ending variety check + "see more" hook test.

### Reply Templates (use as inspiration, not copy-paste)

**Agreement with specific detail:**
- "this. [one specific reason from experience]"
- "^^ especially [the specific part]"
- "[specific number] times this happened to me"

**Disagreement/Nuance:**
- "counterpoint: [specific experience]"
- "mostly true except [edge case]"
- "worked until [specific situation]"

**Humor/Sarcasm:**
- "[exaggerated version of their point]"
- "the [specific thing] trauma is real"
- "[relatable failure]"

**Personal experience:**
- "built this. [one insight]"
- "tried [thing]. [result]"
- "saw [specific number] of these [fail/succeed]"

---

## Safety Limits

### Daily Maximums (Conservative)

| Action | New Account (<1mo) | Established |
|--------|-------------------|-------------|
| Follows | 15-20 | 30-40 |
| Likes | 30-50 | 80-100 |
| Replies | 20-30 | 40-50 |
| DMs | 5-10 | 15-20 |
| Posts | 2-3 | 3-5 |

### Timing Patterns

```python
# Random delay between actions (Python-like pseudocode)
def get_delay():
    base = random.randint(30, 90)  # 30-90 seconds

    # Occasionally take longer breaks (like a human)
    if random.random() < 0.2:  # 20% chance
        base += random.randint(60, 180)  # 1-3 min extra

    return base

# Between sessions
session_break = random.randint(120, 300)  # 2-5 min
```

### Red Flags to Avoid

- Same reply text to multiple posts
- Replying to same account repeatedly (3+ in a row)
- Following then unfollowing
- Engaging at perfectly regular intervals
- Engaging 24/7 (pick realistic hours)

---

## Execution Flow

### Single Reply Sequence

```bash
# 1. Navigate to target post
agent-browser --cdp 9222 open "https://x.com/username/status/123"
sleep 2

# 2. Understand the page — read the FULL post context
agent-browser --cdp 9222 snapshot

# 3. WRITER: Draft reply based on post context + persona
#    - What specific point can I add from my experience?
#    - What angle hasn't been said by the other replies?

# 4. EDITOR: Run Content Review Gate on draft
#    - Persona alignment? Context match? Anti-AI? Platform rules?
#    - If FAIL → rewrite with specific feedback
#    - If PASS → proceed to post

# 5. Find and click reply button
agent-browser --cdp 9222 click @[reply_button_ref]
sleep 1

# 6. Snapshot to find textbox
agent-browser --cdp 9222 snapshot

# 7. Type the APPROVED reply
agent-browser --cdp 9222 fill @[textbox_ref] "your reviewed reply here"
sleep 1

# 8. Verify and post
agent-browser --cdp 9222 snapshot  # check character count
agent-browser --cdp 9222 click @[post_button_ref]

# 9. Random delay before next action
sleep $((RANDOM % 60 + 30))
```

### Full Morning Session Sequence

```bash
#!/bin/bash
CDP=9222

# 1. Check notifications
agent-browser --cdp $CDP open "https://x.com/notifications"
sleep 3
agent-browser --cdp $CDP snapshot

# Process notifications (agent reads snapshot, decides actions)
# ... engage with relevant ones ...

# 2. Target account sweep
TARGETS=("rauchg" "theo" "ThePrimeagen")
for account in "${TARGETS[@]}"; do
    agent-browser --cdp $CDP open "https://x.com/$account"
    sleep 3
    agent-browser --cdp $CDP snapshot

    # Agent decides if there's a good reply opportunity
    # If yes: navigate to tweet, craft reply, post

    # Random delay
    sleep $((RANDOM % 60 + 45))
done

# 3. Post original content
agent-browser --cdp $CDP open "https://x.com/compose/post"
sleep 2
agent-browser --cdp $CDP snapshot
# ... compose and post ...
```

---

## Metrics to Track

### Weekly Review

| Metric | How to Check | Target |
|--------|--------------|--------|
| Follower growth | Profile page | +50-100/week once rolling |
| Profile visits | Analytics | Increasing |
| Reply engagement | Check replies you made | Some getting likes/replies |
| Post engagement | Analytics | > 2% engagement rate |

### What to Optimize

**If not growing:**
1. Check reply quality (are you adding value?)
2. Check content quality (would YOU engage with it?)
3. Check if targeting right accounts
4. Check consistency (daily showing up?)

**If growing slowly:**
- Normal for first 3-6 months
- Focus on reply quality over quantity
- Build deeper relationships with fewer people

---

## Implementation Notes

### What the Agent Handles
- Navigation and page interaction
- Crafting replies based on context
- Timing and safety limits
- Finding opportunities

### What Requires Human Input
- Deciding overall strategy
- Approving major content
- Handling edge cases
- Adjusting approach based on results

### Checkpoints
1. After every 10 replies → review quality
2. Weekly → review metrics and adjust
3. Monthly → reassess target accounts
