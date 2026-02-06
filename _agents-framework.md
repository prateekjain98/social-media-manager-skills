# Goal-Based Agents Framework

A framework for creating autonomous agents that pursue specific social media objectives.

---

## What is a Goal-Based Agent?

A goal-based agent is an autonomous system that:

1. **Pursues a specific, measurable objective**
2. **Executes strategies** to achieve that objective
3. **Adapts** based on results
4. **Operates safely** within platform limits

Unlike simple automation scripts, goal-based agents:
- Make decisions based on context
- Track progress toward goals
- Adjust strategies when things aren't working
- Maintain human-like behavior patterns

---

## Agent Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         GOAL-BASED AGENT                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                         GOAL                                 │   │
│  │  "Specific, Measurable, Time-bound objective"               │   │
│  │  Example: "Grow X followers from 1K to 5K in 90 days"       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      STRATEGY LAYER                          │   │
│  │                                                              │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │   │
│  │  │ Strategy A   │ │ Strategy B   │ │ Strategy C   │        │   │
│  │  │ (Primary)    │ │ (Secondary)  │ │ (Tertiary)   │        │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘        │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    EXECUTION ENGINE                          │   │
│  │                                                              │   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────┐ │   │
│  │  │ Session    │ │ Action     │ │ Timing     │ │ Progress │ │   │
│  │  │ Planner    │ │ Sequencer  │ │ Controller │ │ Tracker  │ │   │
│  │  └────────────┘ └────────────┘ └────────────┘ └──────────┘ │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      SAFETY LAYER                            │   │
│  │                                                              │   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────┐ │   │
│  │  │ Rate       │ │ Detection  │ │ Behavioral │ │ Recovery │ │   │
│  │  │ Limiter    │ │ Avoidance  │ │ Variance   │ │ Protocol │ │   │
│  │  └────────────┘ └────────────┘ └────────────┘ └──────────┘ │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Defining an Agent

### Agent Definition Template

```yaml
agent:
  name: "[Agent Name]"
  version: "1.0"

goal:
  objective: "[What the agent is trying to achieve]"
  metric: "[How success is measured]"
  target: "[Specific number/outcome]"
  timeframe: "[Duration]"

platforms:
  - name: "[Platform]"
    account: "[Account handle]"
    current_state: "[Starting metrics]"

strategies:
  primary:
    name: "[Strategy name]"
    description: "[What it does]"
    actions:
      - "[Action 1]"
      - "[Action 2]"
    daily_quota: "[Max actions/day]"

  secondary:
    name: "[Strategy name]"
    description: "[What it does]"
    actions:
      - "[Action 1]"
    daily_quota: "[Max actions/day]"

schedule:
  sessions_per_day: 3
  session_times:
    - "08:00-08:45"
    - "12:00-12:20"
    - "18:00-18:30"
  rest_days: ["Sunday"]

safety:
  rate_limits:
    follows_per_day: 30
    likes_per_day: 100
    comments_per_day: 50
    dms_per_day: 20

  timing:
    min_action_gap: 30  # seconds
    max_action_gap: 120  # seconds
    session_cooldown: 7200  # 2 hours

  detection_avoidance:
    random_timing: true
    action_mixing: true
    natural_breaks: true
    skip_days: true

tracking:
  metrics:
    - "follower_count"
    - "engagement_rate"
    - "profile_visits"
  log_frequency: "daily"
  review_frequency: "weekly"
```

---

## Available Agent Types

### 1. Growth Agent (`/growth-agent`)
**Goal**: Increase follower count
**Strategies**: Strategic replies, content posting, profile optimization
**Platforms**: X, LinkedIn, Instagram

### 2. Lead Generation Agent (Planned)
**Goal**: Find and qualify potential customers
**Strategies**: Search monitoring, engagement, DM outreach
**Platforms**: X, LinkedIn, Reddit

### 3. Brand Awareness Agent (Planned)
**Goal**: Increase brand mentions and visibility
**Strategies**: Content distribution, influencer engagement, trend participation
**Platforms**: All

