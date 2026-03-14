---
versie: '1.0'
pdf: false
type: meta
layer: 3
---

# Feedback

Jouw feedback maakt de AI Project Blauwdruk beter. Laat ons weten wat er ontbreekt, wat er fout staat of wat goed werkt.

______________________________________________________________________

<form class="feedback-form" action="https://formspree.io/f/xpqylakk" method="POST">

<div class="feedback-form__field">
    <label for="fb-page">Pagina of module</label>
    <input type="text" id="fb-page" name="page" placeholder="Bijv. Red Teaming Playbook, Doelkaart, Fase 3 Realisatie">
  </div>

<div class="feedback-form__field">
    <label>Type feedback</label>
    <div class="feedback-form__radios">
      <label><input type="radio" name="type" value="inhoudelijke-fout"> Inhoudelijke fout</label>
      <label><input type="radio" name="type" value="ontbrekende-info"> Ontbrekende informatie</label>
      <label><input type="radio" name="type" value="vertaling"> Vertaling of taalfout</label>
      <label><input type="radio" name="type" value="compliment"> Compliment</label>
      <label><input type="radio" name="type" value="overig" checked> Overig</label>
    </div>
  </div>

<div class="feedback-form__field">
    <label for="fb-message">Bericht <span class="feedback-form__required">*</span></label>
    <textarea id="fb-message" name="message" rows="6" placeholder="Beschrijf je feedback zo concreet mogelijk..." required></textarea>
  </div>

<div class="feedback-form__field">
    <label for="fb-email">E-mailadres (optioneel)</label>
    <input type="email" id="fb-email" name="email" placeholder="jouw@email.com — alleen als je een antwoord wilt ontvangen">
  </div>

<button type="submit" class="feedback-form__submit">Verstuur feedback</button>

</form>

<div id="feedback-thanks" style="display:none;padding:1.5rem;border-left:4px solid var(--md-primary-fg-color);background:var(--md-code-bg-color);border-radius:4px;margin-top:1rem">
  <strong>Bedankt voor je feedback!</strong><br>
  We hebben je bericht ontvangen en nemen het mee in de verdere ontwikkeling van de Blauwdruk.
</div>

<div id="feedback-error" style="display:none;padding:1.5rem;border-left:4px solid #c0392b;background:var(--md-code-bg-color);border-radius:4px;margin-top:1rem">
  Er ging iets mis bij het verzenden. Probeer het opnieuw of stuur een e-mail.
</div>

<script>
document.querySelector('.feedback-form').addEventListener('submit', function(e) {
  e.preventDefault();
  var form = e.target;
  var btn = form.querySelector('button[type="submit"]');
  btn.disabled = true;
  fetch(form.action, {
    method: 'POST',
    body: new FormData(form),
    headers: { 'Accept': 'application/json' }
  }).then(function(r) {
    if (r.ok) {
      form.style.display = 'none';
      document.getElementById('feedback-thanks').style.display = 'block';
    } else {
      btn.disabled = false;
      document.getElementById('feedback-error').style.display = 'block';
    }
  }).catch(function() {
    btn.disabled = false;
    document.getElementById('feedback-error').style.display = 'block';
  });
});
</script>

______________________________________________________________________

!!! info "Privacy"
    Je e-mailadres is optioneel en wordt uitsluitend gebruikt om te reageren op jouw feedback. We slaan geen analytics of tracking op.
