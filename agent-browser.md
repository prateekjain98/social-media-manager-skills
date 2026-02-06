# Agent Browser Connection

Connect to a browser instance for automated social media interactions using Chrome DevTools Protocol (CDP) while evading bot detection.

## Skill: `/agent-browser`

**CRITICAL: Read `_core-principles.md` first. All automated interactions must appear human-like. Never reveal automation to platforms or users.**

---

## Why Agent Browser?

Manual social media tasks are time-consuming. Agent browser allows you to:
- **Search for leads** on social platforms
- **Follow accounts** programmatically
- **Like and engage** with content
- **Monitor conversations** in real-time
- **Execute outreach** at scale

The key: **Native Chrome with proper anti-detection flags** minimizes automation fingerprints.

---

## How Platforms Detect Bots

Understanding detection is crucial for evasion. Platforms use multi-layered approaches:

### 1. Browser Fingerprinting

Platforms check for automation indicators:

| Attribute | What They Check | Bot Signal |
|-----------|-----------------|------------|
| `navigator.webdriver` | Set to `true` by automation tools | Primary detection flag |
| User-Agent | Contains "HeadlessChrome" | Instant detection |
| `navigator.plugins` | Empty list | Suspiciously minimal |
| `navigator.languages` | Missing or empty | Automation indicator |
| WebGL renderer | Missing or generic | Headless browser |
| Screen resolution | Unusual dimensions | Virtual environment |
| Timezone | Mismatch with IP location | Proxy/VPN detection |

### 2. CDP (Chrome DevTools Protocol) Detection

All major automation libraries (Puppeteer, Playwright, Selenium) use CDP's `Runtime.Enable` command. Modern anti-bot systems detect this protocol-level signature.

**Solution**: Use real Chrome with `--user-data-dir` instead of headless browsers. Native Chrome doesn't have CDP detection artifacts.

### 3. Behavioral Analysis

Platforms analyze interaction patterns:

| Human Behavior | Bot Behavior |
|----------------|--------------|
| 10-50 events/second | 200+ events/second |
| Gaussian mouse movement (300-400px avg) | Bimodal distribution (jumps) |
| Curved, erratic mouse paths | Linear, direct movements |
| Variable timing (10-60ms variance) | Precise, identical timing |
| Scrolls before clicking | Instant clicks without context |
| Typos and corrections | Perfect typing |
| Session breaks and pauses | Continuous activity |

### 4. Network Analysis

- Data center IP addresses
- Known proxy/VPN ranges
- Unusual geographic patterns
- API call velocity

---

## Platform-Specific Detection Methods

### X (Twitter)

X uses behavioral fingerprints analyzing:
- Speed of actions
- Repetition patterns
- API call sequences
- Session history
- IP volatility
- Engagement context

**What triggers detection**:
- Following 50+ accounts in 10 minutes
- Identical reply text to multiple users
- Liking posts faster than humanly possible
- Activity during unusual hours for your timezone

### LinkedIn

LinkedIn employs aggressive client-side fingerprinting:
- Detects browser extensions
- Monitors DOM mutations
- Checks for automation-injected elements
- Tracks JavaScript globals
- Monitors patched APIs

**What triggers detection**:
- Connection requests > 100/day
- Profile views at inhuman speed
- Identical messages to connections
- Scraping patterns (rapid page loads)

### Instagram/Meta

Instagram uses sophisticated detection:
- Network analysis (data center detection)
- Device fingerprinting (unique identifier per device)
- Behavioral models (speed, repetition, session patterns)
- Cross-account correlation

**What triggers detection**:
- Mass following/unfollowing
- Rapid liking across many posts
- Generic automated comments
- Activity from known bot IP ranges

---

## Anti-Detection Setup

### Step 1: Launch Chrome with Stealth Flags

```bash
# macOS - Full anti-detection launch
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-agent-profile \
  --disable-blink-features=AutomationControlled \
  --disable-features=IsolateOrigins,site-per-process \
  --disable-site-isolation-trials \
  --disable-web-security \
  --no-first-run \
  --no-default-browser-check \
  --disable-infobars \
  --window-size=1920,1080 \
  --start-maximized

# Linux
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-agent-profile \
  --disable-blink-features=AutomationControlled \
  --disable-features=IsolateOrigins,site-per-process \
  --no-first-run \
  --window-size=1920,1080

# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" ^
  --remote-debugging-port=9222 ^
  --user-data-dir=C:\Temp\chrome-agent-profile ^
  --disable-blink-features=AutomationControlled ^
  --disable-features=IsolateOrigins,site-per-process ^
  --no-first-run ^
  --window-size=1920,1080
```

