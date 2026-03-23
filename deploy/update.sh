#!/bin/bash
set -euo pipefail

# =============================================================================
# Blueprint VPS Update — run after code/content changes
# =============================================================================

echo "=== Blueprint Update ==="

cd "$(dirname "$0")/.."
REPO_ROOT="$(pwd)"

# Pull latest
git pull

# Rebuild site
echo "Building MkDocs site..."
docker run --rm -v "$REPO_ROOT":/app -w /app python:3.12-slim bash -c "
    pip install -q -r requirements.txt 2>/dev/null &&
    python3 scripts/patch_i18n.py 2>/dev/null &&
    MKDOCS_LANG=nl MKDOCS_BUILD_I18N=true mkdocs build --quiet
"

# Deploy static files
echo "Deploying static site..."
sudo cp -r site/* /var/www/ai-delivery.io/
sudo chown -R www-data:www-data /var/www/ai-delivery.io

# Rebuild containers if code changed
echo "Rebuilding Docker containers..."
cd deploy
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
