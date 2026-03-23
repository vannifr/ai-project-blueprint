---
versie: '1.0'
description: Blueprint Navigator — interactive guide to find the right module for your AI project phase, role, or challenge. Start here to orient yourself in the AI Project Blueprint.
type: index
layer: 1
answers: [What does the Blueprint Navigator section contain?]
---

# Blueprint Navigator

Answer four steps — your role, your context, and ten maturity questions — and the Navigator points you directly to your starting position in the blueprint.

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
.bn-heading { font-size: 1.15rem; font-weight: 700; margin-bottom: 0.35rem; color: var(--md-default-fg-color, #333); }
.bn-subtext { font-size: 0.88rem; color: var(--md-default-fg-color, #333); opacity: 0.7; margin-bottom: 1.5rem; }
.bn-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 1.5rem; }
@media (max-width: 500px) { .bn-grid { grid-template-columns: 1fr; } }
.bn-card { background: var(--md-code-bg-color, #f5f5f5); border: 2px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12)); border-radius: 8px; padding: 16px; cursor: pointer; transition: border-color 0.2s, transform 0.15s; }
.bn-card:hover { border-color: var(--md-primary-bg-color, #009688); transform: translateY(-2px); }
.bn-card.bn-selected { border-color: var(--md-primary-bg-color, #009688); background: rgba(0, 150, 136, 0.07); }
.bn-card-icon { font-size: 1.9rem; display: block; margin-bottom: 8px; }
.bn-card-title { font-weight: 700; font-size: 0.92rem; margin-bottom: 4px; color: var(--md-default-fg-color, #333); }
.bn-card-desc { font-size: 0.78rem; color: var(--md-default-fg-color, #333); opacity: 0.7; }
.bn-route-tag { display: inline-block; margin-top: 8px; padding: 2px 10px; border-radius: 12px; font-size: 0.72rem; font-weight: 700; background: var(--md-primary-bg-color, #009688); color: white; }
.bn-fields { display: flex; flex-direction: column; gap: 16px; margin-bottom: 1.5rem; }
.bn-field-label { font-weight: 600; font-size: 0.88rem; color: var(--md-default-fg-color, #333); margin-bottom: 6px; }
.bn-select-wrap select { width: 100%; padding: 9px 12px; border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.2)); border-radius: 6px; background: var(--md-code-bg-color, #f5f5f5); color: var(--md-default-fg-color, #333); font-size: 0.88rem; cursor: pointer; }
.bn-radio-list { display: flex; flex-direction: column; gap: 8px; }
.bn-radio-item { display: flex; align-items: center; gap: 10px; padding: 9px 12px; border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12)); border-radius: 6px; cursor: pointer; background: var(--md-code-bg-color, #f5f5f5); font-size: 0.88rem; color: var(--md-default-fg-color, #333); transition: border-color 0.15s; }
.bn-radio-item:hover { border-color: var(--md-primary-bg-color, #009688); }
.bn-radio-item input[type="radio"] { accent-color: var(--md-primary-bg-color, #009688); }
.bn-scan-meta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.bn-scan-bar { height: 5px; background: var(--md-default-fg-color--lightest, rgba(0,0,0,0.1)); border-radius: 3px; overflow: hidden; flex: 1; margin-right: 12px; }
.bn-scan-fill { height: 100%; background: var(--md-primary-bg-color, #009688); border-radius: 3px; transition: width 0.3s; }
.bn-scan-count { font-size: 0.78rem; color: var(--md-default-fg-color, #333); opacity: 0.65; white-space: nowrap; }
.bn-dimension { background: var(--md-code-bg-color, #f5f5f5); border-radius: 8px; padding: 16px; margin-bottom: 16px; }
.bn-dim-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--md-primary-bg-color, #009688); margin-bottom: 14px; }
.bn-q-item { margin-bottom: 16px; }
.bn-q-item:last-child { margin-bottom: 0; }
.bn-q-text { font-size: 0.88rem; font-weight: 500; margin-bottom: 8px; color: var(--md-default-fg-color, #333); }
.bn-score-row { display: flex; gap: 6px; }
.bn-score-btn { flex: 1; padding: 7px 4px; border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.15)); border-radius: 5px; background: var(--md-default-bg-color, #fff); color: var(--md-default-fg-color, #333); font-size: 0.82rem; font-weight: 600; cursor: pointer; text-align: center; transition: all 0.15s; }
.bn-score-btn:hover { border-color: var(--md-primary-bg-color, #009688); color: var(--md-primary-bg-color, #009688); }
.bn-score-btn.bn-sel { background: var(--md-primary-bg-color, #009688); border-color: var(--md-primary-bg-color, #009688); color: white; }
.bn-score-hints { display: flex; margin-top: 4px; }
.bn-score-hint { flex: 1; font-size: 0.68rem; color: var(--md-default-fg-color, #333); opacity: 0.55; text-align: center; }
.bn-nav { display: flex; justify-content: space-between; align-items: center; margin-top: 1.75rem; }
.bn-btn { padding: 10px 22px; border-radius: 6px; border: none; cursor: pointer; font-size: 0.88rem; font-weight: 600; transition: all 0.15s; }
.bn-btn-primary { background: var(--md-primary-bg-color, #009688); color: white; }
.bn-btn-primary:hover:not(:disabled) { opacity: 0.88; transform: translateY(-1px); }
.bn-btn-primary:disabled { opacity: 0.35; cursor: not-allowed; }
.bn-btn-ghost { background: transparent; color: var(--md-default-fg-color, #333); border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.2)); }
.bn-btn-ghost:hover { border-color: var(--md-primary-bg-color, #009688); color: var(--md-primary-bg-color, #009688); }
.bn-result-center { text-align: center; padding-bottom: 12px; }
.bn-profile-pill { display: inline-block; padding: 8px 22px; border-radius: 24px; font-size: 1.05rem; font-weight: 700; color: white; margin-bottom: 6px; }
.bn-pill-explorer { background: #0ea5e9; }
.bn-pill-builder { background: #f59e0b; }
.bn-pill-visionary { background: #8b5cf6; }
.bn-score-meta { font-size: 0.82rem; color: var(--md-default-fg-color, #333); opacity: 0.65; margin-bottom: 1.5rem; }
.bn-start-box { background: var(--md-code-bg-color, #f5f5f5); border-left: 4px solid var(--md-primary-bg-color, #009688); border-radius: 8px; padding: 16px; margin-bottom: 1.25rem; text-align: left; }
.bn-start-title { font-weight: 700; font-size: 0.95rem; color: var(--md-default-fg-color, #333); margin-bottom: 4px; }
.bn-start-desc { font-size: 0.82rem; color: var(--md-default-fg-color, #333); opacity: 0.7; margin-bottom: 12px; }
.bn-actions-title { font-weight: 700; font-size: 0.9rem; color: var(--md-default-fg-color, #333); margin-bottom: 10px; text-align: left; }
.bn-action { display: flex; align-items: flex-start; gap: 12px; padding: 12px; border: 1px solid var(--md-default-fg-color--lightest, rgba(0,0,0,0.12)); border-radius: 7px; margin-bottom: 8px; text-decoration: none !important; color: inherit; background: var(--md-default-bg-color, #fff); transition: all 0.15s; }
.bn-action:hover { border-color: var(--md-primary-bg-color, #009688); background: rgba(0,150,136,0.04); }
.bn-action-num { width: 26px; height: 26px; border-radius: 50%; background: var(--md-primary-bg-color, #009688); color: white; display: flex; align-items: center; justify-content: center; font-size: 0.78rem; font-weight: 700; flex-shrink: 0; }
.bn-action-name { font-weight: 600; font-size: 0.88rem; color: var(--md-primary-bg-color, #009688); display: block; }
.bn-action-hint { font-size: 0.78rem; color: var(--md-default-fg-color, #333); opacity: 0.65; display: block; margin-top: 2px; }
.bn-restart-link { text-align: center; font-size: 0.82rem; color: var(--md-primary-bg-color, #009688); cursor: pointer; text-decoration: underline; }
</style>

<div class="bn-progress-bar-outer">
  <div class="bn-step active" id="bn-s1"><div class="bn-step-dot">1</div><div class="bn-step-label">Your Role</div></div>
  <div class="bn-step" id="bn-s2"><div class="bn-step-dot">2</div><div class="bn-step-label">Context</div></div>
  <div class="bn-step" id="bn-s3"><div class="bn-step-dot">3</div><div class="bn-step-label">Maturity</div></div>
  <div class="bn-step" id="bn-s4"><div class="bn-step-dot">4</div><div class="bn-step-label">Result</div></div>
</div>

<div class="bn-panel bn-active" id="bn-p1">
  <div class="bn-heading">Who are you?</div>
  <div class="bn-subtext">Your role determines which modules are most relevant for your personalised route.</div>
  <div class="bn-grid">
    <div class="bn-card" data-persona="pm" onclick="bnSelect(this)">
      <span class="bn-card-icon">📋</span>
      <div class="bn-card-title">AI Project Manager</div>
      <div class="bn-card-desc">You manage AI projects and steer the team on progress and scope.</div>
      <span class="bn-route-tag">Route A</span>
    </div>
    <div class="bn-card" data-persona="tech" onclick="bnSelect(this)">
      <span class="bn-card-icon">⚙️</span>
      <div class="bn-card-title">Tech Lead / Developer</div>
      <div class="bn-card-desc">You build and implement AI systems and technical infrastructure.</div>
      <span class="bn-route-tag">Route B</span>
    </div>
    <div class="bn-card" data-persona="guardian" onclick="bnSelect(this)">
      <span class="bn-card-icon">🛡️</span>
      <div class="bn-card-title">AI Guardian / Compliance</div>
      <div class="bn-card-desc">You oversee ethics, risk management and regulatory compliance.</div>
      <span class="bn-route-tag">Route C</span>
    </div>
    <div class="bn-card" data-persona="caio" onclick="bnSelect(this)">
      <span class="bn-card-icon">🎯</span>
      <div class="bn-card-title">CAIO / Management Team</div>
      <div class="bn-card-desc">You drive AI strategy at board level and make investment decisions.</div>
      <span class="bn-route-tag">Route D</span>
    </div>
  </div>
  <div class="bn-nav">
    <div></div>
    <button class="bn-btn bn-btn-primary" id="bn-next1" onclick="bnGo(2)" disabled>Next →</button>
  </div>
</div>

<div class="bn-panel" id="bn-p2">
  <div class="bn-heading">Your Organisational Context</div>
  <div class="bn-subtext">Three quick questions — less than a minute.</div>
  <div class="bn-fields">
    <div>
      <div class="bn-field-label">Organisation type</div>
      <div class="bn-select-wrap">
        <select id="bn-org" onchange="bnCheckContext()">
          <option value="">— Select —</option>
          <option value="public">Public sector (government)</option>
          <option value="private">Private company (SME)</option>
          <option value="enterprise">Large enterprise</option>
          <option value="ngo">Non-profit / NGO</option>
          <option value="startup">Start-up / Scale-up</option>
        </select>
      </div>
    </div>
    <div>
      <div class="bn-field-label">Primary AI objective</div>
      <div class="bn-select-wrap">
        <select id="bn-goal" onchange="bnCheckContext()">
          <option value="">— Select —</option>
          <option value="efficiency">Efficiency &amp; automation</option>
          <option value="innovation">Innovation &amp; new services</option>
          <option value="compliance">Compliance &amp; risk management</option>
          <option value="customer">Improving customer experience</option>
          <option value="insight">Data insights &amp; decision-making</option>
        </select>
      </div>
    </div>
    <div>
      <div class="bn-field-label">Risk tolerance</div>
      <div class="bn-radio-list">
        <label class="bn-radio-item"><input type="radio" name="bn-risk" value="low" onchange="bnCheckContext()"> 🟢 Low — Cautious, phased approach, strong governance</label>
        <label class="bn-radio-item"><input type="radio" name="bn-risk" value="medium" onchange="bnCheckContext()"> 🟡 Medium — Balance between speed and control</label>
        <label class="bn-radio-item"><input type="radio" name="bn-risk" value="high" onchange="bnCheckContext()"> 🔴 High — Move fast, learn quickly, validate afterwards</label>
      </div>
    </div>
  </div>
  <div class="bn-nav">
    <button class="bn-btn bn-btn-ghost" onclick="bnGo(1)">← Back</button>
    <button class="bn-btn bn-btn-primary" id="bn-next2" onclick="bnGo(3)" disabled>Next →</button>
  </div>
</div>

<div class="bn-panel" id="bn-p3">
  <div class="bn-heading">10-Question Maturity Scan</div>
  <div class="bn-subtext">Rate each statement from 1 (low/not at all) to 4 (high/fully). Approximately 3 minutes.</div>
  <div class="bn-scan-meta">
    <div class="bn-scan-bar"><div class="bn-scan-fill" id="bn-fill" style="width:0%"></div></div>
    <div class="bn-scan-count" id="bn-cnt">0 / 10</div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimension A — Strategy &amp; Leadership</div>
    <div class="bn-q-item">
      <div class="bn-q-text">1. AI is explicitly included in our multi-year planning.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="1" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="1" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="1" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="1" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Not at all</span><span class="bn-score-hint">Sporadically</span><span class="bn-score-hint">Partially</span><span class="bn-score-hint">Fully</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">2. We actively stop projects that deliver no demonstrable value.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="2" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="2" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="2" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="2" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Never</span><span class="bn-score-hint">Rarely</span><span class="bn-score-hint">Sometimes</span><span class="bn-score-hint">Systematically</span></div>
    </div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimension B — Technical Capacity</div>
    <div class="bn-q-item">
      <div class="bn-q-text">3. We have AI systems running in production (not just demos or pilots).</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="3" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="3" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="3" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="3" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">None</span><span class="bn-score-hint">1 system</span><span class="bn-score-hint">2–5</span><span class="bn-score-hint">6+</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">4. Our team understands MLOps (monitoring, retraining, versioning).</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="4" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="4" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="4" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="4" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Not at all</span><span class="bn-score-hint">Partially</span><span class="bn-score-hint">Mostly</span><span class="bn-score-hint">Fully</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">5. Our data is accessible, documented and of sufficient quality.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="5" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="5" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="5" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="5" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Not at all</span><span class="bn-score-hint">Partially</span><span class="bn-score-hint">Mostly</span><span class="bn-score-hint">Fully</span></div>
    </div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimension C — Governance &amp; Risk Management</div>
    <div class="bn-q-item">
      <div class="bn-q-text">6. We have formal Hard Boundaries established for our AI systems.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="6" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="6" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="6" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="6" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">None</span><span class="bn-score-hint">Informal</span><span class="bn-score-hint">Draft</span><span class="bn-score-hint">Formal</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">7. A designated Guardian actively monitors ethical risks.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="7" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="7" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="7" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="7" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">None</span><span class="bn-score-hint">Ad hoc</span><span class="bn-score-hint">Appointed</span><span class="bn-score-hint">Fully active</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">8. We log AI decisions for audits and accountability.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="8" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="8" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="8" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="8" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Not at all</span><span class="bn-score-hint">Partially</span><span class="bn-score-hint">Mostly</span><span class="bn-score-hint">Fully</span></div>
    </div>
  </div>

<div class="bn-dimension">
    <div class="bn-dim-label">Dimension D — Organisational Learning</div>
    <div class="bn-q-item">
      <div class="bn-q-text">9. We conduct structured Lessons Learned sessions after every AI project.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="9" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="9" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="9" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="9" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Never</span><span class="bn-score-hint">Occasionally</span><span class="bn-score-hint">Regularly</span><span class="bn-score-hint">Always</span></div>
    </div>
    <div class="bn-q-item">
      <div class="bn-q-text">10. We measure the impact of AI projects with concrete KPIs.</div>
      <div class="bn-score-row">
        <button class="bn-score-btn" data-q="10" data-v="1" onclick="bnScore(this)">1</button>
        <button class="bn-score-btn" data-q="10" data-v="2" onclick="bnScore(this)">2</button>
        <button class="bn-score-btn" data-q="10" data-v="3" onclick="bnScore(this)">3</button>
        <button class="bn-score-btn" data-q="10" data-v="4" onclick="bnScore(this)">4</button>
      </div>
      <div class="bn-score-hints"><span class="bn-score-hint">Not at all</span><span class="bn-score-hint">Informally</span><span class="bn-score-hint">Partially</span><span class="bn-score-hint">Structurally</span></div>
    </div>
  </div>

<div class="bn-nav">
    <button class="bn-btn bn-btn-ghost" onclick="bnGo(2)">← Back</button>
    <button class="bn-btn bn-btn-primary" id="bn-next3" onclick="bnShowResults()" disabled>View result →</button>
  </div>
</div>

<div class="bn-panel" id="bn-p4">
  <div id="bn-result"></div>
  <div class="bn-nav">
    <div class="bn-restart-link" onclick="bnRestart()">↺ Start over</div>
    <div></div>
  </div>
</div>

<script>
var BN = { persona: null, scores: {} };
var BN_ROUTES = {
  pm: {
    name: 'AI Project Manager', route: 'A',
    Explorer: {
      start: { label: '30-Day Explorer Kit', url: '../00-explorer-kit/', desc: 'Your personalised starter pack with day-by-day planning and simplified templates' },
      actions: [
        { label: 'Fill in Project Charter Light', url: '../00-explorer-kit/02-project-charter-light/', desc: 'Streamlined 1-page project framework for your first AI initiative' },
        { label: '90-Day Quick-Start Roadmap', url: '../12-90-dagen-roadmap/', desc: 'From strategy to action in three phased steps' },
        { label: 'Phase 1: Discovery \x26 Strategy', url: '../02-fase-ontdekking/01-doelstellingen/', desc: 'Fully understand the problem before you start building' }
      ]
    },
    Builder: {
      start: { label: 'Gate Review System', url: '../09-sjablonen/04-gate-reviews/checklist/', desc: 'Structured decision framework for the transition to production' },
      actions: [
        { label: 'Development Phase Overview', url: '../04-fase-ontwikkeling/01-doelstellingen/', desc: 'From proof-of-concept to production-ready system' },
        { label: 'Validation Report Template', url: '../09-sjablonen/07-validatie-bewijs/validatierapport/', desc: 'Document the evidence that your system works' },
        { label: 'Monitoring \x26 Optimisation', url: '../06-fase-monitoring/01-doelstellingen/', desc: 'Performance monitoring and drift detection after go-live' }
      ]
    },
    Visionary: {
      start: { label: 'The Three Transformation Tracks', url: '../14-drie-tracks/', desc: 'Strategic growth perspective for organisations scaling AI' },
      actions: [
        { label: 'Accelerators Overview', url: '../15-accelerators/', desc: 'Reusable components for accelerated AI roll-out' },
        { label: 'Continuous Improvement', url: '../10-doorlopende-verbetering/', desc: 'Kaizen, retrospectives and continuous optimisation' },
        { label: 'Benefits Realisation', url: '../10-doorlopende-verbetering/04-batenrealisatie/', desc: 'Demonstrate and manage ROI of your AI portfolio' }
      ]
    }
  },
  tech: {
    name: 'Tech Lead / Developer', route: 'B',
    Explorer: {
      start: { label: 'Specification-first Pattern', url: '../04-fase-ontwikkeling/05-sdd-patroon/', desc: 'Test-first approach for reliable and traceable AI systems' },
      actions: [
        { label: 'Technical Standards Overview', url: '../08-technische-standaarden/', desc: 'Architecture, MLOps patterns and data pipeline standards' },
        { label: 'Data Pipelines', url: '../08-technische-standaarden/02-data-pipelines/', desc: 'Build the data foundation for your first AI project' },
        { label: 'Engineering Patterns', url: '../04-fase-ontwikkeling/06-engineering-patterns/', desc: 'Proven patterns for safe AI development and code review' }
      ]
    },
    Builder: {
      start: { label: 'MLOps Standards', url: '../08-technische-standaarden/01-mloops-standaarden/', desc: 'Production-grade monitoring, deployment and model lifecycle management' },
      actions: [
        { label: 'Drift Detection', url: '../06-fase-monitoring/05-drift-detectie/', desc: 'Detect performance drift early and automatically' },
        { label: 'Model Governance', url: '../08-technische-standaarden/03-model-governance/', desc: 'Version control, reproducibility and audit trails for models' },
        { label: 'Test Frameworks', url: '../08-technische-standaarden/04-test-frameworks/', desc: 'Automated testing of AI behaviour and edge cases' }
      ]
    },
    Visionary: {
      start: { label: 'AI Architecture at Scale', url: '../08-technische-standaarden/05-ai-architectuur/', desc: 'Enterprise AI architecture patterns for complex environments' },
      actions: [
        { label: 'Operational Accelerators', url: '../15-accelerators/02-operationele-herontwerp-accelerators/', desc: 'Reusable components for faster roll-out of new use cases' },
        { label: 'Model Governance (Advanced)', url: '../08-technische-standaarden/03-model-governance/', desc: 'Manage a fleet of AI models at portfolio level' },
        { label: 'Metrics Dashboards', url: '../10-doorlopende-verbetering/03-metrics-dashboards/', desc: 'KPI dashboards for AI portfolio monitoring' }
      ]
    }
  },
  guardian: {
    name: 'AI Guardian / Compliance', route: 'C',
    Explorer: {
      start: { label: 'Quick Risk Pre-Scan', url: '../00-explorer-kit/03-risk-prescan-quick/', desc: 'Rapid risk profile of your AI initiative in 15 questions' },
      actions: [
        { label: 'EU AI Act Overview', url: '../07-compliance-hub/01-eu-ai-act/', desc: 'What does European AI regulation mean for your organisation?' },
        { label: 'Risk Classification Framework', url: '../01-ai-native-fundamenten/05-risicoclassificatie/', desc: 'Determine the risk level of your specific use case' },
        { label: 'AI Collaboration Modes', url: '../00-strategisch-kader/06-has-h-niveaus/', desc: 'What level of human oversight is required?' }
      ]
    },
    Builder: {
      start: { label: 'Compliance Hub', url: '../07-compliance-hub/', desc: 'Central overview of all compliance requirements per phase' },
      actions: [
        { label: 'Ethical Guidelines', url: '../07-compliance-hub/03-ethische-richtlijnen/', desc: 'Operational ethical frameworks translated to daily practice' },
        { label: 'Validation Requirements', url: '../07-compliance-hub/04-validatie-eisen/', desc: 'Evidence standards required for audit compliance' },
        { label: 'Full Risk Analysis', url: '../09-sjablonen/03-risicoanalyse/template/', desc: 'Document a complete risk assessment for Gate Review' }
      ]
    },
    Visionary: {
      start: { label: 'Incident Response Procedure', url: '../07-compliance-hub/05-incidentrespons/', desc: 'Structured approach to AI incidents at organisational scale' },
      actions: [
        { label: 'Model Governance', url: '../08-technische-standaarden/03-model-governance/', desc: 'Compliance governance for a portfolio of AI systems' },
        { label: 'Continuous Improvement', url: '../10-doorlopende-verbetering/', desc: 'Systematically learn and improve compliance processes' },
        { label: 'Track Sequence (Compliance)', url: '../14-drie-tracks/04-track-sequentie/', desc: 'Compliance considerations in organisation-wide AI transformation' }
      ]
    }
  },
  caio: {
    name: 'CAIO / Management Team', route: 'D',
    Explorer: {
      start: { label: 'Executive Summary', url: '../00-strategisch-kader/00-executive-summary/', desc: 'Understand the full AI Project Blueprint in ten minutes' },
      actions: [
        { label: 'Organisation Profiles \x26 Maturity', url: '../13-organisatieprofielen/', desc: 'Where does your organisation stand in the AI maturity journey?' },
        { label: '90-Day Quick-Start Roadmap', url: '../12-90-dagen-roadmap/', desc: 'Concrete roadmap from strategy to first results' },
        { label: 'Governance Model', url: '../00-strategisch-kader/03-governance-model/', desc: 'Who decides what — roles, responsibilities and escalation' }
      ]
    },
    Builder: {
      start: { label: 'The Three Transformation Tracks', url: '../14-drie-tracks/', desc: 'Strategic growth perspective for your AI transformation ambitions' },
      actions: [
        { label: 'Governance Model (Formalise)', url: '../00-strategisch-kader/03-governance-model/', desc: 'Set up your AI governance for the long term' },
        { label: 'Continuous Improvement', url: '../10-doorlopende-verbetering/', desc: 'From project mindset to programme thinking' },
        { label: 'Benefits Realisation', url: '../10-doorlopende-verbetering/04-batenrealisatie/', desc: 'Report ROI to management and the board' }
      ]
    },
    Visionary: {
      start: { label: 'Accelerators for Scale', url: '../15-accelerators/', desc: 'Acceleration options for AI organisations already operating at scale' },
      actions: [
        { label: 'Organisational Reinvention', url: '../00-strategisch-kader/07-organisatorische-heruitvinding/', desc: 'AI as the foundation of your business model and culture' },
        { label: 'Strategic Reinvention (Track)', url: '../14-drie-tracks/01-strategische-heruitvinding/', desc: 'Long-term strategic transformation through AI' },
        { label: 'Portfolio-level Benefits', url: '../10-doorlopende-verbetering/04-batenrealisatie/', desc: 'Manage and communicate the value of your AI portfolio' }
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
  var labels = { Explorer: 'Explorer', Builder: 'Builder', Visionary: 'Visionary' };
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
      '<div class="bn-start-title">📍 Recommended starting point: ' + data.start.label + '</div>' +
      '<div class="bn-start-desc">' + data.start.desc + '</div>' +
      '<a href="' + data.start.url + '" class="bn-btn bn-btn-primary" style="display:inline-block;text-decoration:none!important;">Start here →</a>' +
    '</div>' +
    '<div class="bn-actions-title">First 3 recommended actions</div>' +
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

## Manual Route Overview

Prefer to navigate directly without the wizard? Use the table below.

| Profile       | Score | Route A (PM)                                                 | Route B (Tech)                                                           | Route C (Guardian)                                              | Route D (CAIO)                                                              |
| :------------ | :---- | :----------------------------------------------------------- | :----------------------------------------------------------------------- | :-------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Explorer**  | 10–20 | [30-Day Kit](../00-explorer-kit/index.md)                    | [Specification-first Pattern](../04-fase-ontwikkeling/05-sdd-patroon.md) | [Quick Pre-Scan](../00-explorer-kit/03-risk-prescan-quick.md)   | [Exec Summary](../00-strategisch-kader/00-executive-summary.md)             |
| **Builder**   | 21–32 | [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md) | [MLOps Standards](../08-technische-standaarden/01-mloops-standaarden.md) | [Compliance Hub](../07-compliance-hub/index.md)                 | [Three Tracks](../14-drie-tracks/index.md)                                  |
| **Visionary** | 33–40 | [Accelerators](../15-accelerators/index.md)                  | [AI Architecture](../08-technische-standaarden/05-ai-architectuur.md)    | [Incident Response](../07-compliance-hub/05-incidentrespons.md) | [Reinvention](../00-strategisch-kader/07-organisatorische-heruitvinding.md) |

______________________________________________________________________

## Related Modules

- [Organisation Profiles (Explorer / Builder / Visionary)](../13-organisatieprofielen/index.md)
- [Profile Assessment (extended version)](../13-organisatieprofielen/04-profiel-beoordeling.md)
- [30-Day Explorer Kit](../00-explorer-kit/index.md)
- [90-Day Quick-Start Roadmap](../12-90-dagen-roadmap/index.md)
