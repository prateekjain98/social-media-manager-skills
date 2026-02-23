# Agent Browser Connection

Connect to a browser instance for automated social media interactions using Chrome DevTools Protocol (CDP) or Safari via AppleScript while evading bot detection. Supports both Chrome and Safari on macOS.

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

The key: **Native Chrome with proper anti-detection flags** or **Real Safari via AppleScript** minimizes automation fingerprints.

### Browser Choice: Chrome vs Safari

| Factor | Chrome (CDP) | Safari (AppleScript) |
|--------|-------------|---------------------|
| Stealth ecosystem | Mature (many stealth tools) | Not needed (real browser, zero automation markers) |
| Bot detection focus | Heavily targeted (~95% of bots use Chrome) | Rarely targeted (low bot traffic) |
| CDP detection risk | High (Runtime.enable leaks) | None (no CDP — uses native macOS AppleScript) |
| `navigator.webdriver` | `true` (must bypass with flags) | `false` by default (real Safari, no bypass needed) |
| Headless mode | Yes | No (requires display) |
| Concurrent sessions | Multiple | Single window (multiple tabs) |
| Fingerprint authenticity | Spoofed Chrome profile | Genuine WebKit/macOS fingerprint |
| Session persistence | Via `--user-data-dir` | Real Safari profile (cookies, history — already there) |
| Platform | macOS, Linux, Windows | macOS only |
| Best for | High-volume, multi-platform | Maximum stealth on macOS |

**Recommendation**: Use Chrome for high-volume automation or cross-platform. Use Safari when you need maximum stealth — it uses your real browser with real cookies, `navigator.webdriver=false`, no CDP artifacts, and a genuine WebKit fingerprint that bot detectors rarely target.

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

### Choose Your Browser

- **Chrome** (default): Best for most automation tasks. Full agent-browser CLI support with CDP. Cross-platform.
- **Safari** (macOS): Maximum stealth. Real Safari.app controlled via AppleScript — your actual browser, real cookies, `navigator.webdriver=false`, zero automation markers.

---

### Option A: Chrome Setup

#### Step 1: Launch Chrome with Stealth Flags

**Each persona needs its own Chrome profile** so login sessions stay separate. Replace `PERSONA_NAME` with your persona folder name (e.g., `prateek`, `jane`).

```bash
# macOS - Full anti-detection launch
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=$HOME/chrome-PERSONA_NAME \
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
  --user-data-dir=$HOME/chrome-PERSONA_NAME \
  --disable-blink-features=AutomationControlled \
  --disable-features=IsolateOrigins,site-per-process \
  --no-first-run \
  --window-size=1920,1080

# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" ^
  --remote-debugging-port=9222 ^
  --user-data-dir=%USERPROFILE%\chrome-PERSONA_NAME ^
  --disable-blink-features=AutomationControlled ^
  --disable-features=IsolateOrigins,site-per-process ^
  --no-first-run ^
  --window-size=1920,1080
```

**Important:** The `--user-data-dir` stores cookies and login sessions. Each persona must use a different directory (e.g., `~/chrome-prateek`, `~/chrome-jane`). After first launch, log into your social accounts manually — sessions persist across restarts.

### Key Anti-Detection Flags Explained

| Flag | Purpose |
|------|---------|
| `--disable-blink-features=AutomationControlled` | Hides `navigator.webdriver=true` |
| `--user-data-dir` | Creates real profile (not headless) |
| `--no-first-run` | Skips first-run dialogs |
| `--disable-infobars` | Removes "Chrome is being controlled" bar |
| `--window-size=1920,1080` | Normal screen resolution |

#### Step 2: Verify Chrome Stealth

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

#### Step 3: Authenticate Manually (Chrome)

1. Navigate to your target platform in the Chrome window
2. Log in with real credentials
3. Complete 2FA if prompted
4. Your authenticated session is now usable

#### Step 4: Connect Agent Browser (Chrome)

```bash
# Verify connection
agent-browser --cdp 9222 snapshot

# If successful, you'll see the page DOM structure
```

---

### Option B: Safari Setup (macOS Only)

