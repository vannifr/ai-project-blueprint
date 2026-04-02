/**
 * Integration tests for the Blueprint Chat Widget.
 *
 * The widget is an IIFE that auto-initialises on DOMContentLoaded.
 * We set up a minimal Material-theme DOM, then load the script via
 * dynamic import so jsdom executes it — then assert on DOM state.
 *
 * @vitest-environment jsdom
 */
import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { readFileSync } from "fs";
import { resolve } from "path";

const WIDGET_SRC = readFileSync(
  resolve(__dirname, "..", "chat-widget.js"),
  "utf-8",
);

/* ── Helpers ── */

/** Build the minimal Material-theme HTML the widget expects. */
function seedDOM(lang = "nl") {
  document.documentElement.lang = lang;
  document.body.innerHTML = `
    <header class="md-header">
      <input id="__search" class="md-toggle" type="checkbox" data-md-toggle="search" />
      <label class="md-header__button md-icon" for="__search">
        <svg>search icon</svg>
      </label>
      <div class="md-search" data-md-component="search" role="dialog">
        <div class="md-search__inner" role="search"></div>
      </div>
    </header>
  `;
}

/** Execute the widget IIFE in the current jsdom context. */
function loadWidget() {
  // eslint-disable-next-line no-eval
  const fn = new Function(WIDGET_SRC);
  fn();
}

/** Shortcut: seed + load. */
function boot(lang = "nl") {
  seedDOM(lang);
  loadWidget();
}

/* ── Tear down ── */

beforeEach(() => {
  sessionStorage.clear();
});

afterEach(() => {
  document.body.innerHTML = "";
  document.documentElement.lang = "";
  vi.restoreAllMocks();
});

/* ================================================================
   1. SEARCH REPLACEMENT
   ================================================================ */

describe("search replacement", () => {
  it("hides the native search dialog", () => {
    boot();
    const search = document.querySelector(".md-search");
    expect(search.style.display).toBe("none");
  });

  it("replaces the search label with a chat trigger button", () => {
    boot();
    const label = document.querySelector('label[for="__search"]');
    expect(label).toBeNull();

    const btn = document.querySelector(".chat-header-trigger");
    expect(btn).not.toBeNull();
    expect(btn.tagName).toBe("BUTTON");
  });

  it("disables the search checkbox", () => {
    boot();
    const cb = document.getElementById("__search");
    expect(cb.disabled).toBe(true);
  });

  it("sets correct aria-label for NL", () => {
    boot("nl");
    const btn = document.querySelector(".chat-header-trigger");
    expect(btn.getAttribute("aria-label")).toBe(
      "Vraag de Blauwdruk Assistent",
    );
  });

  it("sets correct aria-label for EN", () => {
    boot("en");
    const btn = document.querySelector(".chat-header-trigger");
    expect(btn.getAttribute("aria-label")).toBe(
      "Ask the Blueprint Assistant",
    );
  });
});

/* ================================================================
   2. CHAT PANEL CREATION
   ================================================================ */

describe("chat panel creation", () => {
  it("appends the #blueprint-chat wrapper to body", () => {
    boot();
    const widget = document.getElementById("blueprint-chat");
    expect(widget).not.toBeNull();
    expect(widget.parentNode).toBe(document.body);
  });

  it("starts in the closed state", () => {
    boot();
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--closed")).toBe(true);
    expect(widget.classList.contains("chat-widget--open")).toBe(false);
  });

  it("contains a backdrop, panel, header, messages area, and form", () => {
    boot();
    expect(document.querySelector(".chat-widget__backdrop")).not.toBeNull();
    expect(document.querySelector(".chat-widget__panel")).not.toBeNull();
    expect(document.querySelector(".chat-widget__header")).not.toBeNull();
    expect(document.querySelector(".chat-widget__messages")).not.toBeNull();
    expect(document.querySelector(".chat-widget__input")).not.toBeNull();
  });

  it("renders NL labels when lang=nl", () => {
    boot("nl");
    expect(document.querySelector(".chat-widget__title").textContent).toBe(
      "Blauwdruk Assistent",
    );
  });

  it("renders EN labels when lang=en", () => {
    boot("en");
    expect(document.querySelector(".chat-widget__title").textContent).toBe(
      "Blueprint Assistant",
    );
  });
});