### Key Anti-Detection Flags Explained

| Flag | Purpose |
|------|---------|
| `--disable-blink-features=AutomationControlled` | Hides `navigator.webdriver=true` |
| `--user-data-dir` | Creates real profile (not headless) |
| `--no-first-run` | Skips first-run dialogs |
| `--disable-infobars` | Removes "Chrome is being controlled" bar |
| `--window-size=1920,1080` | Normal screen resolution |

### Step 2: Verify Stealth

After launching, check your fingerprint:

```bash
# Open fingerprint test
agent-browser --cdp 9222 open "https://bot.sannysoft.com"

# Or
agent-browser --cdp 9222 open "https://abrahamjuliot.github.io/creepjs/"
```

Look for:
- `navigator.webdriver`: Should be `undefined` or `false`
- No "HeadlessChrome" in User-Agent
- Plugins list should show PDF viewer, etc.
- WebGL should show real GPU info

### Step 3: Authenticate Manually

1. Navigate to your target platform in the Chrome window
2. Log in with real credentials
3. Complete 2FA if prompted
4. Your authenticated session is now usable

### Step 4: Connect Agent Browser

```bash
# Verify connection
agent-browser --cdp 9222 snapshot

# If successful, you'll see the page DOM structure
```

---

## Human-Like Mouse Movement

### Why It Matters

Bot detection systems analyze mouse patterns extensively:
- **Human**: Curved paths with Bezier trajectories, micro-corrections, variable speed
- **Bot**: Linear paths, instant teleportation, constant velocity

### Movement Characteristics to Emulate

```
HUMAN MOUSE MOVEMENT PATTERNS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Trajectory:
- Curved paths using Bezier curves
- Slight overshoot then correction
- Acceleration at start, deceleration at end

Speed Variation:
- Start slow → accelerate → decelerate → stop
- 300-400 pixel average displacement
- Never perfectly constant velocity

Micro-Movements:
- Random jitter (±2.5 pixels)
- Small corrections mid-path
- Occasional pause during movement

Timing:
- 10-60ms random delays between movements
- Pause before clicking (200-500ms)
- Variable hold time on clicks (50-150ms)
```

### Implementation Approach

When using agent-browser, mentally add these patterns:

1. **Before clicking**: Pause 200-500ms (humans read before clicking)
2. **Between actions**: Random 2-10 second delays
3. **Scrolling**: Scroll in view before clicking elements
4. **Typing**: Variable speed, occasional backspace

---

## Behavioral Evasion Rules

### Timing Patterns

```
ACTION TIMING GUIDELINES:
━━━━━━━━━━━━━━━━━━━━━━━━

Between page loads: 3-8 seconds
Between clicks: 1-3 seconds
Between follows: 30-90 seconds
Between likes: 10-30 seconds
Between messages: 2-5 minutes
Session length: 15-45 minutes
Break between sessions: 1-4 hours
```

### Activity Windows

Match normal human hours for your timezone:
- **Active hours**: 8am-11pm local time
- **Peak activity**: 9am-12pm, 7pm-10pm
- **Avoid**: 2am-6am (suspicious)

### Session Behavior

```
REALISTIC SESSION PATTERN:
━━━━━━━━━━━━━━━━━━━━━━━━━

1. Open platform
2. Scroll feed for 30-60 seconds (reading)
3. Like 2-3 posts (random intervals)
4. View 1-2 profiles
5. Maybe follow 1 person
6. Check notifications
7. Scroll more
8. Engage with 1-2 posts
9. Pause/break
10. Repeat or end session
```

### Daily Limits (Conservative)