Safari automation uses **AppleScript + JavaScript injection** to control the real Safari.app. This is the stealthiest approach — it uses your actual browser with real cookies, real profile, and zero automation markers.

**Why AppleScript over safaridriver/Playwright WebKit?**
- **safaridriver** creates isolated automation windows (orange bar, no cookies, `navigator.webdriver=true`)
- **Playwright WebKit** runs a sandboxed test browser, not real Safari
- **AppleScript** controls the actual Safari.app — real profile, real cookies, `navigator.webdriver=false`

#### Step 1: One-Time Setup (GUI)

Enable two settings in Safari (only needed once):

1. **Safari > Settings > Advanced** → check **"Show features for web developers"**
2. **Safari > Settings > Developer** → check **"Allow JavaScript from Apple Events"**

No CLI flags, no safaridriver, no npm packages needed.

#### Step 2: Open Safari

```bash
# Open Safari and navigate to a URL
osascript -e 'tell application "Safari" to activate' \
  -e 'tell application "Safari" to make new document with properties {URL:"https://x.com"}'
```

Your real Safari opens with your real profile — if you're already logged into X, you're already authenticated.

#### Step 3: Verify Connection

```bash
# Get current URL
osascript -e 'tell application "Safari" to get URL of current tab of window 1'

# Get page title
osascript -e 'tell application "Safari" to do JavaScript "document.title" in current tab of window 1'

# Verify no automation markers
osascript -e 'tell application "Safari" to do JavaScript "navigator.webdriver" in current tab of window 1'
# → Returns "false" (real Safari, not automated)
```

#### Step 4: Authenticate (if needed)

If not already logged in, log in manually in the Safari window. Since this is your real Safari profile, cookies persist naturally — no special profile directories needed.

#### Safari AppleScript Command Reference

```bash
# Navigation
osascript -e 'tell application "Safari" to set URL of current tab of window 1 to "https://x.com"'
osascript -e 'tell application "Safari" to do JavaScript "history.back()" in current tab of window 1'

# Get page info
osascript -e 'tell application "Safari" to get URL of current tab of window 1'
osascript -e 'tell application "Safari" to get name of current tab of window 1'
osascript -e 'tell application "Safari" to do JavaScript "document.title" in current tab of window 1'

# Execute JavaScript (click, fill, scroll, extract)
osascript -e 'tell application "Safari" to do JavaScript "document.querySelector(\"[data-testid=loginButton]\").click()" in current tab of window 1'
osascript -e 'tell application "Safari" to do JavaScript "document.querySelector(\"input[name=text]\").value = \"search query\"" in current tab of window 1'
osascript -e 'tell application "Safari" to do JavaScript "window.scrollBy(0, 500)" in current tab of window 1'

# Extract text content
osascript -e 'tell application "Safari" to do JavaScript "document.querySelector(\"article\").textContent" in current tab of window 1'

# Tab management
osascript -e 'tell application "Safari" to make new tab in window 1 with properties {URL:"https://x.com"}'
osascript -e 'tell application "Safari" to get number of tabs of window 1'
osascript -e 'tell application "Safari" to set current tab of window 1 to tab 2 of window 1'
osascript -e 'tell application "Safari" to close tab 2 of window 1'
```

#### Safari Detection Characteristics

