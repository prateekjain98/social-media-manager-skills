#!/bin/bash
# Launch CloakBrowser instances for a persona (client account).
# Each persona gets isolated browser profiles on dedicated ports.
#
# Usage:
#   bash launch-browsers.sh <persona> [platforms...]
#   bash launch-browsers.sh prateek              — launch all platforms for prateek
#   bash launch-browsers.sh suprdash x linkedin   — launch X + LinkedIn for suprdash
#   bash launch-browsers.sh prateek x & bash launch-browsers.sh suprdash x
#     — run two clients' X accounts in parallel
#
# Port allocation:
#   Each persona gets a block of 10 ports based on alphabetical order in personas/.
#   Offsets: X=0, LinkedIn=1, Reddit=2, Instagram=3
#   Formula: port = 9222 + (persona_index * 10) + platform_offset

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$1" ]; then
  echo "Usage: launch-browsers.sh <persona> [platforms...]"
  echo ""
  echo "Examples:"
  echo "  bash launch-browsers.sh prateek              # all platforms"
  echo "  bash launch-browsers.sh suprdash x linkedin   # specific platforms"
  echo ""
  echo "Available personas:"
  ls -d "$SCRIPT_DIR"/personas/*/strategy 2>/dev/null | xargs -I{} dirname {} | xargs -I{} basename {} | grep -v _template | sort
  exit 1
fi

PERSONA=$1
shift
PLATFORMS=${@:-x linkedin reddit instagram}

# Verify persona exists
if [ ! -d "$SCRIPT_DIR/personas/$PERSONA/strategy" ]; then
  echo "ERROR: Persona '$PERSONA' not found. Available personas:"
  ls -d "$SCRIPT_DIR"/personas/*/strategy 2>/dev/null | xargs -I{} dirname {} | xargs -I{} basename {} | grep -v _template | sort
  exit 1
fi

# Platform port offsets
declare -A OFFSETS=( [x]=0 [linkedin]=1 [reddit]=2 [instagram]=3 )

# Persona → base port (auto-assign based on persona directories, alphabetical)
PERSONA_DIRS=($(ls -d "$SCRIPT_DIR"/personas/*/strategy 2>/dev/null | xargs -I{} dirname {} | xargs -I{} basename {} | grep -v _template | sort))
PERSONA_INDEX=0
for dir in "${PERSONA_DIRS[@]}"; do
  if [ "$dir" = "$PERSONA" ]; then break; fi
  PERSONA_INDEX=$((PERSONA_INDEX + 1))
done
BASE_PORT=$((9222 + PERSONA_INDEX * 10))

echo "=== Launching CloakBrowser for: $PERSONA (base port: $BASE_PORT) ==="
echo ""

for platform in $PLATFORMS; do
  offset=${OFFSETS[$platform]}
  if [ -z "$offset" ]; then
    echo "  [SKIP] Unknown platform: $platform (valid: x, linkedin, reddit, instagram)"
    continue
  fi

  port=$((BASE_PORT + offset))

  # Skip if port already in use
  if lsof -i :$port &>/dev/null; then
    echo "  [$platform] Already running on port $port"
    continue
  fi

  echo "  [$platform] Launching on port $port..."
  node "$SCRIPT_DIR/launch-browser.mjs" "$PERSONA" "$platform" "$port" &

  sleep 3
done

echo ""
echo "Connect with agent-browser:"
for platform in $PLATFORMS; do
  offset=${OFFSETS[$platform]}
  if [ -z "$offset" ]; then continue; fi
  port=$((BASE_PORT + offset))
  echo "  agent-browser --cdp $port snapshot   # $PERSONA → $platform"
done
echo ""
echo "To stop all browsers: pkill -f 'launch-browser.mjs'"