### 4. Community Building Agent (Planned)
**Goal**: Build engaged community
**Strategies**: Response management, UGC encouragement, relationship building
**Platforms**: All

### 5. Content Distribution Agent (Planned)
**Goal**: Maximize content reach
**Strategies**: Cross-posting, repurposing, optimal timing
**Platforms**: All

---

## Execution Engine Components

### 1. Session Planner

Determines what actions to take during each session.

```
SESSION PLANNING LOGIC:
━━━━━━━━━━━━━━━━━━━━━━━

1. Check remaining daily quotas
2. Identify highest-priority actions
3. Distribute actions across session duration
4. Add buffer time for responses/reactions
5. Include natural scrolling/reading time
```

### 2. Action Sequencer

Orders actions to appear human-like.

```
ACTION SEQUENCING RULES:
━━━━━━━━━━━━━━━━━━━━━━━━

✓ Never do same action type 5+ times in a row
✓ Mix engagement types (like, comment, follow)
✓ Include passive actions (scroll, read)
✓ Respond to notifications mid-session
✓ Vary action intensity throughout session
```

### 3. Timing Controller

Ensures human-like timing patterns.

```
TIMING PATTERNS:
━━━━━━━━━━━━━━━━

Action Type      | Min Wait | Max Wait | Distribution
─────────────────|----------|----------|─────────────
Reply            | 45s      | 120s     | Normal
Like             | 15s      | 45s      | Uniform
Follow           | 60s      | 180s     | Normal
Comment          | 60s      | 150s     | Normal
Read/Scroll      | 3s       | 15s      | Uniform
Profile Visit    | 5s       | 20s      | Normal
```

### 4. Progress Tracker

Monitors goal progress and adjusts strategies.

```
TRACKING METRICS:
━━━━━━━━━━━━━━━━━

Daily:
- Actions completed vs. quota
- Engagement received
- New followers gained
- Profile visits

Weekly:
- Net follower growth
- Engagement rate change
- Best performing content
- Strategy effectiveness

Monthly:
- Goal progress percentage
- ROI on time invested
- Strategy adjustments needed
```

---

## Safety Layer Components

### 1. Rate Limiter

Enforces platform-safe action limits.

```
CONSERVATIVE DAILY LIMITS:
━━━━━━━━━━━━━━━━━━━━━━━━━━

Platform    | Follows | Likes  | Comments | DMs
────────────|---------|--------|----------|────
X           | 30-50   | 100    | 50       | 20
LinkedIn    | 30-50   | 100    | 30       | 25
Instagram   | 30-50   | 100    | 50       | 20

Note: Start at 50% of these limits for new accounts
```

### 2. Detection Avoidance

Prevents patterns that trigger bot detection.

```
ANTI-DETECTION MEASURES:
━━━━━━━━━━━━━━━━━━━━━━━━

✓ Random timing variance (±30% of base)
✓ Gaussian distribution for delays
✓ Session time variation (±15 min)
✓ Occasional typos (then correction)
✓ Incomplete sessions (sometimes)
✓ Skip days randomly (1-2 per week)
✓ Activity during human hours only
✓ Geographic consistency (IP = timezone)
```

### 3. Behavioral Variance

Injects human-like inconsistencies.

```
VARIANCE INJECTION:
━━━━━━━━━━━━━━━━━━

- Some days do 70% of quota, some 110%
- Occasionally abandon session midway
- Sometimes scroll without engaging
- Random breaks mid-session
- Variable message lengths
- Different emoji usage patterns
```

### 4. Recovery Protocol

Handles rate limiting and blocks.

```
RECOVERY PROCEDURES:
━━━━━━━━━━━━━━━━━━━━

IF soft_limit_warning:
  → Reduce activity by 50% for 24h
  → Skip next scheduled session

IF action_blocked:
  → Stop all automation for 24-48h
  → Resume at 25% capacity

IF account_restricted:
  → Full stop for 7 days
  → Manual activity only
  → Gradual ramp-up over 2 weeks

IF account_suspended:
  → Appeal if possible
  → Wait for resolution
  → Never admit to automation
```

