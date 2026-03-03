#!/usr/bin/env node
/**
 * Launch a CloakBrowser (stealth Chromium) instance for a persona + platform.
 * Directly runs the patched Chromium binary with stealth args.
 *
 * Usage:
 *   node launch-browser.mjs <persona> <platform> [port]
 *   node launch-browser.mjs prateek x 9222
 *   node launch-browser.mjs suprdash linkedin 9233
 *
 * The browser opens headed (visible) with a persistent profile at:
 *   ~/cloakbrowser-<persona>-<platform>/
 *
 * Connect agent-browser:
 *   agent-browser --cdp <port> snapshot
 */

import { resolve } from 'node:path';
import { homedir, platform as osPlatform } from 'node:os';
import { existsSync, readdirSync } from 'node:fs';
import { spawn } from 'node:child_process';

const PLATFORM_URLS = {
  x: 'https://x.com',
  linkedin: 'https://linkedin.com',
  reddit: 'https://reddit.com',
  instagram: 'https://instagram.com',
};

// Parse args
const persona = process.argv[2];
const platform = process.argv[3];
const port = parseInt(process.argv[4] || '9222', 10);

if (!persona || !platform) {
  console.error('Usage: node launch-browser.mjs <persona> <platform> [port]');
  console.error('  node launch-browser.mjs prateek x 9222');
  process.exit(1);
}

const url = PLATFORM_URLS[platform];
if (!url) {
  console.error(`Unknown platform: ${platform}. Valid: ${Object.keys(PLATFORM_URLS).join(', ')}`);
  process.exit(1);
}

// Find CloakBrowser binary
const cacheDir = process.env.CLOAKBROWSER_CACHE_DIR || resolve(homedir(), '.cloakbrowser');
let binaryPath;

if (process.env.CLOAKBROWSER_BINARY_PATH) {
  binaryPath = process.env.CLOAKBROWSER_BINARY_PATH;
} else {
  // Find the latest chromium-* directory
  const dirs = readdirSync(cacheDir)
    .filter(d => d.startsWith('chromium-'))
    .sort()
    .reverse();

  if (dirs.length === 0) {
    console.error('ERROR: CloakBrowser binary not found. Run: node -e "import(\'cloakbrowser\').then(m=>m.ensureBinary())"');
    console.error('Or set CLOAKBROWSER_BINARY_PATH to a local Chromium binary.');
    process.exit(1);
  }

  const latestDir = resolve(cacheDir, dirs[0]);

  if (osPlatform() === 'darwin') {
    binaryPath = resolve(latestDir, 'Chromium.app', 'Contents', 'MacOS', 'Chromium');
  } else if (osPlatform() === 'win32') {
    binaryPath = resolve(latestDir, 'chrome.exe');
  } else {
    binaryPath = resolve(latestDir, 'chrome');
  }
}

if (!existsSync(binaryPath)) {
  console.error(`ERROR: Binary not found at ${binaryPath}`);
  process.exit(1);
}

const profileDir = resolve(homedir(), `cloakbrowser-${persona}-${platform}`);

// Build stealth args (matches CloakBrowser's getDefaultStealthArgs)
const seed = Math.floor(Math.random() * 90000) + 10000;
const isMac = osPlatform() === 'darwin';

const stealthArgs = [
  '--no-sandbox',
  '--disable-blink-features=AutomationControlled',
  `--fingerprint=${seed}`,
  ...(isMac ? [
    '--fingerprint-platform=macos',
    '--fingerprint-gpu-vendor=Google Inc. (Apple)',
    '--fingerprint-gpu-renderer=ANGLE (Apple, ANGLE Metal Renderer: Apple M3, Unspecified Version)',
  ] : [
    '--fingerprint-platform=windows',
    '--fingerprint-hardware-concurrency=8',
    '--fingerprint-device-memory=8',
    '--fingerprint-gpu-vendor=NVIDIA Corporation',
    '--fingerprint-gpu-renderer=NVIDIA GeForce RTX 3070',
    '--fingerprint-screen-width=1920',
    '--fingerprint-screen-height=1080',
  ]),
];

const args = [
  ...stealthArgs,
  `--remote-debugging-port=${port}`,
  `--user-data-dir=${profileDir}`,
  '--window-size=1920,1080',
  '--no-first-run',
  '--no-default-browser-check',
  url,
];

console.log(`\n=== CloakBrowser: ${persona} → ${platform} ===`);
console.log(`  Port:    ${port}`);
console.log(`  Profile: ${profileDir}`);
console.log(`  URL:     ${url}`);
console.log(`  Connect: agent-browser --cdp ${port} snapshot\n`);

// Launch the binary directly
const child = spawn(binaryPath, args, {
  stdio: 'ignore',
  detached: true,
});

child.unref();

console.log(`  Browser launched (PID: ${child.pid})`);
console.log(`  Waiting for CDP on port ${port}...`);

// Wait for port to become available
let attempts = 0;
const maxAttempts = 15;
while (attempts < maxAttempts) {
  await new Promise(r => setTimeout(r, 1000));
  try {
    const res = await fetch(`http://127.0.0.1:${port}/json/version`);
    if (res.ok) {
      const info = await res.json();
      console.log(`  Connected! Browser: ${info.Browser || 'CloakBrowser'}`);
      break;
    }
  } catch {
    // Not ready yet
  }
  attempts++;
}

if (attempts >= maxAttempts) {
  console.error(`  WARNING: Could not verify CDP on port ${port} after ${maxAttempts}s`);
}

process.exit(0);
