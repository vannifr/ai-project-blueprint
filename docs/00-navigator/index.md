---
versie: '1.0'
description: Blueprint Navigator — interactieve gids om de juiste module te vinden voor jouw AI-projectfase, rol of uitdaging. Begin hier om jezelf te oriënteren in de AI Project Blauwdruk.
---

# Blueprint Navigator

Beantwoord vier stappen — uw rol, uw context, en tien maturity-vragen — en de Navigator wijst u direct naar uw startpunt in de blauwdruk.

<div id="blueprint-navigator">
<style>
#blueprint-navigator {
  max-width: 820px;
  margin: 0 auto;
  font-family: inherit;
}
.bn-progress-bar-outer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  position: relative;
}
.bn-progress-bar-outer::before {
  content: '';
  position: absolute;
  top: 16px;
  left: 16px;
  right: 16px;
  height: 2px;
  background: var(--md-default-fg-color--lightest, rgba(0,0,0,0.12));
  z-index: 0;
}
.bn-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  z-index: 1;
}
.bn-step-dot {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--md-code-bg-color, #f5f5f5);
  border: 2px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  color: var(--md-default-fg-color, #333);
  transition: all 0.25s ease;
}
.bn-step.active .bn-step-dot {
  background: var(--md-primary-bg-color, #009688);
  border-color: var(--md-primary-bg-color, #009688);
  color: white;
}
.bn-step.done .bn-step-dot {
  background: #22c55e;
  border-color: #22c55e;
  color: white;
}
.bn-step-label {
  font-size: 11px;
  color: var(--md-default-fg-color, #333);
  opacity: 0.6;
  text-align: center;
  max-width: 64px;
}
.bn-step.active .bn-step-label {
  opacity: 1;
  font-weight: 600;
  color: var(--md-primary-bg-color, #009688);
}
.bn-panel { display: none; }
.bn-panel.bn-active { display: block; }
.bn-heading {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 0.35rem;
  color: var(--md-default-fg-color, #333);
}
.bn-subtext {
  font-size: 0.88rem;
  color: var(--md-default-fg-color, #333);
  opacity: 0.7;
  margin-bottom: 1.5rem;
}
/* Persona cards */
.bn-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 1.5rem;
}
@media (max-width: 500px) { .bn-grid { grid-template-columns: 1fr; } }
.bn-card {
  background: var(--md-code-bg-color, #f5f5f5);
  border: 2px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12));
  border-radius: 8px;
  padding: 16px;
  cursor: pointer;
  transition: border-color 0.2s, transform 0.15s;
}
.bn-card:hover { border-color: var(--md-primary-bg-color, #009688); transform: translateY(-2px); }
.bn-card.bn-selected {
  border-color: var(--md-primary-bg-color, #009688);
  background: rgba(0, 150, 136, 0.07);
}
.bn-card-icon { font-size: 1.9rem; display: block; margin-bottom: 8px; }
.bn-card-title { font-weight: 700; font-size: 0.92rem; margin-bottom: 4px; color: var(--md-default-fg-color, #333); }
.bn-card-desc { font-size: 0.78rem; color: var(--md-default-fg-color, #333); opacity: 0.7; }
.bn-route-tag {
  display: inline-block;
  margin-top: 8px;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.72rem;
  font-weight: 700;
  background: var(--md-primary-bg-color, #009688);
  color: white;
}
/* Context fields */
.bn-fields { display: flex; flex-direction: column; gap: 16px; margin-bottom: 1.5rem; }
.bn-field-label { font-weight: 600; font-size: 0.88rem; color: var(--md-default-fg-color, #333); margin-bottom: 6px; }
.bn-select-wrap select {
  width: 100%;
  padding: 9px 12px;
  border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.2));
  border-radius: 6px;
  background: var(--md-code-bg-color, #f5f5f5);
  color: var(--md-default-fg-color, #333);
  font-size: 0.88rem;
  cursor: pointer;
}
.bn-radio-list { display: flex; flex-direction: column; gap: 8px; }
.bn-radio-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12));
  border-radius: 6px;
  cursor: pointer;
  background: var(--md-code-bg-color, #f5f5f5);
  font-size: 0.88rem;
  color: var(--md-default-fg-color, #333);
  transition: border-color 0.15s;
}
.bn-radio-item:hover { border-color: var(--md-primary-bg-color, #009688); }
.bn-radio-item input[type="radio"] { accent-color: var(--md-primary-bg-color, #009688); }
/* Maturity scan */
.bn-scan-meta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.bn-scan-bar { height: 5px; background: var(--md-default-fg-color--lightest, rgba(0,0,0,0.1)); border-radius: 3px; overflow: hidden; flex: 1; margin-right: 12px; }
.bn-scan-fill { height: 100%; background: var(--md-primary-bg-color, #009688); border-radius: 3px; transition: width 0.3s; }
.bn-scan-count { font-size: 0.78rem; color: var(--md-default-fg-color, #333); opacity: 0.65; white-space: nowrap; }
.bn-dimension {
  background: var(--md-code-bg-color, #f5f5f5);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
}
.bn-dim-label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--md-primary-bg-color, #009688);
  margin-bottom: 14px;
}
.bn-q-item { margin-bottom: 16px; }
.bn-q-item:last-child { margin-bottom: 0; }
.bn-q-text { font-size: 0.88rem; font-weight: 500; margin-bottom: 8px; color: var(--md-default-fg-color, #333); }
.bn-score-row { display: flex; gap: 6px; }
.bn-score-btn {
  flex: 1;
  padding: 7px 4px;
  border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.15));
  border-radius: 5px;
  background: var(--md-default-bg-color, #fff);
  color: var(--md-default-fg-color, #333);
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: all 0.15s;
}
.bn-score-btn:hover { border-color: var(--md-primary-bg-color, #009688); color: var(--md-primary-bg-color, #009688); }
.bn-score-btn.bn-sel {
  background: var(--md-primary-bg-color, #009688);
  border-color: var(--md-primary-bg-color, #009688);
  color: white;
}
.bn-score-hints { display: flex; margin-top: 4px; }
.bn-score-hint { flex: 1; font-size: 0.68rem; color: var(--md-default-fg-color, #333); opacity: 0.55; text-align: center; }
/* Navigation buttons */
.bn-nav { display: flex; justify-content: space-between; align-items: center; margin-top: 1.75rem; }
.bn-btn {
  padding: 10px 22px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  font-size: 0.88rem;
  font-weight: 600;
  transition: all 0.15s;
}
.bn-btn-primary { background: var(--md-primary-bg-color, #009688); color: white; }
.bn-btn-primary:hover:not(:disabled) { opacity: 0.88; transform: translateY(-1px); }
.bn-btn-primary:disabled { opacity: 0.35; cursor: not-allowed; }
.bn-btn-ghost {
  background: transparent;
  color: var(--md-default-fg-color, #333);
  border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.2));
}
.bn-btn-ghost:hover { border-color: var(--md-primary-bg-color, #009688); color: var(--md-primary-bg-color, #009688); }
/* Results */
.bn-result-center { text-align: center; padding-bottom: 12px; }
.bn-profile-pill {
  display: inline-block;
  padding: 8px 22px;
  border-radius: 24px;
  font-size: 1.05rem;
  font-weight: 700;
  color: white;
  margin-bottom: 6px;
}
.bn-pill-explorer { background: #0ea5e9; }
.bn-pill-builder { background: #f59e0b; }
.bn-pill-visionary { background: #8b5cf6; }
.bn-score-meta { font-size: 0.82rem; color: var(--md-default-fg-color, #333); opacity: 0.65; margin-bottom: 1.5rem; }
.bn-start-box {
  background: var(--md-code-bg-color, #f5f5f5);
  border-left: 4px solid var(--md-primary-bg-color, #009688);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 1.25rem;
  text-align: left;
}
.bn-start-title { font-weight: 700; font-size: 0.95rem; color: var(--md-default-fg-color, #333); margin-bottom: 4px; }
.bn-start-desc { font-size: 0.82rem; color: var(--md-default-fg-color, #333); opacity: 0.7; margin-bottom: 12px; }
.bn-actions-title { font-weight: 700; font-size: 0.9rem; color: var(--md-default-fg-color, #333); margin-bottom: 10px; text-align: left; }
.bn-action {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
  border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12));
  border-radius: 7px;
  margin-bottom: 8px;
  text-decoration: none !important;
  color: inherit;
  background: var(--md-default-bg-color, #fff);
  transition: all 0.15s;
}
.bn-action:hover { border-color: var(--md-primary-bg-color, #009688); background: rgba(0,150,136,0.04); }
.bn-action-num {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--md-primary-bg-color, #009688);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  font-weight: 700;
  flex-shrink: 0;
}
.bn-action-name { font-weight: 600; font-size: 0.88rem; color: var(--md-primary-bg-color, #009688); display: block; }
.bn-action-hint { font-size: 0.78rem; color: var(--md-default-fg-color, #333); opacity: 0.65; display: block; margin-top: 2px; }
.bn-restart-link { text-align: center; font-size: 0.82rem; color: var(--md-primary-bg-color, #009688); cursor: pointer; text-decoration: underline; }
</style>

<!-- Progress indicator -->

<div class="bn-progress-bar-outer">
  <div class="bn-step active" id="bn-s1"><div class="bn-step-dot">1</div><div class="bn-step-label">Uw Rol</div></div>
  <div class="bn-step" id="bn-s2"><div class="bn-step-dot">2</div><div class="bn-step-label">Context</div></div>
  <div class="bn-step" id="bn-s3"><div class="bn-step-dot">3</div><div class="bn-step-label">Maturity</div></div>
  <div class="bn-step" id="bn-s4"><div class="bn-step-dot">4</div><div class="bn-step-label">Resultaat</div></div>
</div>

<!-- Stap 1: Rol -->

<div class="bn-panel bn-active" id="bn-p1">
  <div class="bn-heading">Wie bent u?</div>
  <div class="bn-subtext">Uw rol bepaalt welke modules centraal staan in uw gepersonaliseerde route.</div>
  <div class="bn-grid">
    <div class="bn-card" data-persona="pm" onclick="bnSelect(this)">
      <span class="bn-card-icon">📋</span>
      <div class="bn-card-title">AI Projectmanager</div>
      <div class="bn-card-desc">U beheert AI-projecten en stuurt het team aan op voortgang en scope.</div>
      <span class="bn-route-tag">Route A</span>
    </div>
    <div class="bn-card" data-persona="tech" onclick="bnSelect(this)">
      <span class="bn-card-icon">⚙️</span>
      <div class="bn-card-title">Tech Lead / Developer</div>
      <div class="bn-card-desc">U bouwt en implementeert AI-systemen en technische infrastructuur.</div>
      <span class="bn-route-tag">Route B</span>
    </div>
    <div class="bn-card" data-persona="guardian" onclick="bnSelect(this)">
      <span class="bn-card-icon">🛡️</span>
      <div class="bn-card-title">AI Guardian / Compliance</div>
      <div class="bn-card-desc">U bewaakt ethiek, risicobeheer en naleving van regelgeving.</div>
      <span class="bn-route-tag">Route C</span>
    </div>
    <div class="bn-card" data-persona="caio" onclick="bnSelect(this)">
      <span class="bn-card-icon">🎯</span>
      <div class="bn-card-title">CAIO / Management Team</div>
      <div class="bn-card-desc">U stuurt AI-strategie op directieniveau en neemt investeringsbeslissingen.</div>
      <span class="bn-route-tag">Route D</span>
    </div>
  </div>
  <div class="bn-nav">
    <div></div>
    <button class="bn-btn bn-btn-primary" id="bn-next1" onclick="bnGo(2)" disabled>Volgende →</button>
  </div>
</div>

<!-- Stap 2: Context -->

<div class="bn-panel" id="bn-p2">
  <div class="bn-heading">Uw Organisatiecontext</div>
  <div class="bn-subtext">Drie snelle vragen — dit duurt minder dan een minuut.</div>
  <div class="bn-fields">
    <div>
      <div class="bn-field-label">Organisatietype</div>
      <div class="bn-select-wrap">
        <select id="bn-org" onchange="bnCheckContext()">
          <option value="">— Selecteer —</option>
          <option value="public">Publieke sector (overheid)</option>
          <option value="private">Privaat bedrijf (MKB)</option>
          <option value="enterprise">Groot bedrijf (enterprise)</option>
          <option value="ngo">Non-profit / NGO</option>
          <option value="startup">Start-up / Scale-up</option>
        </select>
      </div>
    </div>
    <div>
      <div class="bn-field-label">Primaire AI-doelstelling</div>
      <div class="bn-select-wrap">
        <select id="bn-goal" onchange="bnCheckContext()">
          <option value="">— Selecteer —</option>
          <option value="efficiency">Efficiëntie &amp; automatisering</option>
          <option value="innovation">Innovatie &amp; nieuwe diensten</option>
          <option value="compliance">Compliance &amp; risicobeheersing</option>
          <option value="customer">Klantervaring verbeteren</option>
          <option value="insight">Data-inzichten &amp; besluitvorming</option>
        </select>
      </div>
    </div>
    <div>
      <div class="bn-field-label">Risicotolerantie</div>
      <div class="bn-radio-list">
        <label class="bn-radio-item"><input type="radio" name="bn-risk" value="low" onchange="bnCheckContext()"> 🟢 Laag — Voorzichtig, gefaseerde aanpak, sterke governance</label>
        <label class="bn-radio-item"><input type="radio" name="bn-risk" value="medium" onchange="bnCheckContext()"> 🟡 Gemiddeld — Balans tussen snelheid en controle</label>
        <label class="bn-radio-item"><input type="radio" name="bn-risk" value="high" onchange="bnCheckContext()"> 🔴 Hoog — Snel itereren en leren, controleer achteraf</label>
      </div>
    </div>
  </div>
  <div class="bn-nav">
    <button class="bn-btn bn-btn-ghost" onclick="bnGo(1)">← Terug</button>
    <button class="bn-btn bn-btn-primary" id="bn-next2" onclick="bnGo(3)" disabled>Volgende →</button>
  </div>
</div>

<!-- Stap 3: Maturity Scan -->

<div class="bn-panel" id="bn-p3">
  <div class="bn-heading">10-Vragen Maturity Scan</div>
  <div class="bn-subtext">Geef elke stelling een score van 1 (laag/niet) tot 4 (hoog/volledig). Circa 3 minuten.</div>
  <div class="bn-scan-meta">
    <div class="bn-scan-bar"><div class="bn-scan-fill" id="bn-fill" style="width:0%"></div></div>
    <div class="bn-scan-count" id="bn-cnt">0 / 10</div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimensie A — Strategie &amp; Leiderschap</div>
    <div class="bn-q-item">
      <div class="bn-q-text">1. AI is expliciet opgenomen in onze meerjarenplanning.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="1" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="1" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="1" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="1" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Niet</span><span class="bn-score-hint">Sporadisch</span><span class="bn-score-hint">Gedeeltelijk</span><span class="bn-score-hint">Volledig</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">2. We stoppen actief projecten die geen aantoonbare waarde leveren.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="2" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="2" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="2" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="2" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Nooit</span><span class="bn-score-hint">Zelden</span><span class="bn-score-hint">Soms</span><span class="bn-score-hint">Systematisch</span></div>
    </div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimensie B — Technische Capaciteit</div>
    <div class="bn-q-item">
      <div class="bn-q-text">3. We hebben AI-systemen in productie (niet alleen demo's of pilots).</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="3" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="3" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="3" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="3" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Geen</span><span class="bn-score-hint">1 systeem</span><span class="bn-score-hint">2–5</span><span class="bn-score-hint">6+</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">4. Ons team begrijpt MLOps (monitoring, hertraining, versioning).</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="4" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="4" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="4" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="4" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Niet</span><span class="bn-score-hint">Beperkt</span><span class="bn-score-hint">Grotendeels</span><span class="bn-score-hint">Volledig</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">5. Onze data is toegankelijk, gedocumenteerd en van voldoende kwaliteit.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="5" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="5" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="5" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="5" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Niet</span><span class="bn-score-hint">Gedeeltelijk</span><span class="bn-score-hint">Grotendeels</span><span class="bn-score-hint">Volledig</span></div>
    </div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimensie C — Governance &amp; Risicobeheer</div>
    <div class="bn-q-item">
      <div class="bn-q-text">6. We hebben formele Rode Lijnen vastgesteld voor onze AI-systemen.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="6" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="6" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="6" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="6" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Geen</span><span class="bn-score-hint">Informeel</span><span class="bn-score-hint">Concept</span><span class="bn-score-hint">Formeel</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">7. Er is een aangewezen Guardian die ethische risico's actief bewaakt.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="7" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="7" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="7" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="7" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Geen</span><span class="bn-score-hint">Ad hoc</span><span class="bn-score-hint">Benoemd</span><span class="bn-score-hint">Volledig actief</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">8. We loggen AI-beslissingen voor audits en verantwoording.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="8" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="8" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="8" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="8" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Niet</span><span class="bn-score-hint">Gedeeltelijk</span><span class="bn-score-hint">Grotendeels</span><span class="bn-score-hint">Volledig</span></div>
    </div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimensie D — Organisatorisch Leervermogen</div>
    <div class="bn-q-item">
      <div class="bn-q-text">9. We voeren gestructureerde Lessons Learned uit na elk AI-project.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="9" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="9" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="9" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="9" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Nooit</span><span class="bn-score-hint">Incidenteel</span><span class="bn-score-hint">Regelmatig</span><span class="bn-score-hint">Altijd</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">10. We meten de impact van AI-projecten met concrete KPI's.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="10" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="10" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="10" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="10" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Niet</span><span class="bn-score-hint">Informeel</span><span class="bn-score-hint">Gedeeltelijk</span><span class="bn-score-hint">Structureel</span></div>
    </div>
  </div>

<div class="bn-nav">
    <button class="bn-btn bn-btn-ghost" onclick="bnGo(2)">← Terug</button>
    <button class="bn-btn bn-btn-primary" id="bn-next3" onclick="bnShowResults()" disabled>Bekijk resultaat →</button>
  </div>
</div>

<!-- Stap 4: Resultaat -->

<div class="bn-panel" id="bn-p4">
  <div id="bn-result"></div>
  <div class="bn-nav">
    <div class="bn-restart-link" onclick="bnRestart()">↺ Opnieuw starten</div>
    <div></div>
  </div>
</div>

<script>
var BN = {
  persona: null,
  scores: {}
};

var BN_ROUTES = {
  pm: {
    name: 'AI Projectmanager', route: 'A',
    Explorer: {
      start: { label: '30-Dagen Verkenner Kit', url: '../00-explorer-kit/', desc: 'Uw gepersonaliseerde startpakket met dag-tot-dag planning, vereenvoudigde templates en scaffold code' },
      actions: [
        { label: 'Project Charter Light invullen', url: '../00-explorer-kit/02-project-charter-light/', desc: 'Gestroomlijnd 1-pagina projectkader voor uw eerste AI-initiatief' },
        { label: 'Snelstart 90-Dagen Roadmap', url: '../12-90-dagen-roadmap/', desc: 'Van strategie naar actie in drie gefaseerde stappen' },
        { label: 'Fase 1: Verkenning &amp; Strategie', url: '../02-fase-ontdekking/01-doelstellingen/', desc: 'Begrijp het probleem volledig voordat u begint te bouwen' }
      ]
    },
    Builder: {
      start: { label: 'Gate Review Systeem', url: '../09-sjablonen/04-gate-reviews/checklist/', desc: 'Gestructureerd beslissingsraamwerk voor overgang naar productie' },
      actions: [
        { label: 'Realisatiefase Overzicht', url: '../04-fase-ontwikkeling/01-doelstellingen/', desc: 'Van proof-of-concept naar productieklaar systeem' },
        { label: 'Validatierapport Template', url: '../09-sjablonen/07-validatie-bewijs/validatierapport/', desc: 'Documenteer het bewijs dat uw systeem werkt' },
        { label: 'Monitoring &amp; Optimalisatie', url: '../06-fase-monitoring/01-doelstellingen/', desc: 'Prestatiebewaking en drift-detectie na go-live' }
      ]
    },
    Visionary: {
      start: { label: 'De Drie Transformatietracks', url: '../14-drie-tracks/', desc: 'Strategisch groeiperspectief voor organisaties die AI op schaal inzetten' },
      actions: [
        { label: 'Accelerators Overzicht', url: '../15-accelerators/', desc: 'Herbruikbare componenten voor versnelde AI-uitrol' },
        { label: 'Doorlopende Verbetering', url: '../10-doorlopende-verbetering/', desc: 'Kaizen, retrospectives en continue optimalisatie' },
        { label: 'Waarderealisatie (benefits realization)', url: '../10-doorlopende-verbetering/04-waarderealisatie (benefits realization)/', desc: 'Aantoon en beheer de ROI van uw AI-portfolio' }
      ]
    }
  },
  tech: {
    name: 'Tech Lead / Developer', route: 'B',
    Explorer: {
      start: { label: 'SDD Patroon (Spec-Driven Development)', url: '../04-fase-ontwikkeling/05-sdd-patroon/', desc: 'Test-first aanpak voor betrouwbare en traceerbare AI-systemen' },
      actions: [
        { label: 'Technische Standaarden Overzicht', url: '../08-technische-standaarden/', desc: 'Architectuur, MLOps-patronen en data pipeline standaarden' },
        { label: 'Data Pipelines', url: '../08-technische-standaarden/02-data-pipelines/', desc: 'Bouw het datafundament voor uw eerste AI-project' },
        { label: 'Scaffold Code (30-Dagen Kit)', url: '../00-explorer-kit/05-scaffold-code/', desc: 'Python notebooks voor RAG, e-mailclassificatie en contentgeneratie' }
      ]
    },
    Builder: {
      start: { label: 'MLOps Standaarden', url: '../08-technische-standaarden/01-mloops-standaarden/', desc: 'Production-grade monitoring, deployment en model lifecycle management' },
      actions: [
        { label: 'Drift Detectie', url: '../06-fase-monitoring/05-drift-detectie/', desc: 'Detecteer prestatieverschuiving vroeg en geautomatiseerd' },
        { label: 'Model Governance', url: '../08-technische-standaarden/03-model-governance/', desc: 'Versiebeheer, reproducibility en audit trails voor modellen' },
        { label: 'Test Frameworks', url: '../08-technische-standaarden/04-test-frameworks/', desc: 'Geautomatiseerd testen van AI-gedrag en grensgevallen' }
      ]
    },
    Visionary: {
      start: { label: 'AI Architectuur op Schaal', url: '../08-technische-standaarden/05-ai-architectuur/', desc: 'Enterprise AI-architectuurpatronen voor complexe omgevingen' },
      actions: [
        { label: 'Operationele Accelerators', url: '../15-accelerators/02-operationele-herontwerp-accelerators/', desc: 'Herbruikbare componenten voor snellere uitrol van nieuwe use cases' },
        { label: 'Model Governance (Geavanceerd)', url: '../08-technische-standaarden/03-model-governance/', desc: 'Beheer een vloot van AI-modellen op portfolio-niveau' },
        { label: 'Metrics Dashboards', url: '../10-doorlopende-verbetering/03-metrics-dashboards/', desc: 'KPI-dashboards voor AI-portfolio monitoring' }
      ]
    }
  },
  guardian: {
    name: 'AI Guardian / Compliance', route: 'C',
    Explorer: {
      start: { label: 'Risico Pre-Scan Quick', url: '../00-explorer-kit/03-risk-prescan-quick/', desc: 'Snel risicoprofiel van uw AI-voornemen in 15 vragen' },
      actions: [
        { label: 'EU AI Act Overzicht', url: '../07-compliance-hub/01-eu-ai-act/', desc: 'Wat betekent de Europese AI-wet voor uw organisatie?' },
        { label: 'Risicoclassificatie Framework', url: '../01-ai-native-fundamenten/05-risicoclassificatie/', desc: 'Bepaal het risiconiveau van uw specifieke use case' },
        { label: 'AI-Samenwerkingsmodi', url: '../00-strategisch-kader/06-has-h-niveaus/', desc: 'Welke mate van menselijk toezicht is vereist?' }
      ]
    },
    Builder: {
      start: { label: 'Compliance Hub', url: '../07-compliance-hub/', desc: 'Centraal overzicht van alle compliance-vereisten per fase' },
      actions: [
        { label: 'Ethische Richtlijnen', url: '../07-compliance-hub/03-ethische-richtlijnen/', desc: 'Operationele ethische kaders vertaald naar dagelijkse praktijk' },
        { label: 'Validatie Eisen', url: '../07-compliance-hub/04-validatie-eisen/', desc: 'Bewijsstandaarden die nodig zijn voor audit-compliance' },
        { label: 'Volledige Risicoanalyse', url: '../09-sjablonen/03-risicoanalyse/template/', desc: 'Volledige risicobeoordeling documenteren voor Gate Review' }
      ]
    },
    Visionary: {
      start: { label: 'Incident Respons Procedure', url: '../07-compliance-hub/05-incidentrespons/', desc: 'Gestructureerde aanpak bij AI-incidenten op organisatieschaal' },
      actions: [
        { label: 'Model Governance', url: '../08-technische-standaarden/03-model-governance/', desc: 'Compliance governance voor een portfolio van AI-systemen' },
        { label: 'Doorlopende Verbetering', url: '../10-doorlopende-verbetering/', desc: 'Systematisch leren en verbeteren van compliance-processen' },
        { label: 'Track Volgorde (Compliance)', url: '../14-drie-tracks/04-track-sequentie/', desc: 'Compliance-overwegingen bij organisatiebrede AI-transformatie' }
      ]
    }
  },
  caio: {
    name: 'CAIO / Management Team', route: 'D',
    Explorer: {
      start: { label: 'Management Samenvatting', url: '../00-strategisch-kader/00-executive-summary/', desc: 'De volledige AI Project Blauwdruk in tien minuten begrijpen' },
      actions: [
        { label: 'Organisatieprofielen &amp; Maturity', url: '../13-organisatieprofielen/', desc: 'Waar staat uw organisatie in de AI-volwassenheidsreis?' },
        { label: 'Snelstart 90-Dagen Roadmap', url: '../12-90-dagen-roadmap/', desc: 'Concrete roadmap van strategie naar eerste resultaten' },
        { label: 'Governance Model', url: '../00-strategisch-kader/03-governance-model/', desc: 'Wie beslist wat — rollen, verantwoordelijkheden en escalatie' }
      ]
    },
    Builder: {
      start: { label: 'De Drie Transformatietracks', url: '../14-drie-tracks/', desc: 'Strategisch groeiperspectief voor uw AI-transformatieambities' },
      actions: [
        { label: 'Governance Model (Formaliseer)', url: '../00-strategisch-kader/03-governance-model/', desc: 'Zet uw AI-governance op voor de lange termijn' },
        { label: 'Doorlopende Verbetering', url: '../10-doorlopende-verbetering/', desc: 'Van projectmentaliteit naar programma-denken' },
        { label: 'Waarderealisatie (benefits realization)', url: '../10-doorlopende-verbetering/04-waarderealisatie (benefits realization)/', desc: 'Rapporteer ROI aan het management en de raad van bestuur' }
      ]
    },
    Visionary: {
      start: { label: 'Accelerators voor Schaal', url: '../15-accelerators/', desc: 'Versnellingsopties voor AI-organisaties die al op schaal opereren' },
      actions: [
        { label: 'Organisatorische Heruitvinding', url: '../00-strategisch-kader/07-organisatorische-heruitvinding/', desc: 'AI als fundament van uw bedrijfsmodel en cultuur' },
        { label: 'Strategische Heruitvinding (Track)', url: '../14-drie-tracks/01-strategische-heruitvinding/', desc: 'Strategische transformatie op de lange termijn' },
        { label: 'Waarderealisatie (benefits realization) op Portfolio-niveau', url: '../10-doorlopende-verbetering/04-waarderealisatie (benefits realization)/', desc: 'Beheer en communiceer de waarde van uw AI-portfolio' }
      ]
    }
  }
};

function bnSelect(card) {
  document.querySelectorAll('.bn-card').forEach(function(c) { c.classList.remove('bn-selected'); });
  card.classList.add('bn-selected');
  BN.persona = card.dataset.persona;
  document.getElementById('bn-next1').disabled = false;
}

function bnCheckContext() {
  var org = document.getElementById('bn-org').value;
  var goal = document.getElementById('bn-goal').value;
  var risk = document.querySelector('input[name="bn-risk"]:checked');
  document.getElementById('bn-next2').disabled = !(org && goal && risk);
}

function bnScore(btn) {
  var q = btn.dataset.q;
  document.querySelectorAll('.bn-score-btn[data-q="' + q + '"]').forEach(function(b) { b.classList.remove('bn-sel'); });
  btn.classList.add('bn-sel');
  BN.scores[q] = parseInt(btn.dataset.v);
  var n = Object.keys(BN.scores).length;
  document.getElementById('bn-fill').style.width = (n / 10 * 100) + '%';
  document.getElementById('bn-cnt').textContent = n + ' / 10';
  document.getElementById('bn-next3').disabled = (n < 10);
}

function bnGetProfile(total) {
  if (total <= 20) return 'Explorer';
  if (total <= 32) return 'Builder';
  return 'Visionary';
}

function bnShowResults() {
  var total = 0;
  for (var k in BN.scores) { total += BN.scores[k]; }
  var profile = bnGetProfile(total);
  var labels = { Explorer: 'De Verkenner', Builder: 'De Bouwer', Visionary: 'De Visionair' };
  var pillClass = { Explorer: 'bn-pill-explorer', Builder: 'bn-pill-builder', Visionary: 'bn-pill-visionary' };
  var route = BN_ROUTES[BN.persona];
  var data = route[profile];
  var pct = Math.round(total / 40 * 100);

  var acts = data.actions.map(function(a, i) {
    return '<a class="bn-action" href="' + a.url + '">' +
      '<div class="bn-action-num">' + (i+1) + '</div>' +
      '<div><span class="bn-action-name">' + a.label + '</span><span class="bn-action-hint">' + a.desc + '</span></div>' +
      '</a>';
  }).join('');

  document.getElementById('bn-result').innerHTML =
    '<div class="bn-result-center">' +
      '<div class="bn-profile-pill ' + pillClass[profile] + '">' + labels[profile] + '</div><br>' +
      '<div class="bn-score-meta">Score: ' + total + '/40 (' + pct + '%) &nbsp;·&nbsp; Route ' + route.route + ': ' + route.name + '</div>' +
    '</div>' +
    '<div class="bn-start-box">' +
      '<div class="bn-start-title">📍 Aanbevolen startpunt: ' + data.start.label + '</div>' +
      '<div class="bn-start-desc">' + data.start.desc + '</div>' +
      '<a href="' + data.start.url + '" class="bn-btn bn-btn-primary" style="display:inline-block;text-decoration:none!important;">Begin hier →</a>' +
    '</div>' +
    '<div class="bn-actions-title">Eerste 3 aanbevolen acties</div>' +
    acts;

  bnGo(4);
}

function bnGo(step) {
  document.querySelectorAll('.bn-panel').forEach(function(p) { p.classList.remove('bn-active'); });
  document.getElementById('bn-p' + step).classList.add('bn-active');
  document.querySelectorAll('.bn-step').forEach(function(d, i) {
    var n = i + 1;
    var dot = d.querySelector('.bn-step-dot');
    d.classList.remove('active', 'done');
    if (n < step) { d.classList.add('done'); dot.textContent = '✓'; }
    else if (n === step) { d.classList.add('active'); dot.textContent = n; }
    else { dot.textContent = n; }
  });
  window.scrollTo({ top: document.getElementById('blueprint-navigator').offsetTop - 80, behavior: 'smooth' });
}

function bnRestart() {
  BN = { persona: null, scores: {} };
  document.querySelectorAll('.bn-card').forEach(function(c) { c.classList.remove('bn-selected'); });
  document.getElementById('bn-next1').disabled = true;
  document.getElementById('bn-org').value = '';
  document.getElementById('bn-goal').value = '';
  document.querySelectorAll('input[name="bn-risk"]').forEach(function(r) { r.checked = false; });
  document.getElementById('bn-next2').disabled = true;
  document.querySelectorAll('.bn-score-btn').forEach(function(b) { b.classList.remove('bn-sel'); });
  document.getElementById('bn-fill').style.width = '0%';
  document.getElementById('bn-cnt').textContent = '0 / 10';
  document.getElementById('bn-next3').disabled = true;
  bnGo(1);
}
</script>

</div>

______________________________________________________________________

## Handmatige Route-overzicht

Wilt u direct naar een route zonder de wizard? Gebruik dan de tabel hieronder.

| Profiel       | Score | Route A (PM)                                               | Route B (Tech)                                                           | Route C (Guardian)                                           | Route D (CAIO)                                                              |
| :------------ | :---- | :--------------------------------------------------------- | :----------------------------------------------------------------------- | :----------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Verkenner** | 10–20 | [30-Dagen Kit](../00-explorer-kit/)                        | [SDD Patroon](../04-fase-ontwikkeling/05-sdd-patroon/)                   | [Pre-Scan Quick](../00-explorer-kit/03-risk-prescan-quick/)  | [Exec Summary](../00-strategisch-kader/00-executive-summary/)               |
| **Bouwer**    | 21–32 | [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist/) | [MLOps Standaarden](../08-technische-standaarden/01-mloops-standaarden/) | [Compliance Hub](../07-compliance-hub/)                      | [Drie Tracks](../14-drie-tracks/)                                           |
| **Visionair** | 33–40 | [Accelerators](../15-accelerators/)                        | [AI Architectuur](../08-technische-standaarden/05-ai-architectuur/)      | [Incident Respons](../07-compliance-hub/05-incidentrespons/) | [Heruitvinding](../00-strategisch-kader/07-organisatorische-heruitvinding/) |

______________________________________________________________________

## Gerelateerde Modules

- [Organisatieprofielen (Verkenner / Bouwer / Visionair)](../13-organisatieprofielen/index.md)
- [Profielbeoordeling (uitgebreide versie)](../13-organisatieprofielen/04-profiel-beoordeling.md)
- [30-Dagen Verkenner Kit](../00-explorer-kit/index.md)
- [Snelstart 90-Dagen Roadmap](../12-90-dagen-roadmap/index.md)
