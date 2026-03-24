/**
 * Blueprint Chat Widget — lightweight vanilla JS chat for ai-delivery.io
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
    },
    en: {
      title: "Blueprint Assistant",
      hint: "Ask a question — I'll give you an answer, not a page list",
      placeholder: "Ask a question about the Blueprint...",
      error: "Something went wrong. Please try again.",
      sources: "Sources",
      expand: "Full screen",
      collapse: "Smaller",
    },
  };

  const l = LABELS[LANG] || LABELS.en;

  function createWidget() {
    const widget = document.createElement("div");
    widget.id = "blueprint-chat";
    widget.className = "chat-widget chat-widget--closed";
    widget.innerHTML = `
      <button class="chat-widget__toggle" aria-label="${l.title}">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
        </svg>
      </button>
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
    document.body.appendChild(widget);
    return widget;
  }

  function init() {
    const widget = createWidget();
    const toggle = widget.querySelector(".chat-widget__toggle");
    const close = widget.querySelector(".chat-widget__close");
    const fullscreenBtn = widget.querySelector(".chat-widget__fullscreen");
    const messages = widget.querySelector(".chat-widget__messages");
    const form = widget.querySelector(".chat-widget__input");
    const input = form.querySelector("input");

    // Restore state
    if (sessionStorage.getItem("chat-open") === "true") {
      widget.classList.remove("chat-widget--closed");
      widget.classList.add("chat-widget--open");
    }
    if (sessionStorage.getItem("chat-fullscreen") === "true") {
      widget.classList.add("chat-widget--fullscreen");
      updateFullscreenIcon(fullscreenBtn, true);
    }

    toggle.addEventListener("click", function () {
      widget.classList.remove("chat-widget--closed");
      widget.classList.add("chat-widget--open");
      sessionStorage.setItem("chat-open", "true");
      input.focus();
    });

    close.addEventListener("click", function () {
      widget.classList.remove("chat-widget--open");
      widget.classList.add("chat-widget--closed");
      widget.classList.remove("chat-widget--fullscreen");
      sessionStorage.setItem("chat-open", "false");
      sessionStorage.setItem("chat-fullscreen", "false");
      updateFullscreenIcon(fullscreenBtn, false);
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
    var l = LABELS[LANG] || LABELS.en;
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
    // Basic markdown-lite: bold, links, line breaks
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
