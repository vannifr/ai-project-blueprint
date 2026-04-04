# Rollback Procedure

Use this guide to roll back the production deployment on ai-delivery.io to a previous stable state.

______________________________________________________________________

## Prerequisites

- SSH access to the VPS (`deploy/setup.sh` credentials)
- The Git SHA or tag of the last known-good commit (find via `git log --oneline`)

______________________________________________________________________

## 1. Quick rollback — code only (\< 2 min)

Use this when the site content or MCP server broke but containers are still up.

```bash
ssh -p $SSH_PORT $SSH_USER@$SSH_HOST
cd $SSH_PATH

# Pin to a specific commit
git fetch origin
git checkout <GOOD_SHA>

# Rebuild static site and restart containers
bash deploy/update.sh
```

Verify: `curl -fsS http://localhost:8902/health` — expect `{"status":"ok",...}`.

______________________________________________________________________

## 2. Container rollback — broken image (\< 5 min)

Use when a newly built Docker image is unhealthy (`docker compose ps` shows `unhealthy`).

```bash
cd $SSH_PATH/deploy

# Bring down current containers
docker compose down

# Restore previous image by reverting the Dockerfile commit, then rebuild
git checkout <GOOD_SHA> -- mcp_server/Dockerfile chatbot/Dockerfile
docker compose build
docker compose up -d

# Confirm health
docker compose ps
curl -fsS http://localhost:8902/health
```

______________________________________________________________________

## 3. Full rollback — data + code (\< 10 min)

Use when the ChromaDB search index is corrupted.

```bash
cd $SSH_PATH/deploy

# Stop all containers (preserves named volumes)
docker compose down

# Restore code
git checkout <GOOD_SHA>

# Remove and recreate the chroma volume
docker volume rm deploy_chroma_data
docker compose up -d

# Rebuild search index from docs
docker compose run --rm chatbot python /app/scripts/build_index.py \
    --docs-root /app/docs \
    --output-dir /app/chroma_data

docker compose restart chatbot
```

______________________________________________________________________

## 4. Verify rollback success

Run all checks before declaring the rollback done:

```bash
# MCP server health
curl -fsS http://localhost:8902/health | python3 -m json.tool

# Chatbot API (if applicable)
curl -fsS http://localhost:8901/health | python3 -m json.tool

# Docker container status
docker compose ps

# Nginx serving the site
curl -fsI https://ai-delivery.io/ | head -5
```

Expected outcomes:

- Both `/health` endpoints return `{"status":"ok"}` with `doc_count >= 100`
- All containers show status `healthy`
- Site returns HTTP 200

______________________________________________________________________

## 5. Re-deploy after the fix

Once the root cause is fixed and merged to `main`, re-deploy normally:

```bash
cd $SSH_PATH
git checkout main
git pull
bash deploy/update.sh
```

______________________________________________________________________

## Contacts / escalation

| Role        | Action                                                                       |
| ----------- | ---------------------------------------------------------------------------- |
| On-call dev | Fix root cause in code, push to `main`, re-deploy                            |
| Infra       | VPS unreachable → check host provider dashboard                              |
| Monitoring  | UptimeRobot alert → check `https://ai-delivery.io/` and MCP health endpoints |
