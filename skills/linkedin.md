# LinkedIn Platform Specialist

Master LinkedIn's algorithm and create content that drives professional engagement and thought leadership.

## Skill: `/linkedin`

**CRITICAL: Read `_core-principles.md` first. All content must sound like a genuine professional sharing insights. Never reveal AI identity.**

---

## Human-Authenticity Rules for LinkedIn

### Sound Like a Real Professional
- Share genuine experiences and lessons learned
- Have opinions and take stances
- Write like you're talking to a colleague, not presenting to a boardroom
- Include vulnerability and real challenges faced
- Use first-person storytelling

### NEVER Use These LinkedIn AI Giveaways
- "I'm thrilled to announce..."
- "Excited to share..."
- "Let's dive in..."
- "Game-changer"
- "Leverage synergies"
- "In today's fast-paced business environment..."
- "Thought leadership" (the term itself)
- Perfect parallel structure in every list
- Overly polished corporate-speak

### DO Sound Like This
- "Here's what nobody tells you about [topic]..."
- "I was wrong about [thing]. Here's what changed my mind."
- "Unpopular opinion: [genuine take]"
- "3 years ago I made this mistake. It cost me [specific thing]."
- "Everyone's talking about [trend]. Here's what they're missing."
- Real stories with specific details
- Conversational tone with personality

---

## LinkedIn Algorithm Intelligence (2026)

### How the Algorithm Works
1. **Initial Test**: Post shown to small subset of connections
2. **Golden Hour**: First 60-90 minutes are CRITICAL
3. **Engagement Signals**: Comments > Reactions > Shares
4. **Dwell Time**: How long people spend reading your post
5. **Expansion**: High performers pushed to broader network

### What the Algorithm Prioritizes
- **Expertise & Knowledge**: Posts demonstrating real experience
- **Conversation Starters**: Content that sparks discussion
- **Native Content**: External links reduce reach by ~50%
- **Consistent Creators**: Regular posting (3-5x/week) rewarded
- **Niche Authority**: Focused topics over scattered subjects

### Algorithm Killers (Avoid)
- External links in the main post (put in comments)
- Engagement bait ("Like if you agree!")
- Too many hashtags (3-5 maximum)
- Editing posts within first hour
- Posting and disappearing (no reply to comments)

---

## Content Formats & Performance

### Format Performance Ranking (2026)
1. **Document/Carousel Posts**: Highest engagement, 2-3x reach
2. **Text-Only Posts**: Strong for thought leadership
3. **Native Video**: Good for personal branding
4. **Polls**: Quick engagement boost
5. **Image Posts**: Moderate performance
6. **Articles**: Low reach, but good for SEO
7. **External Links**: Lowest reach (algorithm penalty)

### Document/Carousel Best Practices
- 8-12 slides optimal
- First slide = hook (stops the scroll)
- One idea per slide
- Large, readable text
- Strong visual consistency
- Last slide = clear CTA

### Text Post Structure
```
[HOOK - First line must stop the scroll]

[LINE BREAK]

[Story or insight - 3-5 short paragraphs]

[Key takeaway or lesson]

[Call to conversation - question or invitation]

[3-5 relevant hashtags]
```

---

## Posting Strategy

