# Follower Growth Agent

An autonomous goal-based agent for growing social media followers using strategic engagement patterns via agent-browser.

## Skill: `/growth-agent`

**CRITICAL: Read `_core-principles.md` and `agent-browser.md` first. All engagement must appear human-like. Never reveal automation.**

---

## Goal-Based Agent Framework

This skill introduces a framework for autonomous agents that pursue specific goals. Each agent:

1. **Has a defined goal** (e.g., "Grow X followers by 1000 in 30 days")
2. **Executes strategies** aligned with platform algorithms
3. **Tracks metrics** to measure progress
4. **Adapts behavior** based on results
5. **Operates within safety limits** to avoid detection

### Agent Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     GOAL-BASED AGENT                        │
├─────────────────────────────────────────────────────────────┤
│  GOAL: [Specific, Measurable, Time-bound]                  │
├─────────────────────────────────────────────────────────────┤
│  STRATEGIES                                                 │
│  ├── Strategy 1: [Action pattern]                          │
│  ├── Strategy 2: [Action pattern]                          │
│  └── Strategy 3: [Action pattern]                          │
├─────────────────────────────────────────────────────────────┤
│  EXECUTION ENGINE                                           │
│  ├── Daily Session Planner                                 │
│  ├── Action Sequencer (with human-like timing)             │
│  ├── Anti-Detection Guard                                  │
│  └── Progress Tracker                                      │
├─────────────────────────────────────────────────────────────┤
│  SAFETY LIMITS                                              │
│  ├── Rate limits per action type                           │
│  ├── Session duration limits                               │
│  ├── Cool-down periods                                     │
│  └── Behavioral variance injection                         │
└─────────────────────────────────────────────────────────────┘
```

---

## The Follower Growth Algorithm

### Core Principle: The Engagement Flywheel

```
          ┌─────────────────┐
          │   YOUR CONTENT  │
          └────────┬────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │  STRATEGIC ENGAGEMENT        │
    │  (Reply to bigger accounts)  │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │  VISIBILITY                  │
    │  (Appear in their audience)  │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │  PROFILE VISITS              │
    │  (Curious users check you)   │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │  FOLLOW DECISION             │
    │  (Bio + content = follow)    │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │  NEW FOLLOWERS               │
    │  (Engage with your content)  │
    └──────────────────────────────┘
```

### The 70/30 Rule

**Spend 70% of time engaging, 30% creating content.**

This is the most important principle. Most people invert this and fail.

---

## Platform-Specific Growth Algorithms

### X (Twitter) Growth Algorithm

#### Phase 1: Foundation (Week 1-2)
- Optimize profile (bio, pinned tweet, banner)
- Identify 20-30 target accounts (2-10x your size, same niche)
- Establish posting rhythm (3-5 posts/day)

#### Phase 2: Strategic Engagement (Ongoing)

**The Reply Strategy (Highest ROI)**
```
DAILY ROUTINE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. MORNING SESSION (30-45 min)
   └── Find 5-10 fresh posts from target accounts
   └── Reply with genuine value (not "Great post!")
   └── Engage with other replies on those posts

2. POST YOUR CONTENT (15 min)
   └── Post 1-2 original tweets
   └── Reply to ALL comments within 15 min

3. AFTERNOON SESSION (20-30 min)
   └── Find trending posts in your niche
   └── Add valuable commentary
   └── Quote-tweet with insights

4. EVENING SESSION (20 min)
   └── Engage with your timeline
   └── Reply to new followers
   └── Like/reply to those who engaged with you
```

**Reply Quality Framework**
```
BAD REPLIES (Ignored):
- "Great post!"
- "So true!"
- "Love this!"
- Emojis only

GOOD REPLIES (Get noticed):
- Add a related insight
- Share a personal experience
- Ask a thoughtful question
- Respectfully challenge with reasoning
- Provide additional data/examples

GREAT REPLIES (Get followers):
- Mini-threads that expand on the topic
- Unique perspective that sparks discussion
- Stories that illustrate the point
- Resources that add value
```

#### Phase 3: Content Strategy

**The 3:1 Reply Ratio**
- Post 1 original tweet
- Reply to 3 bigger accounts within 60 seconds
- This trains the algorithm to boost your content

**Thread Strategy (3x engagement)**
```
THREAD STRUCTURE:
━━━━━━━━━━━━━━━━━━