| Platform | Action | Safe Daily Limit | Spacing |
|----------|--------|------------------|---------|
| X | Follows | 30-50 | 30-90 sec each |
| X | Likes | 50-100 | 10-30 sec each |
| X | DMs | 10-20 | 2-5 min each |
| X | Replies | 20-30 | 1-3 min each |
| LinkedIn | Connections | 30-50 | 1-2 min each |
| LinkedIn | Messages | 15-25 | 3-5 min each |
| Instagram | Follows | 30-50 | 30-90 sec each |
| Instagram | Likes | 50-100 | 10-30 sec each |

---

## Installation

```bash
# NPM (Recommended)
npm install -g agent-browser
agent-browser install  # Download Chromium

# Linux dependencies
agent-browser install --with-deps
```

---

## Complete Command Reference

*Official commands from [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)*

### Connection Methods

```bash
# Method 1: Pass --cdp on each command
agent-browser --cdp 9222 open "https://x.com"
agent-browser --cdp 9222 snapshot

# Method 2: Connect once, then run commands without --cdp
agent-browser connect 9222
agent-browser open "https://x.com"
agent-browser snapshot

# Method 3: Use persistent profile
agent-browser --profile ~/.myapp-profile open "https://x.com"
```

### Navigation Commands

```bash
agent-browser open <url>           # Navigate to URL (aliases: goto, navigate)
agent-browser back                 # Go back
agent-browser forward              # Go forward
agent-browser reload               # Reload page
agent-browser close                # Close browser
```

### Snapshot (Critical for AI)

```bash
agent-browser snapshot             # Get accessibility tree with refs
agent-browser snapshot -i          # Interactive elements only with refs (@e1, @e2)
agent-browser snapshot -i -C       # Include cursor-interactive elements
agent-browser snapshot -s "#selector"  # Scope to CSS selector
```

**Output format**: Elements marked with `@e1`, `@e2`, etc. for direct targeting.

### Element Interaction

```bash
# Clicking
agent-browser click @e1            # Click element by ref
agent-browser dblclick @e1         # Double-click
agent-browser click "#submit"      # Click by CSS selector

# Text Input
agent-browser fill @e2 "text"      # Clear field and type (recommended)
agent-browser type @e2 "text"      # Type without clearing
agent-browser press Enter          # Press key (Enter, Tab, Escape, etc.)

# Form Controls
agent-browser select @e1 "option"  # Select dropdown option
agent-browser check @e1            # Check checkbox
agent-browser uncheck @e1          # Uncheck checkbox

# Mouse Actions
agent-browser hover @e1            # Hover over element
agent-browser focus @e1            # Focus element
agent-browser drag @src @tgt       # Drag and drop
agent-browser upload @e1 file.pdf  # Upload file
agent-browser scrollintoview @e1   # Scroll element into view
```

### Semantic Locators (AI-Friendly)

Find elements using human-readable criteria:

```bash
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "user@test.com"
agent-browser find role button click --name "Submit"
agent-browser find placeholder "Search" type "query"
agent-browser find alt "Logo" click
agent-browser find testid "submit-btn" click
agent-browser find first ".item" click
agent-browser find nth 2 "a" text
```

### Scrolling

```bash
agent-browser scroll down 500      # Scroll down 500px
agent-browser scroll up 300        # Scroll up 300px
agent-browser scroll left 200      # Scroll left
agent-browser scroll right 200     # Scroll right
```

### Information Retrieval

```bash
agent-browser get text @e1         # Get text content
agent-browser get html @e1         # Get innerHTML
agent-browser get value @e1        # Get input value
agent-browser get attr @e1 href    # Get attribute
agent-browser get title            # Get page title
agent-browser get url              # Get current URL
agent-browser get count ".items"   # Count matching elements
agent-browser get box @e1          # Get bounding box
```

### State Checking

```bash
agent-browser is visible @e1       # Check visibility
agent-browser is enabled @e1       # Check if enabled
agent-browser is checked @e1       # Check if checked
```

### Wait Commands

```bash
agent-browser wait @e1             # Wait for element visible
agent-browser wait 2000            # Wait milliseconds
agent-browser wait --text "Welcome"    # Wait for text
agent-browser wait --url "**/dashboard"  # Wait for URL pattern
agent-browser wait --load networkidle   # Wait for network idle
agent-browser wait --fn "window.ready"  # Wait for JS condition
```

### Mouse Control (Advanced)

