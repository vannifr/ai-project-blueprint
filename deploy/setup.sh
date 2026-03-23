#!/bin/bash
set -euo pipefail

# =============================================================================
# Blueprint VPS Setup — run once on the VPS
# =============================================================================
#
# Prerequisites:
#   - Debian with Docker + nginx + certbot
#   - DNS: ai-delivery.io A → 57.129.77.32
#
# Usage:
#   ssh user@57.129.77.32
#   git clone https://github.com/vannifr/ai-project-blueprint.git
#   cd ai-project-blueprint/deploy
#   cp .env.example .env   # fill in API keys
#   bash setup.sh
# =============================================================================

echo "=== Blueprint VPS Setup ==="

# Check prerequisites
for cmd in docker nginx certbot; do
    if ! command -v $cmd &>/dev/null; then
        echo "ERROR: $cmd not installed."
        exit 1
    fi
done

if [ ! -f .env ]; then
    echo "ERROR: .env not found. Run: cp .env.example .env"
    exit 1
fi

cd "$(dirname "$0")/.."
REPO_ROOT="$(pwd)"

# --- Step 1: SSL certificate ---
echo "Obtaining SSL certificate for ai-delivery.io..."
sudo certbot certonly --webroot -w /var/www/html \
    -d ai-delivery.io -d www.ai-delivery.io \
    --non-interactive --agree-tos --email admin@ai-delivery.io \
    || echo "Cert already exists or webroot not ready — will retry after nginx config"

# --- Step 2: Build MkDocs site ---
echo "Building MkDocs site..."
docker run --rm -v "$REPO_ROOT":/app -w /app python:3.12-slim bash -c "
    pip install -q -r requirements.txt 2>/dev/null &&
    python3 scripts/patch_i18n.py 2>/dev/null &&
    MKDOCS_LANG=nl MKDOCS_BUILD_I18N=true mkdocs build --quiet
"

# --- Step 3: Deploy static site ---
echo "Deploying static site..."
sudo mkdir -p /var/www/ai-delivery.io
sudo cp -r site/* /var/www/ai-delivery.io/
sudo chown -R www-data:www-data /var/www/ai-delivery.io

# --- Step 4: Nginx config ---
echo "Configuring nginx..."
sudo cp deploy/nginx-ai-delivery.conf /etc/nginx/sites-available/ai-delivery.io
sudo ln -sf /etc/nginx/sites-available/ai-delivery.io /etc/nginx/sites-enabled/ai-delivery.io

# Test nginx config before reloading
sudo nginx -t
sudo systemctl reload nginx

# --- Step 5: SSL cert (retry if first attempt failed) ---
if [ ! -f /etc/letsencrypt/live/ai-delivery.io/fullchain.pem ]; then
    echo "Retrying SSL certificate..."
    sudo certbot certonly --webroot -w /var/www/html \
        -d ai-delivery.io -d www.ai-delivery.io \
        --non-interactive --agree-tos --email admin@ai-delivery.io
    sudo systemctl reload nginx
fi

# --- Step 6: Build and start Docker containers ---
echo "Building Docker containers..."
cd deploy
docker compose build

echo "Building RAG search index..."
docker compose run --rm chatbot python /app/scripts/build_index.py \
    --docs-root /app/docs \
    --output-dir /app/chroma_data

echo "Starting services..."
docker compose up -d

echo ""
echo "=== Setup complete ==="
echo ""
echo "Site:     https://ai-delivery.io"
echo "Chat API: https://ai-delivery.io/api/health"
echo "MCP:      https://ai-delivery.io/mcp/"
echo ""
echo "Verify: curl https://ai-delivery.io/api/health"