Tweet 1 (HOOK):
[Bold claim or question that stops scroll]

Tweet 2-3 (PROBLEM):
[Pain point your audience relates to]

Tweet 4-8 (SOLUTION):
[Actionable insights, numbered]

Tweet 9 (PROOF):
[Your results or case study]

Tweet 10 (CTA):
[Follow for more + retweet request]
```

**Posting Schedule**
| Time (CST) | Content Type | Why |
|------------|--------------|-----|
| 6-8 AM | Thread or insight | Early US timezone boost |
| 12-1 PM | Engagement post (question/poll) | Lunch break activity |
| 5-6 PM | Quote tweet or hot take | Evening scroll time |

#### X Growth Agent Commands

```bash
# Session 1: Morning Engagement
agent-browser --cdp 9222 open "https://x.com/[target_account]"
agent-browser --cdp 9222 snapshot -i
# Find and click on recent tweet
# Wait 3-5 seconds (reading)
# Click reply button
agent-browser --cdp 9222 fill @reply "[thoughtful reply]"
# Wait 1-2 seconds
agent-browser --cdp 9222 click @post_button
# Wait 30-60 seconds before next

# Session 2: Check Notifications
agent-browser --cdp 9222 open "https://x.com/notifications"
agent-browser --cdp 9222 snapshot -i
# Reply to anyone who engaged with you
# Follow back quality accounts
```

---

### LinkedIn Growth Algorithm

#### The Authority Model

LinkedIn's 2026 algorithm rewards **depth over breadth**. You must:
1. Pick ONE niche topic
2. Become the go-to voice on it
3. Create "dwell time" content (carousels, long posts)

#### Daily LinkedIn Routine

```
LINKEDIN DAILY ALGORITHM:
━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PRE-POST ENGAGEMENT (15 min before posting)
   └── Comment on 5-10 posts in your niche
   └── Genuine, insightful comments (not "Great post!")
   └── This warms up your reach

2. POST YOUR CONTENT
   └── Document/Carousel: 8-12 slides
   └── OR Text post: Hook + story + insight + CTA
   └── First line = everything (hook)

3. ENGAGEMENT WINDOW (60 min after posting)
   └── Reply to EVERY comment within 5 min
   └── Ask follow-up questions
   └── Keep the conversation going
   └── Comments > likes for algorithm

4. THROUGHOUT DAY
   └── Engage with people who viewed your profile
   └── Send personalized connection requests
   └── Comment on industry news
```

#### Connection Request Strategy

```
CONNECTION REQUEST TEMPLATE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Hi [Name], I noticed your post about [specific topic].
[One sentence about what resonated with you].
Would love to connect and follow your insights on [niche]."

AVOID:
- Blank connection requests
- Immediate sales pitch
- Generic "I'd like to add you"
```

#### LinkedIn Agent Commands

```bash
# Engagement Session
agent-browser --cdp 9222 open "https://linkedin.com/feed"
agent-browser --cdp 9222 scroll down 500
agent-browser --cdp 9222 snapshot -i
# Find posts from target accounts
# Click comment button
agent-browser --cdp 9222 fill @comment "[insightful comment]"
agent-browser --cdp 9222 click @post_button
# Wait 60-120 seconds before next

# Profile Visit Response
agent-browser --cdp 9222 open "https://linkedin.com/me/profile-views"
agent-browser --cdp 9222 snapshot -i
# Review who viewed your profile
# Send connection requests to relevant people
```

---

### Instagram Growth Algorithm

#### The Shares-First Model

Instagram 2026 prioritizes:
1. **Sends** (DM shares) - Most powerful
2. **Saves** - High intent signal
3. **Comments** - Engagement signal
4. **Likes** - Basic signal

#### Content Strategy for Followers

```
CONTENT MIX FOR GROWTH:
━━━━━━━━━━━━━━━━━━━━━━━

REELS (60% of posts):
- 3-second hook mandatory
- 30-60 seconds optimal
- Trending audio when relevant
- End with CTA to follow

CAROUSELS (25% of posts):
- Swipeable value content
- Hook on slide 1
- CTA on last slide
- Save-worthy information

STORIES (Daily):
- Behind the scenes
- Polls and questions
- Engage existing audience
- Drive to new content
```

#### Engagement Strategy

```
DAILY INSTAGRAM ROUTINE:
━━━━━━━━━━━━━━━━━━━━━━━━