```bash
agent-browser mouse move 100 200   # Move to coordinates
agent-browser mouse down           # Press left button
agent-browser mouse down right     # Press right button
agent-browser mouse up             # Release button
agent-browser mouse wheel 100      # Scroll wheel
```

### Screenshots & Export

```bash
agent-browser screenshot           # Screenshot to temp dir
agent-browser screenshot page.png  # Screenshot to file
agent-browser screenshot --full    # Full page screenshot
agent-browser pdf output.pdf       # Export as PDF
```

### Tabs & Windows

```bash
agent-browser tab                  # List all tabs
agent-browser tab new              # New tab
agent-browser tab new "https://x.com"  # New tab with URL
agent-browser tab 2                # Switch to tab 2
agent-browser tab close            # Close current tab
agent-browser tab close 2          # Close tab 2
agent-browser window new           # New window
```

### Frames (iframes)

```bash
agent-browser frame "#iframe-id"   # Switch to iframe
agent-browser frame main           # Back to main frame
```

### Dialogs

```bash
agent-browser dialog accept        # Accept dialog
agent-browser dialog accept "text" # Accept with input
agent-browser dialog dismiss       # Dismiss dialog
```

### Cookies Management

```bash
agent-browser cookies              # Get all cookies
agent-browser cookies set name value  # Set cookie
agent-browser cookies clear        # Clear all cookies
```

### Storage Management

```bash
agent-browser storage local        # Get all localStorage
agent-browser storage local key    # Get specific key
agent-browser storage local set key value  # Set value
agent-browser storage local clear  # Clear localStorage
agent-browser storage session      # Same for sessionStorage
```

### Network Control

```bash
agent-browser network requests     # View requests
agent-browser network requests --filter api  # Filter requests
agent-browser network route <url>  # Intercept URL
agent-browser network route <url> --abort  # Block URL
agent-browser network route <url> --body '{"mocked":true}'  # Mock response
agent-browser network unroute      # Remove all routes
```

### Browser Settings

```bash
agent-browser set viewport 1920 1080   # Set viewport size
agent-browser set device "iPhone 14"   # Emulate device
agent-browser set geo 40.7128 -74.0060 # Set geolocation
agent-browser set offline on          # Enable offline mode
agent-browser set offline off         # Disable offline mode
agent-browser set headers '{"X-Custom":"value"}'  # Set headers
agent-browser set credentials user pass  # Set HTTP auth
agent-browser set media dark           # Set color scheme
```

### State & Sessions

```bash
# Save/load authentication state
agent-browser state save auth.json     # Save cookies, localStorage, etc.
agent-browser state load auth.json     # Load saved state

# Multiple isolated sessions
agent-browser --session agent1 open "https://x.com"
agent-browser --session agent2 open "https://linkedin.com"
agent-browser session list             # List active sessions
agent-browser session                  # Show current session
```

### Debugging

```bash
agent-browser console              # View console messages
agent-browser console --clear      # Clear console
agent-browser errors               # View page errors
agent-browser errors --clear       # Clear errors
agent-browser highlight @e1        # Highlight element
agent-browser trace start          # Start recording trace
agent-browser trace stop           # Stop and save trace
agent-browser eval "document.title"  # Run JavaScript
```

### Visual Mode

```bash
agent-browser --headed open "https://x.com"  # Show browser window
agent-browser record start demo.webm         # Record video
agent-browser record stop                    # Stop recording
```

### Mobile Testing (iOS Simulator)

```bash
agent-browser -p ios --device "iPhone 16 Pro" open "https://x.com"
agent-browser -p ios tap @e1       # Tap element
agent-browser -p ios swipe up      # Swipe gesture
```

---

## Core Workflow Pattern

The fundamental workflow for AI agents:

```bash
# 1. Navigate
agent-browser --cdp 9222 open "https://x.com"

# 2. Snapshot (get element refs)
agent-browser --cdp 9222 snapshot -i

# 3. Interact using refs
agent-browser --cdp 9222 click @e5
agent-browser --cdp 9222 fill @e8 "search query"

# 4. Re-snapshot after page changes (refs invalidate)
agent-browser --cdp 9222 snapshot -i

# 5. Continue workflow
```

**Important**: Refs (`@e1`, `@e2`) are invalidated when the page changes. Always re-snapshot after navigation or clicks that load new content.

