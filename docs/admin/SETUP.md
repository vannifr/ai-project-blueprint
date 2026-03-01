---
pdf: false
search:
  exclude: true
---

# Static CMS — Authenticatie Setup

Dit bestand is alleen voor interne configuratie. Het verschijnt niet in de navigatie.

## Optie A: Lokaal ontwikkelen (geen OAuth nodig)

Gebruik de local backend proxy voor offline bewerken:

```bash
# Terminal 1 — start de CMS proxy
npx @staticcms/proxy-server

# Terminal 2 — start de MkDocs live preview
mkdocs serve
```

Ga naar `http://localhost:8000/admin/` en log in. Wijzigingen worden direct
naar uw lokale bestanden geschreven (en worden daarna normaal via Git gecommit).

______________________________________________________________________

## Optie B: Productie via Netlify OAuth (aanbevolen, gratis)

Deze methode werkt voor elke statische site — ook zonder Netlify hosting.

### Stap 1 — GitHub OAuth App aanmaken

1. Ga naar **GitHub → Settings → Developer settings → OAuth Apps → New OAuth App**
1. Vul in:
    - **Application name:** `AI Project Blauwdruk CMS`
    - **Homepage URL:** `https://vannifr.ovh/ai-project-blueprint/`
    - **Authorization callback URL:** `https://api.netlify.com/auth/done`
1. Klik **Register application** en noteer de **Client ID** en **Client Secret**.

### Stap 2 — Netlify OAuth provider configureren

1. Maak een gratis account op [netlify.com](https://netlify.com) (geen deployment nodig).
1. Maak een willekeurig **New site** aan (bijv. een leeg project).
1. Ga naar **Site settings → Access control → OAuth → Install provider → GitHub**.
1. Vul **Client ID** en **Client Secret** van stap 1 in.

### Stap 3 — config.yml aanpassen

In `docs/admin/config.yml`, de `base_url` is al ingesteld op `https://api.netlify.com`.
Geen verdere wijzigingen nodig.

### Stap 4 — Testen

Ga naar `https://vannifr.ovh/ai-project-blueprint/admin/` en klik **Login with GitHub**.

______________________________________________________________________

## Optie C: Eigen OAuth-proxy via Cloudflare Workers

Gebruik dit als u geen Netlify account wilt aanmaken.

### Stap 1 — GitHub OAuth App aanmaken (zie Optie B, Stap 1)

Gebruik als callback URL: `https://cms-oauth.UW-SUBDOMAIN.workers.dev/callback`

### Stap 2 — Cloudflare Worker deployen

```bash
npm install -g wrangler
wrangler login

# Clone de kant-en-klare OAuth worker
git clone https://github.com/sveltia/sveltia-cms-auth oauth-worker
cd oauth-worker
```

Pas `wrangler.toml` aan en stel de secrets in:

```bash
wrangler secret put GITHUB_CLIENT_ID
wrangler secret put GITHUB_CLIENT_SECRET
wrangler deploy
```

### Stap 3 — config.yml aanpassen

```yaml
backend:
  base_url: https://cms-oauth.UW-SUBDOMAIN.workers.dev
```

______________________________________________________________________

## Rechten

Alleen GitHub-gebruikers met **Write** of **Admin** toegang tot de repository
`vannifr/ai-project-blueprint` kunnen inloggen in het CMS.
