#!/bin/bash
set -euo pipefail

# =============================================================================
# Blueprint VPS Setup — run once on the VPS
# =============================================================================
# Prerequisites:
#   - Debian with Docker installed
#   - DNS: ai-delivery.io A-record → 57.129.77.32
#
# Usage:
#   ssh user@57.129.77.32
#   git clone https://github.com/vannifr/ai-project-blueprint.git
#   cd ai-project-blueprint/deploy
#   cp .env.example .env
#   # Edit .env with your API keys
#   bash setup.sh
# =============================================================================

echo "=== Blueprint VPS Setup ==="

# Check Docker
if ! command -v docker &>/dev/null; then
    echo "ERROR: Docker not installed. Install first: https://docs.docker.com/engine/install/debian/"
    exit 1
fi

if ! command -v docker compose &>/dev/null; then
    echo "ERROR: Docker Compose not installed."
    exit 1
fi

# Check .env
if [ ! -f .env ]; then
    echo "ERROR: .env not found. Copy .env.example and fill in API keys:"
    echo "  cp .env.example .env"
    exit 1
fi

# Build MkDocs site into the site_html volume
echo "Building MkDocs site..."
cd ..
docker run --rm -v "$(pwd)":/app -w /app python:3.12-slim bash -c "
    pip install -q -r requirements.txt &&
    python3 scripts/patch_i18n.py &&
    MKDOCS_LANG=nl MKDOCS_BUILD_I18N=true mkdocs build
"

# Copy site to deploy context
echo "Preparing site files..."
mkdir -p deploy/site
cp -r site/* deploy/site/
cd deploy

# Build and start services
echo "Building containers..."
docker compose build

# Create site volume and copy files
docker compose up -d caddy
docker compose cp site/. caddy:/srv/site/
docker compose restart caddy

# Build chatbot search index
echo "Building RAG search index..."
docker compose run --rm chatbot python /app/scripts/build_index.py \
    --docs-root /app/docs \
    --output-dir /app/chroma_data

# Start all services
echo "Starting all services..."
docker compose up -d

echo ""
echo "=== Setup complete ==="
echo "Site:     https://ai-delivery.io"
echo "Chat API: https://ai-delivery.io/api/health"
echo "MCP:      https://ai-delivery.io/mcp/"
echo ""
echo "To update after code changes:"
echo "  cd ai-project-blueprint && git pull && bash deploy/update.sh"
