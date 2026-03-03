#!/bin/bash
set -e

echo "=== Social Media Manager Setup ==="

# Check Node.js
if ! command -v node &> /dev/null; then
  echo "ERROR: Node.js not found. Install from https://nodejs.org"
  exit 1
fi

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
  echo "ERROR: Node.js 18+ required (found $(node -v))"
  exit 1
fi

echo "[1/3] Installing agent-browser + CloakBrowser + Playwright..."
npm install -g agent-browser cloakbrowser playwright-core

echo "[2/3] Downloading CloakBrowser stealth Chromium binary (~200MB)..."
node --input-type=module -e "
  import { createRequire } from 'node:module';
  const require = createRequire(import.meta.url);
  const cloakPath = require.resolve('cloakbrowser/dist/download.js');
  const { ensureBinary } = await import('file://' + cloakPath);
  await ensureBinary();
"

echo "[3/3] Setting up credentials template..."
if [ ! -f .credentials.md ]; then
  cp .credentials.example.md .credentials.md
  echo "  Created .credentials.md — edit with your accounts (NEVER commit)"
else
  echo "  .credentials.md already exists, skipping"
fi

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "  1. Edit .credentials.md with your social accounts"
echo "  2. Create your persona: cp -r personas/_template personas/yourname"
echo "  3. Fill in personas/yourname/strategy/_persona.md"
echo "  4. Read strategy/_core-principles.md (anti-AI detection rules)"
echo "  5. Read skills/automation/agent-browser.md (browser automation)"
echo "  6. Launch browsers: bash launch-browsers.sh yourname"