---

## Creating a New Agent

### Step 1: Define the Goal

```
SMART GOAL FORMAT:
━━━━━━━━━━━━━━━━━━

Specific: What exactly do you want to achieve?
Measurable: How will you measure success?
Achievable: Is this realistic with your resources?
Relevant: Does this align with broader objectives?
Time-bound: When should this be achieved?

Example:
"Grow X account from 1,000 to 5,000 followers
in 90 days by engaging with web development
Twitter to establish authority in JavaScript
ecosystem."
```

### Step 2: Identify Strategies

```
STRATEGY SELECTION:
━━━━━━━━━━━━━━━━━━

For follower growth:
├── Strategic reply engagement (Primary)
├── Quality content posting (Secondary)
├── Profile optimization (Foundation)
└── Follower engagement (Retention)

For lead generation:
├── Search monitoring (Primary)
├── Engagement with prospects (Secondary)
├── DM outreach (Tertiary)
└── Content that attracts leads (Foundation)
```

### Step 3: Set Up Execution

```
EXECUTION SETUP:
━━━━━━━━━━━━━━━━

1. Create schedule (sessions/times)
2. Set daily quotas
3. Define action sequences
4. Configure timing parameters
5. Set up tracking
```

### Step 4: Configure Safety

```
SAFETY CONFIGURATION:
━━━━━━━━━━━━━━━━━━━━━

1. Set conservative rate limits
2. Enable variance injection
3. Configure detection avoidance
4. Set up recovery triggers
5. Plan for manual intervention
```

### Step 5: Launch & Monitor

```
LAUNCH CHECKLIST:
━━━━━━━━━━━━━━━━━

□ Browser profile set up
□ Account authenticated
□ Fingerprint verified (bot.sannysoft.com)
□ First session at 25% capacity
□ Monitoring dashboard ready
□ Recovery plan documented
```

---

## Agent Coordination

When running multiple agents:

```
MULTI-AGENT RULES:
━━━━━━━━━━━━━━━━━━

1. One agent per platform at a time
2. Different sessions (not simultaneous)
3. Shared safety limits
4. Centralized logging
5. Priority ordering for conflicts

Example Schedule:
━━━━━━━━━━━━━━━━━

08:00-09:00  → X Growth Agent
10:00-10:30  → LinkedIn Engagement Agent
12:00-12:30  → X Growth Agent (Session 2)
14:00-14:30  → Instagram Growth Agent
18:00-18:45  → X Growth Agent (Session 3)
19:00-19:30  → LinkedIn Engagement Agent (Session 2)
```

---

## Integration with Agent-Browser

All agents use agent-browser for execution:

```bash
# Agent startup
agent-browser connect 9222  # Connect to Chrome CDP

# Agent session
agent-browser open "[url]"
agent-browser snapshot -i
agent-browser click @[ref]
agent-browser fill @[ref] "[text]"
# ... execute action sequence

# Agent tracking
agent-browser screenshot progress-$(date +%Y%m%d).png
```

---

## Future Agent Types

Planned agents for the social media manager:

| Agent | Goal | Status |
|-------|------|--------|
| Growth Agent | Grow followers | ✅ Implemented |
| Lead Gen Agent | Find customers | 📋 Planned |
| Brand Agent | Build awareness | 📋 Planned |
| Community Agent | Build engagement | 📋 Planned |
| Distribution Agent | Maximize reach | 📋 Planned |
| Monitoring Agent | Track mentions | 📋 Planned |
| Response Agent | Handle replies | 📋 Planned |
| Analytics Agent | Report insights | 📋 Planned |

---

## Best Practices

1. **Start conservative** - Begin at 25-50% of limits
2. **Ramp gradually** - Increase over 2-4 weeks
3. **Monitor closely** - Watch for warnings
4. **Mix manual + auto** - 50/50 is safest
5. **Document everything** - Log all sessions
6. **Review weekly** - Adjust strategies
7. **Have backup** - Prepare for restrictions
8. **Stay updated** - Platform rules change