/* ================================================================
   3. OPEN / CLOSE BEHAVIOUR
   ================================================================ */

describe("open / close", () => {
  it("opens the panel when the header button is clicked", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--open")).toBe(true);
    expect(widget.classList.contains("chat-widget--closed")).toBe(false);
  });

  it("persists open state in sessionStorage", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();
    expect(sessionStorage.getItem("chat-open")).toBe("true");
  });

  it("closes the panel via the close button", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();
    document.querySelector(".chat-widget__close").click();
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--closed")).toBe(true);
    expect(widget.classList.contains("chat-widget--open")).toBe(false);
  });

  it("closes the panel via backdrop click", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();
    document.querySelector(".chat-widget__backdrop").click();
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--closed")).toBe(true);
  });

  it("closes the panel via Escape key", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" }));
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--closed")).toBe(true);
  });

  it("Escape does nothing when panel is already closed", () => {
    boot();
    // panel is closed — Escape should not error or change state
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" }));
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--closed")).toBe(true);
  });
});

/* ================================================================
   4. SESSION RESTORE
   ================================================================ */

describe("session restore", () => {
  it("restores open state from sessionStorage", () => {
    sessionStorage.setItem("chat-open", "true");
    boot();
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--open")).toBe(true);
  });

  it("restores fullscreen state from sessionStorage", () => {
    sessionStorage.setItem("chat-open", "true");
    sessionStorage.setItem("chat-fullscreen", "true");
    boot();
    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--fullscreen")).toBe(true);
  });
});

/* ================================================================
   5. FULLSCREEN TOGGLE
   ================================================================ */

describe("fullscreen toggle", () => {
  it("toggles fullscreen class on the widget", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();
    const btn = document.querySelector(".chat-widget__fullscreen");
    const widget = document.getElementById("blueprint-chat");

    btn.click();
    expect(widget.classList.contains("chat-widget--fullscreen")).toBe(true);
    expect(sessionStorage.getItem("chat-fullscreen")).toBe("true");

    btn.click();
    expect(widget.classList.contains("chat-widget--fullscreen")).toBe(false);
    expect(sessionStorage.getItem("chat-fullscreen")).toBe("false");
  });

  it("updates aria-label on fullscreen toggle (NL)", () => {
    boot("nl");
    document.querySelector(".chat-header-trigger").click();
    const btn = document.querySelector(".chat-widget__fullscreen");

    btn.click();
    expect(btn.getAttribute("aria-label")).toBe("Kleiner");

    btn.click();
    expect(btn.getAttribute("aria-label")).toBe("Volledig scherm");
  });

  it("close button also resets fullscreen", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();
    document.querySelector(".chat-widget__fullscreen").click();
    document.querySelector(".chat-widget__close").click();

    const widget = document.getElementById("blueprint-chat");
    expect(widget.classList.contains("chat-widget--fullscreen")).toBe(false);
    expect(sessionStorage.getItem("chat-fullscreen")).toBe("false");
  });
});

/* ================================================================
   6. FORM SUBMISSION & API CALL
   ================================================================ */