| Attribute | Real Safari (AppleScript) | Stealth Impact |
|-----------|--------------------------|----------------|
| `navigator.webdriver` | `false` (not automated from browser's perspective) | Best possible — identical to manual browsing |
| Automation markers | None — AppleScript is external to the browser | Invisible to websites |
| CDP artifacts | None — no CDP protocol involved | Invisible to CDP detection |
| Browser fingerprint | Genuine WebKit/macOS canvas, WebGL, fonts | Perfect — real browser on real hardware |
| Cookies & sessions | Real Safari profile (persistent) | Perfect — uses existing login sessions |
| Orange address bar | No — only safaridriver shows this | No visual indicators |

#### Safari Anti-Detection Tips

1. **Already logged in?** You're done — AppleScript uses your real Safari with existing cookies. No need to re-authenticate.

2. **No `navigator.webdriver` bypass needed** — real Safari controlled via AppleScript reports `false` by default. Websites cannot detect AppleScript control.

3. **Fingerprint is genuine** — Safari on macOS produces a naturally consistent fingerprint (OS fonts, Metal GPU rendering, screen metrics). No spoofing needed.

4. **Add human delays between actions** — even though Safari can't detect you're automated, the platform's server-side analysis still watches for inhuman speed. Use the same timing guidelines as Chrome.

5. **Multiple tabs instead of multiple windows** — Safari supports multiple tabs in one window. Use tabs for multi-page workflows.

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

### Daily Limits

> **Canonical source:** See `strategy/_growth-algorithm.md` > Safety Limits for all rate limits by growth phase.
> Do not define local limits here — they will drift and conflict.

---

## Installation

### Chrome + agent-browser (Default)

```bash
# NPM (Recommended)
npm install -g agent-browser
agent-browser install  # Download Chromium

# Linux dependencies
agent-browser install --with-deps
```

### Safari (macOS Only — No Install Needed)

Safari is already installed on macOS. Just enable two settings once:

1. **Safari > Settings > Advanced** → check **"Show features for web developers"**
2. **Safari > Settings > Developer** → check **"Allow JavaScript from Apple Events"**

```bash
# Verify it works
osascript -e 'tell application "Safari" to activate' \
  -e 'tell application "Safari" to make new document with properties {URL:"https://example.com"}'
sleep 2
osascript -e 'tell application "Safari" to do JavaScript "document.title" in current tab of window 1'
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

### Chrome Workflow (CDP)

The fundamental workflow for AI agents using Chrome:

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

### Safari Workflow (AppleScript)

The workflow for Safari uses AppleScript to control the real Safari.app:

```bash
# 1. Open Safari to target URL
osascript -e 'tell application "Safari" to activate' \
  -e 'tell application "Safari" to set URL of current tab of window 1 to "https://x.com"'

# 2. Wait for page load (human reading time)
sleep 4

# 3. Get page title (verify loaded)
osascript -e 'tell application "Safari" to do JavaScript "document.title" in current tab of window 1'

# 4. Interact using JavaScript injection
# Click search
osascript -e 'tell application "Safari" to do JavaScript "document.querySelector(\"[data-testid=SearchBox_Search_Input]\").focus()" in current tab of window 1'

# Type search query
osascript -e 'tell application "Safari" to do JavaScript "
  var input = document.querySelector(\"[data-testid=SearchBox_Search_Input]\");
  var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, \"value\").set;
  nativeInputValueSetter.call(input, \"search query\");
  input.dispatchEvent(new Event(\"input\", { bubbles: true }));
" in current tab of window 1'

# Press Enter
osascript -e 'tell application "Safari" to do JavaScript "
  document.querySelector(\"[data-testid=SearchBox_Search_Input]\").dispatchEvent(new KeyboardEvent(\"keydown\", {key: \"Enter\", code: \"Enter\", bubbles: true}))
" in current tab of window 1'

# 5. Wait for results
sleep 3

# 6. Extract content
osascript -e 'tell application "Safari" to do JavaScript "
  JSON.stringify(Array.from(document.querySelectorAll(\"[data-testid=tweet]\")).slice(0,5).map(el => el.querySelector(\"[data-testid=tweetText]\")?.textContent))
" in current tab of window 1'
```

**Key difference from Chrome**: No refs (`@e1`) system — use CSS selectors and `data-testid` attributes via JavaScript injection. Use browser DevTools (Develop > Show Web Inspector) to inspect elements and find selectors.

---

## Critical Safari Rules

1. **NEVER use `System Events` keystroke/key code** — it sends input to whatever app is focused, steals screen focus, and interferes with the user's laptop. This includes Cmd+V paste.
2. **NEVER use `tell application "Safari" to activate`** — this also steals focus.
3. **NEVER use `cliclick`** — it moves the physical mouse cursor and interferes with the user's active laptop usage.
4. **NEVER use any screen automation tool** (cliclick, xdotool, Accessibility APIs, `System Events` click/keystroke) — the user is actively using the laptop.
5. **ONLY use JavaScript injection** (`do JavaScript` in Safari) for ALL browser interaction. No exceptions.
6. Use `tell application "Safari" to set URL of ...` for navigation (doesn't steal focus).
7. Use heredoc `osascript <<'APPLESCRIPT' ... APPLESCRIPT` pattern for multi-line scripts.
8. For LinkedIn dropdown menus that require trusted events, use the **Voyager API** directly instead of trying to click UI elements.

---

## Platform-Specific Text Input (Safari)

Different platforms use different editor implementations. Here's what works for each:

### X (Twitter) — Draft.js Editor

X uses a Draft.js contentEditable editor. Standard `element.value` or `innerHTML` won't work.

**CRITICAL:** Draft.js requires `click()` + `focus()` + a `setTimeout` delay before `execCommand("insertText")` works. Without the click+delay, Draft.js silently ignores the text because it only enters its editing state after a real click activates its internal handlers.

**Working method:**
```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var editor = document.querySelector('[data-testid=\"tweetTextarea_0\"]');
    if (!editor) { var editors = document.querySelectorAll('[role=\"textbox\"]'); editor = editors[editors.length - 1]; }
    if (editor) {
      editor.click();
      editor.focus();
      setTimeout(function() {
        document.execCommand('insertText', false, 'Your tweet text here');
        window._replyLen = editor.innerText.length;
      }, 300);
    }
  " in front document
end tell
APPLESCRIPT
```

**Verify text injected (wait 1s):**
```bash
osascript -e 'tell application "Safari" to do JavaScript "window._replyLen" in front document'
```
If result is `1` (empty), the text didn't inject — retry or reload the page.

**To clear and replace text:**
```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var editor = document.querySelector('[data-testid=\"tweetTextarea_0\"]');
    if (editor) {
      editor.click();
      editor.focus();
      setTimeout(function() {
        document.execCommand('selectAll', false, null);
        document.execCommand('delete', false, null);
        document.execCommand('insertText', false, 'New tweet text');
      }, 300);
    }
  " in front document
end tell
APPLESCRIPT
```

**Key X selectors:**
| Element | Selector |
|---------|----------|
| Tweet editor | `[data-testid="tweetTextarea_0"]` |
| Post button (compose) | `[data-testid="tweetButton"]` |
| Reply button (inline) | `[data-testid="tweetButtonInline"]` |
| Add thread tweet | `[data-testid="addButton"]` |
| Caret menu (tweet options) | `[data-testid="caret"]` |
| Like button | `[data-testid="like"]` |
| Follow button | `[data-testid="followButton"]` |

### LinkedIn — TipTap/ProseMirror Editor (Safari)

LinkedIn uses TipTap (ProseMirror) for comment editors: `.tiptap.ProseMirror[contenteditable=true]`.

**CRITICAL SAFETY RULES:**
1. **NEVER comment from the feed.** The feed DOM shifts as it loads — clicking "Comment" on one post can open the editor for a completely different post. This has caused comments to land on the WRONG POST.
2. **ALWAYS navigate to the individual post URL first:** `https://www.linkedin.com/feed/update/urn:li:activity:ACTIVITY_ID/`
3. **VERIFY post content before commenting** — extract post text, confirm it matches the topic you're commenting on. If it doesn't match, STOP.
4. **VERIFY comment landed correctly after submitting** — check that your comment appears under the correct post.

**Working method (comment on individual post page):**
```bash
# 1. Navigate to individual post (MANDATORY)
osascript -e 'tell application "Safari" to set URL of front document to "https://www.linkedin.com/feed/update/urn:li:activity:ACTIVITY_ID/"'
# 2. Wait 4s, verify post content
# 3. Click Comment button
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
# 4. Wait 2s, inject text into TipTap editor
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var editor = document.querySelector('.tiptap.ProseMirror[contenteditable=true]');
    if (editor) {
      editor.scrollIntoView({behavior: 'instant', block: 'center'});
      setTimeout(function() {
        editor.focus();
        editor.innerHTML = '<p>Your comment text here</p>';
        editor.dispatchEvent(new Event('input', {bubbles: true}));
      }, 500);
    }
  " in front document
end tell
APPLESCRIPT
# 5. Submit — find the Comment button BELOW the editor by proximity
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

**LinkedIn post compose (Safari):**
```bash
osascript <<'APPLESCRIPT'
tell application "Safari"
  do JavaScript "
    var editor = document.querySelector('.ql-editor[contenteditable=true]');
    if (editor) {
      editor.focus();
      editor.innerHTML = '<p>Your post text here</p>';
      editor.dispatchEvent(new Event('input', {bubbles: true}));
    }
  " in front document
end tell
APPLESCRIPT
```

### Old Reddit — Simple Textarea

```javascript
var textarea = document.querySelector('textarea');
textarea.value = 'Your comment text';
textarea.dispatchEvent(new Event('change', {bubbles: true}));
// Click save button
document.querySelector('button[type="submit"]').click();
```

### Other Sites — Standard Inputs

```javascript
var input = document.querySelector('input[name="text"]');
var nativeInputValueSetter = Object.getOwnPropertyDescriptor(
  window.HTMLInputElement.prototype, 'value'
).set;
nativeInputValueSetter.call(input, 'your text');
input.dispatchEvent(new Event('input', { bubbles: true }));
```

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

### Chrome Workflow

#### Step 1: Setup Stealth Session
```bash
# Launch Chrome with anti-detection flags
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-agent-profile \
  --disable-blink-features=AutomationControlled \
  --no-first-run \
  --window-size=1920,1080
```

#### Step 2: Verify Fingerprint
```bash
# Check you're not detected
agent-browser --cdp 9222 open "https://bot.sannysoft.com"
```

#### Step 3: Authenticate (Manual)
- Log into X, LinkedIn, etc. in the Chrome window
- Complete any verification
- Browse naturally for 1-2 minutes

#### Step 4: Search for Leads
```bash
# Find people requesting services
agent-browser --cdp 9222 open "https://x.com/search?q=%22need%20a%20website%22&f=live"

# Wait 3-5 seconds
agent-browser --cdp 9222 snapshot
```

#### Step 5: Analyze & Qualify
Review snapshot output for:
- Post content (what they need)
- Engagement (replies, likes, views)
- Recency (when posted)
- Profile info (legit potential client?)

#### Step 6: Engage (With Delays)
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

#### Step 7: Track Results
Keep a spreadsheet of:
- Leads found
- Actions taken
- Responses received
- Conversions

### Safari Workflow (AppleScript)

#### Step 1: Open Safari
```bash
# Open Safari to X (uses your real profile — already logged in if you've logged in before)
osascript -e 'tell application "Safari" to activate' \
  -e 'tell application "Safari" to make new document with properties {URL:"https://x.com"}'
```

#### Step 2: Verify Fingerprint
```bash
# Navigate to fingerprint test
osascript -e 'tell application "Safari" to set URL of current tab of window 1 to "https://bot.sannysoft.com"'

# Check navigator.webdriver (should be "false")
sleep 3 && osascript -e 'tell application "Safari" to do JavaScript "navigator.webdriver" in current tab of window 1'
```

#### Step 3: Search for Leads
```bash
# Navigate to X search
osascript -e 'tell application "Safari" to set URL of current tab of window 1 to "https://x.com/search?q=%22need%20a%20website%22&f=live"'

# Wait 3-5 seconds (human reading time)
sleep 4

# Extract top tweet texts
osascript -e 'tell application "Safari" to do JavaScript "
  JSON.stringify(Array.from(document.querySelectorAll(\"[data-testid=tweet]\")).slice(0,10).map(el => ({
    text: el.querySelector(\"[data-testid=tweetText]\")?.textContent,
    user: el.querySelector(\"a[role=link][href^=/]\")?.getAttribute(\"href\")
  })))
" in current tab of window 1'
```

#### Step 4: Analyze & Qualify
Review extracted content for:
- Post content (what they need)
- User profiles (legit potential client?)
- Recency (when posted)

#### Step 5: Engage (With Delays)
```bash
# Navigate to a lead's profile (30-90 sec between follows)
osascript -e 'tell application "Safari" to set URL of current tab of window 1 to "https://x.com/leadusername"'
sleep 3

# Click follow button
osascript -e 'tell application "Safari" to do JavaScript "document.querySelector(\"[data-testid=followButton]\")?.click()" in current tab of window 1'

# Wait 30-90 seconds before next follow
sleep 45

# Like a post (scroll into view first, then click)
osascript -e 'tell application "Safari" to do JavaScript "window.scrollBy(0, 300)" in current tab of window 1'
sleep 2
osascript -e 'tell application "Safari" to do JavaScript "document.querySelector(\"[data-testid=like]\")?.click()" in current tab of window 1'

# Wait 10-30 seconds before next like
sleep 15
```

#### Step 6: Track Results
Same as Chrome — keep a spreadsheet of leads, actions, responses, conversions.

---

## Output Format

When invoked, provide browser automation guidance:

```
AGENT BROWSER SETUP
━━━━━━━━━━━━━━━━━━━━━━━━

BROWSER: [Chrome (CDP) | Safari (AppleScript)]
TASK: [What you want to accomplish]

SETUP COMMANDS:
[Chrome launch command OR Safari AppleScript open]

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

### Detected as Bot (Chrome)
- Verify fingerprint at bot.sannysoft.com
- Ensure `--disable-blink-features=AutomationControlled` is set
- Check `navigator.webdriver` returns `undefined`
- Slow down significantly
- Add more human-like timing variance
- **Consider switching to Safari** — different browser fingerprint may bypass Chrome-specific detection

### Safari: "Allow JavaScript from Apple Events" Error
```bash
# Error: "You must enable 'Allow JavaScript from Apple Events'"
# Fix: Enable via Safari GUI (cannot be set via command line on modern macOS)
#   1. Safari > Settings > Advanced > check "Show features for web developers"
#   2. Safari > Settings > Developer > check "Allow JavaScript from Apple Events"
#   3. Restart Safari after enabling

# Verify it works
osascript -e 'tell application "Safari" to do JavaScript "document.title" in current tab of window 1'
```

### Safari: JavaScript Returns Empty/Undefined
- Page may not be fully loaded — add `sleep 3-5` before running JavaScript
- Element may not exist — check the CSS selector in Safari's Web Inspector (Develop > Show Web Inspector)
- Special characters in selectors need escaping: use `\"` inside AppleScript strings

### Safari: Navigation Not Working
```bash
# Make sure Safari is open with at least one window
osascript -e 'tell application "Safari" to activate' \
  -e 'tell application "Safari" to make new document with properties {URL:"https://x.com"}'

# If window exists but tab is wrong, target specific tab
osascript -e 'tell application "Safari" to set URL of tab 1 of window 1 to "https://x.com"'
```

### Safari: AppleScript Permission Denied
- Go to **System Settings > Privacy & Security > Automation**
- Ensure your terminal app (Terminal.app, iTerm2, etc.) has permission to control Safari
- You may need to re-grant permission after macOS updates

---

## Security Notes

- **Never share your user-data-dir** (Chrome) — contains session cookies
- **Safari uses your real profile** — be aware that automation runs in the same context as your personal browsing
- **Use separate macOS user accounts** if you need isolated Safari profiles for different personas
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

### Safari & AppleScript
- [Safari AppleScript Dictionary](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/) - Apple's AppleScript language guide
- [Automating Safari with AppleScript](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/) - Mac Automation Scripting Guide
- [About WebDriver for Safari](https://developer.apple.com/documentation/webkit/about-webdriver-for-safari) - Apple developer docs (safaridriver reference)
- [Enabling Remote Automation in Safari 14+](https://blog.bytesguy.com/enabling-remote-automation-in-safari-14) - CLI removal workarounds

### Anti-Detection Research
- [Bot Detection Methods](https://fingerprint.com/blog/bot-detection/)
- [CDP Detection Evasion](https://blog.castle.io/from-puppeteer-stealth-to-nodriver-how-anti-detect-frameworks-evolved-to-evade-bot-detection/)
- [LinkedIn Bot Detection](https://blog.castle.io/detecting-browser-extensions-for-bot-detection-lessons-from-linkedin-and-castle/)
- [Mouse Movement Patterns](https://github.com/sarperavci/human_mouse)
- [Browser Fingerprinting](https://www.browserless.io/blog/device-fingerprinting)
- [Navigator.webdriver Evasion](https://www.zenrows.com/blog/navigator-webdriver)