---

## Social Media Use Cases

### 1. Lead Generation on X (Twitter)

```bash
# Search for people needing services
agent-browser --cdp 9222 open "https://x.com/search?q=%22need%20a%20website%22%20OR%20%22looking%20for%20developer%22&f=live"

# Wait 3-5 seconds (human reading time)
# Take snapshot to analyze results
agent-browser --cdp 9222 snapshot

# Navigate to a profile
agent-browser --cdp 9222 open "https://x.com/username"
```

### 2. Following Accounts

```bash
# Navigate to profile
agent-browser --cdp 9222 open "https://x.com/targetuser"

# Wait 2-4 seconds (human reading profile)

# Snapshot to find follow button reference
agent-browser --cdp 9222 snapshot

# Wait 1-2 seconds

# Click follow button (use the ref from snapshot)
agent-browser --cdp 9222 click e42

# Wait 30-90 seconds before next follow
```

### 3. Liking Posts

```bash
# Scroll to view post (important for detection)
# Find like button in snapshot
agent-browser --cdp 9222 snapshot

# Wait 0.5-2 seconds

# Click the like button reference
agent-browser --cdp 9222 click e28

# Wait 10-30 seconds before next like
```

### 4. LinkedIn Lead Search

```bash
# Search for decision makers
agent-browser --cdp 9222 open "https://linkedin.com/search/results/people/?keywords=marketing%20director"

# Wait 4-6 seconds

# Snapshot results
agent-browser --cdp 9222 snapshot
```

---

## Search Query Patterns

### Finding Potential Clients

| Platform | Search Query | Purpose |
|----------|--------------|---------|
| X | `"need a website" OR "looking for developer"` | Web dev leads |
| X | `"hiring social media" OR "need social manager"` | SMM leads |
| X | `"looking for designer" OR "need logo"` | Design leads |
| LinkedIn | `"we're hiring" marketing` | Job opportunities |

### URL Encoding

Spaces and special characters must be encoded:
- Space → `%20`
- Quote → `%22`
- OR stays as `OR`
- Ampersand → `%26`

Example:
```
"I need a website" OR "looking for developer"
↓
%22I%20need%20a%20website%22%20OR%20%22looking%20for%20developer%22
```

---

## Red Flags That Trigger Detection

### Instant Detection

- Following 100+ accounts in an hour
- Liking 200+ posts in an hour
- Sending identical messages to many users
- Activity at 3am local time
- Actions from data center IPs

### Pattern Detection

- Exactly 5 seconds between every action
- Perfect click accuracy (no missed clicks ever)
- No scrolling before interacting
- Same sequence of actions every session
- Linear mouse movements (teleportation)

### Fingerprint Detection

- `navigator.webdriver = true`
- "HeadlessChrome" in User-Agent
- Missing plugins/languages
- Screen resolution 800x600 (virtual)
- Timezone mismatch with IP

---

## Advanced Evasion Techniques

### 1. IP Rotation

If getting blocked frequently:
- Use residential proxies (not data center)
- Rotate IPs every session
- Match IP location to account timezone

### 2. Session Isolation

```bash
# Create separate profiles per account
--user-data-dir=/tmp/chrome-profile-account1
--user-data-dir=/tmp/chrome-profile-account2
```

### 3. Fingerprint Consistency

Ensure these match:
- Timezone = IP location = Account location
- Language settings = Expected for region
- Screen resolution = Common desktop size

### 4. Warm-Up New Accounts

New accounts need gradual ramp-up:

```
Week 1: 5-10 follows/day, 10-20 likes/day
Week 2: 10-20 follows/day, 20-40 likes/day
Week 3: 20-30 follows/day, 40-60 likes/day
Week 4+: Normal limits
```

### 5. Mix Manual + Automated

Best practice:
- 50% manual activity
- 50% automated activity
- Automated tasks during consistent hours
- Manual engagement adds authenticity

---

## Workflow: Full Lead Generation Cycle

### Step 1: Setup Stealth Session
```bash
# Launch Chrome with anti-detection flags
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-agent-profile \
  --disable-blink-features=AutomationControlled \
  --no-first-run \
  --window-size=1920,1080
```