describe("form submission", () => {
  it("adds a user message to the messages container", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();

    // Mock fetch to prevent actual network call
    vi.spyOn(globalThis, "fetch").mockResolvedValue({
      ok: true,
      json: () =>
        Promise.resolve({ answer: "Test antwoord", sources: [] }),
    });

    const input = document.querySelector(".chat-widget__input input");
    input.value = "Wat is AI-native?";
    document.querySelector(".chat-widget__input").dispatchEvent(
      new Event("submit", { bubbles: true, cancelable: true }),
    );

    const msgs = document.querySelectorAll(".chat-widget__msg--user");
    expect(msgs.length).toBe(1);
    expect(msgs[0].textContent).toBe("Wat is AI-native?");
  });

  it("calls the /api/chat endpoint with correct payload", () => {
    boot("nl");
    document.querySelector(".chat-header-trigger").click();

    const fetchMock = vi.spyOn(globalThis, "fetch").mockResolvedValue({
      ok: true,
      json: () =>
        Promise.resolve({ answer: "Antwoord", sources: [] }),
    });

    const input = document.querySelector(".chat-widget__input input");
    input.value = "Test vraag";
    document.querySelector(".chat-widget__input").dispatchEvent(
      new Event("submit", { bubbles: true, cancelable: true }),
    );

    expect(fetchMock).toHaveBeenCalledWith("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: "Test vraag", language: "nl" }),
    });
  });

  it("renders assistant answer after successful API response", async () => {
    boot();
    document.querySelector(".chat-header-trigger").click();

    vi.spyOn(globalThis, "fetch").mockResolvedValue({
      ok: true,
      json: () =>
        Promise.resolve({
          answer: "Dit is het **antwoord**.",
          sources: [{ url: "/test/", title: "Test Page" }],
        }),
    });

    const input = document.querySelector(".chat-widget__input input");
    input.value = "Vraag";
    document.querySelector(".chat-widget__input").dispatchEvent(
      new Event("submit", { bubbles: true, cancelable: true }),
    );

    // Wait for the fetch promise chain to resolve
    await vi.waitFor(() => {
      const assistantMsgs = document.querySelectorAll(
        ".chat-widget__msg--assistant",
      );
      // Should have the answer (loading "..." should be replaced)
      const lastMsg = assistantMsgs[assistantMsgs.length - 1];
      expect(lastMsg.innerHTML).toContain("<strong>antwoord</strong>");
      expect(lastMsg.innerHTML).toContain("Test Page");
    });
  });

  it("shows error message on fetch failure", async () => {
    boot("nl");
    document.querySelector(".chat-header-trigger").click();

    vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("Network"));

    const input = document.querySelector(".chat-widget__input input");
    input.value = "Oops";
    document.querySelector(".chat-widget__input").dispatchEvent(
      new Event("submit", { bubbles: true, cancelable: true }),
    );

    await vi.waitFor(() => {
      const msgs = document.querySelectorAll(".chat-widget__msg--assistant");
      const last = msgs[msgs.length - 1];
      expect(last.textContent).toBe(
        "Er ging iets mis. Probeer het opnieuw.",
      );
    });
  });

  it("ignores empty submissions", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();

    const fetchMock = vi.spyOn(globalThis, "fetch").mockResolvedValue({
      ok: true,
      json: () => Promise.resolve({ answer: "", sources: [] }),
    });

    const input = document.querySelector(".chat-widget__input input");
    input.value = "   ";
    document.querySelector(".chat-widget__input").dispatchEvent(
      new Event("submit", { bubbles: true, cancelable: true }),
    );

    expect(fetchMock).not.toHaveBeenCalled();
  });

  it("disables input while waiting for response", () => {
    boot();
    document.querySelector(".chat-header-trigger").click();

    // Use a never-resolving promise to keep the widget in loading state
    vi.spyOn(globalThis, "fetch").mockReturnValue(new Promise(() => {}));

    const input = document.querySelector(".chat-widget__input input");
    input.value = "Wachten";
    document.querySelector(".chat-widget__input").dispatchEvent(
      new Event("submit", { bubbles: true, cancelable: true }),
    );

    expect(input.disabled).toBe(true);
  });

  it("re-enables input after response", async () => {
    boot();
    document.querySelector(".chat-header-trigger").click();

    vi.spyOn(globalThis, "fetch").mockResolvedValue({
      ok: true,
      json: () => Promise.resolve({ answer: "OK", sources: [] }),
    });

    const input = document.querySelector(".chat-widget__input input");
    input.value = "Test";
    document.querySelector(".chat-widget__input").dispatchEvent(
      new Event("submit", { bubbles: true, cancelable: true }),
    );

    await vi.waitFor(() => {
      expect(input.disabled).toBe(false);
    });
  });
});

/* ================================================================
   7. GRACEFUL DEGRADATION (no search elements in DOM)
   ================================================================ */

describe("graceful degradation", () => {
  it("works without a search label in the DOM", () => {
    document.documentElement.lang = "nl";
    document.body.innerHTML = "<header></header>";
    loadWidget();

    // Widget should still be created even without a header button
    expect(document.getElementById("blueprint-chat")).not.toBeNull();
    // No header trigger, but no errors
    expect(document.querySelector(".chat-header-trigger")).toBeNull();
  });
});
