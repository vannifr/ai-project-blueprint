/**
 * Blueprint Chat Widget — replaces the search bar in the header
 * with an AI-powered "Blauwdruk Assistent" chat panel.
 */
(function () {
  "use strict";

  const API_BASE = "/api";
  const LANG = document.documentElement.lang || "nl";

  const LABELS = {
    nl: {
      title: "Blauwdruk Assistent",
      hint: "Stel een vraag — ik geef een antwoord, geen paginalijst",
      placeholder: "Stel een vraag over de Blauwdruk...",
      error: "Er ging iets mis. Probeer het opnieuw.",
      sources: "Bronnen",
      expand: "Volledig scherm",
      collapse: "Kleiner",
      headerBtn: "Vraag de Blauwdruk Assistent",
    },
    en: {
      title: "Blueprint Assistant",
      hint: "Ask a question — I'll give you an answer, not a page list",
      placeholder: "Ask a question about the Blueprint...",
      error: "Something went wrong. Please try again.",
      sources: "Sources",
      expand: "Full screen",
      collapse: "Smaller",
      headerBtn: "Ask the Blueprint Assistant",
    },
  };

  const l = LABELS[LANG] || LABELS.en;

  /* ── Chat panel (appended to body, toggled by header button) ── */

  function createPanel() {
    const wrapper = document.createElement("div");
    wrapper.id = "blueprint-chat";
    wrapper.className = "chat-widget chat-widget--closed";
    wrapper.innerHTML = `
      <div class="chat-widget__backdrop"></div>
      <div class="chat-widget__panel">
        <div class="chat-widget__header">
          <div class="chat-widget__header-text">
            <span class="chat-widget__title">${l.title}</span>
            <span class="chat-widget__hint">${l.hint}</span>
          </div>
          <div class="chat-widget__header-actions">
            <button class="chat-widget__fullscreen" aria-label="${l.expand}" title="${l.expand}">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/>
                <line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/>
              </svg>
            </button>
            <button class="chat-widget__close" aria-label="Close">&times;</button>
          </div>
        </div>
        <div class="chat-widget__messages"></div>
        <form class="chat-widget__input">
          <input type="text" placeholder="${l.placeholder}" autocomplete="off" maxlength="500" />
          <button type="submit" aria-label="Send">&#10148;</button>
        </form>
      </div>
    `;
    document.body.appendChild(wrapper);
    return wrapper;
  }

  /* ── Replace search button in header ── */

  function replaceSearch() {
    // Hide the native search dialog
    var searchForm = document.querySelector(".md-search");
    if (searchForm) searchForm.style.display = "none";

    // Find the search label/button in the header
    var searchLabel = document.querySelector('label.md-header__button[for="__search"]');
    if (!searchLabel) return null;

    // Create replacement button
    var btn = document.createElement("button");
    btn.className = "md-header__button md-icon chat-header-trigger";
    btn.setAttribute("aria-label", l.headerBtn);
    btn.setAttribute("title", l.headerBtn);
    btn.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
        <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>`;

    // Replace the search label with the chat trigger
    searchLabel.parentNode.replaceChild(btn, searchLabel);

    // Also hide the search checkbox so keyboard shortcut doesn't trigger it
    var searchCheckbox = document.getElementById("__search");
    if (searchCheckbox) searchCheckbox.disabled = true;

    return btn;
  }

  /* ── Initialise ── */

  function init() {
    var headerBtn = replaceSearch();
    var widget = createPanel();
    var close = widget.querySelector(".chat-widget__close");
    var backdrop = widget.querySelector(".chat-widget__backdrop");
    var fullscreenBtn = widget.querySelector(".chat-widget__fullscreen");
    var messages = widget.querySelector(".chat-widget__messages");
    var form = widget.querySelector(".chat-widget__input");
    var input = form.querySelector("input");

    function openChat() {
      widget.classList.remove("chat-widget--closed");
      widget.classList.add("chat-widget--open");
      sessionStorage.setItem("chat-open", "true");
      input.focus();
    }

    function closeChat() {
      widget.classList.remove("chat-widget--open", "chat-widget--fullscreen");
      widget.classList.add("chat-widget--closed");
      sessionStorage.setItem("chat-open", "false");
      sessionStorage.setItem("chat-fullscreen", "false");
      updateFullscreenIcon(fullscreenBtn, false);
    }

    // Restore state
    if (sessionStorage.getItem("chat-open") === "true") {
      openChat();
    }
    if (sessionStorage.getItem("chat-fullscreen") === "true") {
      widget.classList.add("chat-widget--fullscreen");
      updateFullscreenIcon(fullscreenBtn, true);
    }

    if (headerBtn) {
      headerBtn.addEventListener("click", openChat);
    }

    close.addEventListener("click", closeChat);
    backdrop.addEventListener("click", closeChat);

    // Close on Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && widget.classList.contains("chat-widget--open")) {
        closeChat();
      }
    });

    fullscreenBtn.addEventListener("click", function () {
      var isFs = widget.classList.toggle("chat-widget--fullscreen");
      sessionStorage.setItem("chat-fullscreen", isFs ? "true" : "false");
      updateFullscreenIcon(fullscreenBtn, isFs);
      messages.scrollTop = messages.scrollHeight;
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var question = input.value.trim();
      if (!question) return;

      addMessage(messages, question, "user");
      input.value = "";
      input.disabled = true;

      sendQuestion(question, messages).finally(function () {
        input.disabled = false;
        input.focus();
      });
    });
  }

  function updateFullscreenIcon(btn, isFullscreen) {
    if (isFullscreen) {
      btn.setAttribute("aria-label", l.collapse);
      btn.setAttribute("title", l.collapse);
      btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 14 10 14 10 20"/><polyline points="20 10 14 10 14 4"/><line x1="10" y1="14" x2="3" y2="21"/><line x1="21" y1="3" x2="14" y2="10"/></svg>';
    } else {
      btn.setAttribute("aria-label", l.expand);
      btn.setAttribute("title", l.expand);
      btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>';
    }
  }

  function addMessage(container, text, role) {
    var msg = document.createElement("div");
    msg.className = "chat-widget__msg chat-widget__msg--" + role;
    msg.textContent = text;
    container.appendChild(msg);
    container.scrollTop = container.scrollHeight;
    return msg;
  }

  function addAssistantMessage(container, html) {
    var msg = document.createElement("div");
    msg.className = "chat-widget__msg chat-widget__msg--assistant";
    msg.innerHTML = html;
    container.appendChild(msg);
    container.scrollTop = container.scrollHeight;
    return msg;
  }

  function renderSources(sources) {
    if (!sources || sources.length === 0) return "";
    var html = '<div class="chat-widget__sources"><span>' + l.sources + ":</span>";
    sources.forEach(function (s) {
      html +=
        ' <a href="' + s.url + '" target="_blank" class="chat-widget__source-link">' + escapeHtml(s.title) + "</a>";
    });
    html += "</div>";
    return html;
  }

  function escapeHtml(text) {
    var div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  function formatAnswer(text) {
    return text
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>')
      .replace(/\n/g, "<br>");
  }

  function sendQuestion(question, container) {
    var loading = addMessage(container, "...", "assistant");

    return fetch(API_BASE + "/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: question, language: LANG }),
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function (data) {
        container.removeChild(loading);
        var html = formatAnswer(data.answer) + renderSources(data.sources);
        addAssistantMessage(container, html);
      })
      .catch(function () {
        container.removeChild(loading);
        addMessage(container, l.error, "assistant");
      });
  }

  // Initialize when DOM is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