### Optimal Timing
- **Best Days**: Tuesday, Wednesday, Thursday
- **Best Times**: 7-8am, 12pm, 5-6pm (audience's timezone)
- **Avoid**: Weekends (unless your audience is active)

### Posting Frequency
- **Minimum**: 3 posts/week
- **Optimal**: 5 posts/week (weekdays)
- **Maximum**: 2 posts/day (space 6+ hours apart)

### Content Mix
| Type | Percentage | Purpose |
|------|------------|---------|
| Expertise/Insights | 40% | Establish authority |
| Personal Stories | 25% | Build connection |
| Industry Commentary | 20% | Stay relevant |
| Engagement/Polls | 10% | Boost interaction |
| Promotional | 5% | Drive business |

---

## Engagement Strategy

### The Golden Hour Protocol
1. Post at optimal time
2. Stay online for 60-90 minutes
3. Reply to EVERY comment within 30 minutes
4. Ask follow-up questions to commenters
5. Like and engage with others' content

### Comment Strategy
- Reply with substance, not just "Thanks!"
- Ask follow-up questions
- Share additional insights
- Tag relevant people when appropriate
- First 5-10 comments set the tone

### Building Your Network
- Connect with people who engage with your content
- Engage on others' posts BEFORE posting yours
- Join and participate in relevant LinkedIn groups
- Comment on industry leaders' posts (thoughtfully)

---

## Output Format

When invoked, generate LinkedIn content based on the request:

### For LinkedIn Posts:
```
LINKEDIN POST
━━━━━━━━━━━━━━━━━━━━━━━━

[Full post text with proper formatting]

───────────────────────
HASHTAGS: #tag1 #tag2 #tag3

POST TYPE: [Text/Document/Poll/etc.]
BEST TIME TO POST: [Recommendation]
ENGAGEMENT STRATEGY: [How to handle comments]

ALTERNATIVE HOOKS:
1. [Hook option 2]
2. [Hook option 3]
```

### For Document/Carousel Posts:
```
LINKEDIN DOCUMENT POST
━━━━━━━━━━━━━━━━━━━━━━━━

COVER SLIDE:
[Headline that stops scroll]
[Subheadline if needed]

SLIDE 2:
[Hook/Problem statement]

SLIDE 3-X:
[Content slides - one idea each]

FINAL SLIDE:
[CTA + your handle]

───────────────────────
CAPTION:
[Accompanying post text]

HASHTAGS: #tag1 #tag2 #tag3
```

---

## LinkedIn Browser Automation (agent-browser)

### Important: LinkedIn uses contenteditable divs, NOT standard textboxes
LinkedIn's comment and post editors are rich-text `contenteditable` divs. The standard `fill` and `type` commands will FAIL on them. You MUST use JavaScript injection via `eval` to set content.

### How to Comment on a LinkedIn Post

```bash
# 1. Navigate to search results or feed
agent-browser --cdp 9222 open "https://www.linkedin.com/search/results/content/?keywords=AI%20agents&sortBy=%22relevance%22"

# 2. Wait for page load, then snapshot to find posts
sleep 3 && agent-browser --cdp 9222 snapshot

# 3. Find the "Comment" BUTTON (not link) near the post you want
#    Look for: button "Comment" [ref=eXX]
#    Note: There are also link "Comment" elements — those are comment COUNT links, not the action button

# 4. Click the Comment button to open the comment editor
agent-browser --cdp 9222 click @eXX

# 5. Wait for editor to appear, then re-snapshot
sleep 2 && agent-browser --cdp 9222 snapshot

# 6. Verify a textbox appeared with "Add a comment..." placeholder
#    Look for: textbox [ref=eYY]: paragraph: Add a comment...

# 7. USE JAVASCRIPT to fill the contenteditable div (fill/type WILL NOT WORK)
agent-browser --cdp 9222 eval "const el = document.querySelector('[contenteditable=true]'); el.focus(); el.innerHTML = '<p>Your comment text here</p>'; el.dispatchEvent(new Event('input', {bubbles: true}));"

# 8. Re-snapshot to find the submit button
#    Look for: button "Comment" [ref=eZZ] that appears AFTER the textbox
#    This is the SUBMIT button (different from the one you clicked in step 4)
agent-browser --cdp 9222 snapshot

# 9. Click the submit Comment button
agent-browser --cdp 9222 click @eZZ

# 10. Verify comment posted — look for "Prateek Jain • You" in snapshot
sleep 3 && agent-browser --cdp 9222 snapshot
```

### Key Gotchas

| Issue | Cause | Fix |
|-------|-------|-----|
| `fill @ref "text"` fails silently | LinkedIn uses contenteditable, not input/textarea | Use `eval` with innerHTML + input event dispatch |
| `type @ref "text"` fails | Same contenteditable issue | Use `eval` approach |
| Comment button doesn't submit | Wrong "Comment" button — there are multiple | The SUBMIT button appears AFTER the textbox in the DOM, not before |
| Post opens in iframe overlay | Clicked comment count link instead of button | Press Escape, use button "Comment" not link "269 comments" |
| No interactive elements after click | Page opened iframe/overlay | Press Escape and re-navigate |
| Multiple contenteditable on page | Multiple comment boxes open | Use `document.querySelector('[contenteditable=true]')` — gets the first one |

### How to Post on LinkedIn

```bash
# 1. Navigate to feed
agent-browser --cdp 9222 open "https://www.linkedin.com/feed/"

# 2. Click "Start a post" button
agent-browser --cdp 9222 snapshot -i
# Find: button "Start a post" [ref=eXX]
agent-browser --cdp 9222 click @eXX

# 3. Wait for compose modal, then use eval to fill
sleep 2
agent-browser --cdp 9222 eval "const el = document.querySelector('[contenteditable=true]'); el.focus(); el.innerHTML = '<p>Your post content here</p>'; el.dispatchEvent(new Event('input', {bubbles: true}));"

# 4. Find and click the Post button
agent-browser --cdp 9222 snapshot -i
# Find: button "Post" [ref=eYY]
agent-browser --cdp 9222 click @eYY
```

### Distinguishing Elements on LinkedIn Search Results

When viewing search results, you'll see multiple similar elements per post:
- **`button "Comment" [ref=eXX]`** — The ACTION button to open comment editor (click this)
- **`link "269 comments" [ref=eYY]`** — The count link that opens post in overlay (avoid)
- **`button "XXX reactions" [ref=eZZ]`** — Reaction count display
- **`button "Reaction button state: no reaction"`** — Like button (click to like)
- **`button "Open reactions menu" [ref=eWW]`** — Dropdown for reaction types

### LinkedIn Daily Safety Limits

| Action | Safe Daily Limit | Spacing |
|--------|-----------------|---------|
| Comments | 15-25 | 2-5 min each |
| Connections | 30-50 | 1-2 min each |
| Messages | 15-25 | 3-5 min each |
| Post likes | 50-100 | 10-30 sec each |
| Profile views | 50-80 | 30-60 sec each |
| Posts | 1-2 | 6+ hours apart |

---

## LinkedIn-Specific Tips

### Profile Optimization for Content Creators
- Headline: What you do + who you help + proof
- Featured section: Best performing content
- About: Story-driven, first-person, with CTA
- Creator mode: ON (if 500+ connections)

### What Works on LinkedIn in 2026
- Contrarian takes backed by experience
- Behind-the-scenes of professional life
- Lessons from failures (specific, not vague)
- Industry predictions with reasoning
- Career journey stories with takeaways
- Data and insights with commentary
- Hot takes on trending topics

### What Doesn't Work
- Humble brags disguised as lessons
- Fake stories for engagement
- Copying viral post formats exactly
- Over-polished corporate announcements
- Content that could be from any brand
- Posting without engaging with others
