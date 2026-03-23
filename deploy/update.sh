#!/bin/bash
set -euo pipefail

# =============================================================================
# Blueprint VPS Update — run after code/content changes
# =============================================================================

echo "=== Blueprint Update ==="

cd "$(dirname "$0")/.."

# Pull latest
git pull

# Rebuild site
echo "Building MkDocs site..."
docker run --rm -v "$(pwd)":/app -w /app python:3.12-slim bash -c "
    pip install -q -r requirements.txt &&
    python3 scripts/patch_i18n.py &&
    MKDOCS_LANG=nl MKDOCS_BUILD_I18N=true mkdocs build
"

# Update site files
echo "Updating site files..."
cd deploy
docker compose cp ../site/. caddy:/srv/site/

# Rebuild containers if code changed
echo "Rebuilding containers..."
docker compose build
docker compose up -d

# Rebuild search index
echo "Rebuilding RAG search index..."
docker compose run --rm chatbot python /app/scripts/build_index.py \
    --docs-root /app/docs \
    --output-dir /app/chroma_data

# Restart chatbot to pick up new index
docker compose restart chatbot

echo ""
echo "=== Update complete ==="
