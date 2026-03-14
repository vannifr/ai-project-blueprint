---
versie: '1.0'
pdf: false
type: meta
layer: 3
---

# Feedback

Your feedback makes the AI Project Blueprint better. Let us know what is missing, what is incorrect, or what works well.

______________________________________________________________________

<form class="feedback-form" action="https://formspree.io/f/xpqylakk" method="POST">

<div class="feedback-form__field">
    <label for="fb-page">Page or module</label>
    <input type="text" id="fb-page" name="page" placeholder="E.g. Red Teaming Playbook, Objective Card, Phase 3 Development">
  </div>

<div class="feedback-form__field">
    <label>Type of feedback</label>
    <div class="feedback-form__radios">
      <label><input type="radio" name="type" value="content-error"> Content error</label>
      <label><input type="radio" name="type" value="missing-info"> Missing information</label>
      <label><input type="radio" name="type" value="translation"> Translation or language error</label>
      <label><input type="radio" name="type" value="compliment"> Compliment</label>
      <label><input type="radio" name="type" value="other" checked> Other</label>
    </div>
  </div>

<div class="feedback-form__field">
    <label for="fb-message">Message <span class="feedback-form__required">*</span></label>
    <textarea id="fb-message" name="message" rows="6" placeholder="Describe your feedback as specifically as possible..." required></textarea>
  </div>

<div class="feedback-form__field">
    <label for="fb-email">Email address (optional)</label>
    <input type="email" id="fb-email" name="email" placeholder="your@email.com — only if you want a reply">
  </div>

<button type="submit" class="feedback-form__submit">Send feedback</button>

</form>

<div id="feedback-thanks" style="display:none;padding:1.5rem;border-left:4px solid var(--md-primary-fg-color);background:var(--md-code-bg-color);border-radius:4px;margin-top:1rem">
  <strong>Thank you for your feedback!</strong><br>
  We have received your message and will incorporate it into the further development of the Blueprint.
</div>

<div id="feedback-error" style="display:none;padding:1.5rem;border-left:4px solid #c0392b;background:var(--md-code-bg-color);border-radius:4px;margin-top:1rem">
  Something went wrong while submitting. Please try again or send an email.
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
    Your email address is optional and will only be used to respond to your feedback. We do not store analytics or tracking data.