### Step 2: Verify Fingerprint
```bash
# Check you're not detected
agent-browser --cdp 9222 open "https://bot.sannysoft.com"
```

### Step 3: Authenticate (Manual)
- Log into X, LinkedIn, etc. in the Chrome window
- Complete any verification
- Browse naturally for 1-2 minutes

### Step 4: Search for Leads
```bash
# Find people requesting services
agent-browser --cdp 9222 open "https://x.com/search?q=%22need%20a%20website%22&f=live"

# Wait 3-5 seconds
agent-browser --cdp 9222 snapshot
```

### Step 5: Analyze & Qualify
Review snapshot output for:
- Post content (what they need)
- Engagement (replies, likes, views)
- Recency (when posted)
- Profile info (legit potential client?)

### Step 6: Engage (With Delays)
```bash
# Follow promising leads (30-90 sec between follows)
agent-browser --cdp 9222 open "https://x.com/leadusername"
# Wait 2-4 seconds
# Click follow button

# Like their posts (10-30 sec between likes)
# Scroll first, then click

# Consider a thoughtful reply
# Wait 2-5 minutes between replies
```

### Step 7: Track Results
Keep a spreadsheet of:
- Leads found
- Actions taken
- Responses received
- Conversions

---

## Output Format

When invoked, provide browser automation guidance:

```
AGENT BROWSER SETUP
━━━━━━━━━━━━━━━━━━━━━━━━

TASK: [What you want to accomplish]

SETUP COMMANDS:
[Chrome launch command with anti-detection flags]

FINGERPRINT CHECK:
[Verify stealth at bot.sannysoft.com]

WORKFLOW:
1. [Step with command]
   ⏱️ Wait X seconds
2. [Step with command]
   ⏱️ Wait X seconds
3. [Step with command]

SEARCH QUERIES:
[Relevant encoded search URLs]

TIMING GUIDELINES:
[Specific delays for this task]

DAILY LIMITS:
[Safe limits for actions involved]
```

---

## Troubleshooting

### Chrome Won't Bind to Port
```bash
# Check if port is in use
lsof -i :9222

# Kill existing Chrome processes
pkill -f "Chrome.*remote-debugging"

# Try again with fresh profile
rm -rf /tmp/chrome-agent-profile
```

### Connection Refused
- Ensure Chrome launched with `--remote-debugging-port=9222`
- Verify `--user-data-dir` points to a writable directory
- Check no firewall blocking localhost:9222

### Platform Blocking Actions
- You're moving too fast—increase delays
- Take a 24-48 hour break
- Clear cookies and re-authenticate
- Use different user-data-dir for fresh fingerprint
- Check your IP isn't flagged

### Detected as Bot
- Verify fingerprint at bot.sannysoft.com
- Ensure `--disable-blink-features=AutomationControlled` is set
- Check `navigator.webdriver` returns `undefined`
- Slow down significantly
- Add more human-like timing variance

---

## Security Notes

- **Never share your user-data-dir** - contains session cookies
- **Use separate profiles** for automation vs. personal browsing
- **Monitor for unusual activity** on your accounts
- **Have backup accounts** in case of suspension
- **Don't automate policy-violating actions**
- **Residential IPs** are safer than data center IPs
- **Warm up accounts** before heavy automation

---

## Sources & Further Reading

### Agent Browser Official
- [agent-browser GitHub](https://github.com/vercel-labs/agent-browser) - Official repository
- [agent-browser.dev](https://agent-browser.dev/) - Official website
- [SKILL.md](https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/SKILL.md) - Official skill documentation

### Anti-Detection Research
- [Bot Detection Methods](https://fingerprint.com/blog/bot-detection/)
- [CDP Detection Evasion](https://blog.castle.io/from-puppeteer-stealth-to-nodriver-how-anti-detect-frameworks-evolved-to-evade-bot-detection/)
- [LinkedIn Bot Detection](https://blog.castle.io/detecting-browser-extensions-for-bot-detection-lessons-from-linkedin-and-castle/)
- [Mouse Movement Patterns](https://github.com/sarperavci/human_mouse)
- [Browser Fingerprinting](https://www.browserless.io/blog/device-fingerprinting)
- [Navigator.webdriver Evasion](https://www.zenrows.com/blog/navigator-webdriver)