1. STORY ENGAGEMENT (15 min)
   └── Reply to stories from target accounts
   └── Use relevant emojis + genuine message
   └── This puts you in their DMs

2. COMMENT STRATEGY (20 min)
   └── Comment on posts BEFORE they blow up
   └── Be one of first 10 comments
   └── Add value, ask questions
   └── Your comment gets visibility as post grows

3. HASHTAG EXPLORATION
   └── Find posts in your niche hashtags
   └── Engage with creators at your level
   └── Build relationships, not just followers

4. DM RELATIONSHIP BUILDING
   └── Reply thoughtfully to DMs
   └── Initiate conversations with engaged followers
   └── Never pitch in first message
```

---

## Agent Execution Framework

### Daily Session Structure

```python
# Pseudocode for Agent Execution

GOAL = "Grow X followers by 1000 in 30 days"

DAILY_TARGETS = {
    "strategic_replies": 15-20,
    "quality_comments": 10-15,
    "original_posts": 3-5,
    "profile_visits_to_follow": 5-10,
    "DM_responses": all
}

SESSION_STRUCTURE = {
    "morning": {
        "duration": "30-45 min",
        "actions": ["strategic_replies", "post_content"]
    },
    "midday": {
        "duration": "15-20 min",
        "actions": ["engagement_check", "reply_to_comments"]
    },
    "evening": {
        "duration": "20-30 min",
        "actions": ["strategic_replies", "timeline_engagement"]
    }
}
```

### Action Timing (Human-Like)

```
TIMING VARIANCE:
━━━━━━━━━━━━━━━━━━

Between replies: 45-120 seconds (random)
Between likes: 15-45 seconds (random)
Between follows: 60-180 seconds (random)
Reading before action: 3-10 seconds (random)
Typing speed: 50-100ms per character (random)
Session breaks: 2-4 hours
```

### Anti-Detection Measures

```
SAFETY PROTOCOLS:
━━━━━━━━━━━━━━━━━━

