---
versie: '1.0'
---

# Feedback

Jouw feedback maakt de AI Project Blauwdruk beter. Laat ons weten wat er ontbreekt, wat er fout staat of wat goed werkt.

______________________________________________________________________

<form class="feedback-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">

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

______________________________________________________________________

!!! info "Privacy"
    Je e-mailadres is optioneel en wordt uitsluitend gebruikt om te reageren op jouw feedback. We slaan geen analytics of tracking op.