1. NEVER exceed daily limits
2. ALWAYS add random variance to timing
3. MIX action types (don't do 20 follows in a row)
4. INCLUDE natural breaks (scroll without action)
5. VARY session start times
6. SKIP days occasionally (like real humans)
7. RESPOND to replies (bots don't do this well)
```

---

## Metrics & Tracking

### Key Metrics to Track

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Profile Visits | +20% weekly | Platform analytics |
| Profile → Follow Rate | 10-15% | Followers ÷ Profile visits |
| Engagement Rate | 3-5% | Engagements ÷ Impressions |
| Reply → Profile Visit | 5-10% | Track via link clicks |
| Follower Growth Rate | +5% weekly | Weekly follower count |

### Progress Tracking Template

```
WEEKLY PROGRESS LOG:
━━━━━━━━━━━━━━━━━━━━

Week: [X]
Starting Followers: [N]
Ending Followers: [N]
Net Growth: [+/-N] ([X]%)

Actions Taken:
- Strategic replies: [N]
- Original posts: [N]
- Threads: [N]
- Comments: [N]

Top Performing:
- Best reply: [link] → [result]
- Best post: [link] → [result]

Learnings:
- What worked: [insight]
- What didn't: [insight]
- Adjustments: [changes for next week]
```

---

## Agent Command Sequences

### X (Twitter) Follower Growth Session

```bash
#!/bin/bash
# X Follower Growth Agent - Morning Session

CDP_PORT=9222

# 1. Navigate to target account
agent-browser --cdp $CDP_PORT open "https://x.com/[TARGET_ACCOUNT]"
sleep $((RANDOM % 3 + 2))  # 2-5 seconds

# 2. Get page snapshot
agent-browser --cdp $CDP_PORT snapshot -i

# 3. Find latest tweet (manually identify ref)
sleep $((RANDOM % 5 + 3))  # 3-8 seconds (reading time)

# 4. Click on tweet to open
agent-browser --cdp $CDP_PORT click @[TWEET_REF]
sleep $((RANDOM % 3 + 2))

# 5. Snapshot for reply button
agent-browser --cdp $CDP_PORT snapshot -i

# 6. Click reply
agent-browser --cdp $CDP_PORT click @[REPLY_REF]
sleep $((RANDOM % 2 + 1))

# 7. Type reply (with human-like speed)
agent-browser --cdp $CDP_PORT type @[INPUT_REF] "[REPLY_TEXT]"
sleep $((RANDOM % 3 + 2))

# 8. Post reply
agent-browser --cdp $CDP_PORT click @[POST_BUTTON]
sleep $((RANDOM % 60 + 45))  # 45-105 seconds before next

# Repeat for next target...
```

### LinkedIn Engagement Session

```bash
#!/bin/bash
# LinkedIn Engagement Agent

CDP_PORT=9222

# 1. Open LinkedIn Feed
agent-browser --cdp $CDP_PORT open "https://linkedin.com/feed"
sleep $((RANDOM % 4 + 3))

# 2. Scroll to find posts
agent-browser --cdp $CDP_PORT scroll down 300
sleep $((RANDOM % 3 + 2))

# 3. Snapshot for elements
agent-browser --cdp $CDP_PORT snapshot -i

# 4. Find and click comment on target post
agent-browser --cdp $CDP_PORT click @[COMMENT_BUTTON]
sleep $((RANDOM % 2 + 1))

# 5. Type comment
agent-browser --cdp $CDP_PORT fill @[COMMENT_INPUT] "[INSIGHTFUL_COMMENT]"
sleep $((RANDOM % 3 + 2))

# 6. Post comment
agent-browser --cdp $CDP_PORT click @[POST_BUTTON]
sleep $((RANDOM % 90 + 60))  # 60-150 seconds before next
```

---

## Growth Targets & Timelines

### Realistic Growth Expectations

| Starting Point | 30-Day Target | 90-Day Target | Strategy Focus |
|----------------|---------------|---------------|----------------|
| 0-500 | +200-400 | +1,000-2,000 | Niche establishment |
| 500-2K | +300-600 | +1,500-3,000 | Strategic engagement |
| 2K-10K | +500-1,000 | +3,000-6,000 | Content + engagement |
| 10K+ | +1,000-2,000 | +5,000-10,000 | Scale what works |

### Account Warm-Up Schedule

```
NEW ACCOUNT WARM-UP:
━━━━━━━━━━━━━━━━━━━━

Week 1:
- 5-10 replies/day
- 10-20 likes/day
- 1-2 posts/day
- 3-5 follows/day

Week 2:
- 10-15 replies/day
- 20-30 likes/day
- 2-3 posts/day
- 5-10 follows/day

Week 3:
- 15-20 replies/day
- 30-50 likes/day
- 3-5 posts/day
- 10-15 follows/day

Week 4+:
- Full daily limits
```

---

## Output Format

When invoked, the agent provides:

```
GROWTH AGENT SESSION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━

GOAL: [Specific growth goal]
PLATFORM: [X/LinkedIn/Instagram]
CURRENT FOLLOWERS: [N]
TARGET: [N] by [date]

TODAY'S SESSION:
━━━━━━━━━━━━━━━━

Morning (30 min):
1. [Action] → [Target account]
   ⏱️ Wait 45-90 sec
2. [Action] → [Target account]
   ⏱️ Wait 45-90 sec
[...]

Midday (15 min):
1. [Action]
2. [Action]
[...]

Evening (20 min):
1. [Action]
2. [Action]
[...]

AGENT-BROWSER COMMANDS:
[Ready-to-execute command sequence]

DAILY LIMITS:
- Replies: [N]/[max]
- Likes: [N]/[max]
- Follows: [N]/[max]

SAFETY CHECKS:
✓ Random timing variance
✓ Action type mixing
✓ Session breaks included
```

---

## Sources

### Research
- [X Algorithm Decoded 2025](https://www.markmorphew.com/strategies-to-grow-your-twitter-x-followers/)
- [LinkedIn Algorithm 2026](https://www.agorapulse.com/blog/linkedin/linkedin-algorithm-2025/)
- [Instagram Algorithm 2026](https://buffer.com/resources/instagram-algorithms/)
- [Twitter Growth Hacks 2025](https://typefully.com/blog/twitter-growth-hacking-tips)
- [Organic Social Media Growth](https://sproutsocial.com/insights/organic-social-media-growth/)

### Key Insights
- 70/30 rule: Engage more than you post
- First 30 minutes of engagement are critical
- Quality replies > quantity of posts
- Niche authority > broad reach
- Human-like timing is essential
