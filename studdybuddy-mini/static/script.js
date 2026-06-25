// =============================================================================
// script.js – StudyBuddy Mini
// Frontend Chat Logic
//
// Responsibilities:
//  • Render the welcome message on page load
//  • Send user messages to Flask via fetch (POST /chat)
//  • Show and hide typing animation
//  • Append user and bot message bubbles
//  • Handle suggestion chip clicks
//  • Support Enter key to send
//  • Auto-scroll to the latest message
//  • Clear chat functionality
//  • Graceful network error handling
// =============================================================================

// ── DOM References ─────────────────────────────────────────────────────────
const chatMessages    = document.getElementById("chatMessages");
const userInput       = document.getElementById("userInput");
const sendBtn         = document.getElementById("sendBtn");
const clearBtn        = document.getElementById("clearBtn");
const typingIndicator = document.getElementById("typingIndicator");
const suggestionChips = document.querySelectorAll(".chip");

// ── Config ──────────────────────────────────────────────────────────────────
const CHAT_ENDPOINT    = "/chat";
// Simulated delay (ms) before showing the bot's reply – makes it feel natural
const TYPING_DELAY_MS  = 800;

// ── Welcome Message ─────────────────────────────────────────────────────────

/**
 * Display the initial welcome message when the page loads.
 * This mirrors a continuous chatbot session – the conversation starts
 * immediately, just like the while-loop in a CLI chatbot would greet the user.
 */
function showWelcomeMessage() {
  const welcomeText =
    "👋 Hey! I'm StudyBuddy Mini – your offline, rule-based learning companion.\n\n" +
    "I know about programming languages, study strategies, and even the occasional joke.\n\n" +
    "Type 'help' to see everything I can discuss, or tap a chip below to get started!";

  appendBotMessage(welcomeText);
}

// ── Message Builders ─────────────────────────────────────────────────────────

/**
 * Create and insert a user message bubble into the chat.
 * @param {string} text – The text the user typed.
 */
function appendUserMessage(text) {
  const row = document.createElement("div");
  row.classList.add("message-row", "user-row");

  row.innerHTML = `
    <div class="message-avatar" aria-hidden="true">You</div>
    <div class="message-bubble" role="article">${escapeHtml(text)}</div>
  `;

  chatMessages.appendChild(row);
  scrollToBottom();
}

/**
 * Create and insert a bot message bubble into the chat.
 * @param {string} text – The bot's response string (may contain \n).
 */
function appendBotMessage(text) {
  const row = document.createElement("div");
  row.classList.add("message-row", "bot-row");

  // escapeHtml first, then convert \n to <br> for display
  const formattedText = escapeHtml(text).replace(/\n/g, "<br>");

  row.innerHTML = `
    <div class="message-avatar" aria-hidden="true">SB</div>
    <div class="message-bubble" role="article">${formattedText}</div>
  `;

  chatMessages.appendChild(row);
  scrollToBottom();
}

/**
 * Show an inline error message if the network request fails.
 * @param {string} message – A user-friendly error description.
 */
function appendErrorMessage(message) {
  const row = document.createElement("div");
  row.classList.add("message-row", "bot-row");

  row.innerHTML = `
    <div class="message-avatar" aria-hidden="true">SB</div>
    <div class="message-bubble" role="alert" style="color:#f87171; border-color:rgba(248,113,113,0.2);">
      ⚠️ ${escapeHtml(message)}
    </div>
  `;

  chatMessages.appendChild(row);
  scrollToBottom();
}

// ── Typing Indicator ─────────────────────────────────────────────────────────

/** Show the animated typing indicator below the messages. */
function showTyping() {
  typingIndicator.hidden = false;
  typingIndicator.setAttribute("aria-hidden", "false");
  scrollToBottom();
}

/** Hide the typing indicator. */
function hideTyping() {
  typingIndicator.hidden = true;
  typingIndicator.setAttribute("aria-hidden", "true");
}

// ── Core Send Flow ───────────────────────────────────────────────────────────

/**
 * Handle sending a message:
 *  1. Validate input
 *  2. Render user bubble
 *  3. Show typing animation
 *  4. POST to /chat
 *  5. Render bot bubble (or error)
 *
 * This reproduces the Input → Process → Output loop of the original
 * CLI while-loop chatbot, but through the browser.
 *
 * @param {string} messageText – The raw text to send.
 */
async function sendMessage(messageText) {
  const trimmed = messageText.trim();

  // Guard: do nothing on empty input
  if (!trimmed) return;

  // Disable UI while waiting for a response
  setUiState(false);

  // 1. Render user's message immediately
  appendUserMessage(trimmed);

  // 2. Clear the input field
  userInput.value = "";

  // 3. Show typing indicator
  showTyping();

  // 4. Wait briefly (simulated thinking), then POST to Flask
  await delay(TYPING_DELAY_MS);

  try {
    const response = await fetch(CHAT_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: trimmed }),
    });

    if (!response.ok) {
      // Non-2xx HTTP status
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();

    hideTyping();

    if (data.response) {
      appendBotMessage(data.response);
    } else if (data.error) {
      appendErrorMessage(`Server said: ${data.error}`);
    } else {
      appendErrorMessage("Received an unexpected response from the server.");
    }

  } catch (err) {
    hideTyping();
    appendErrorMessage(
      "Couldn't reach StudyBuddy Mini. " +
      "Make sure the Flask server is running and try again."
    );
    console.error("[StudyBuddy] Fetch error:", err);
  }

  // Re-enable UI and refocus input
  setUiState(true);
  userInput.focus();
}

// ── Event Listeners ──────────────────────────────────────────────────────────

// Send button click
sendBtn.addEventListener("click", () => {
  sendMessage(userInput.value);
});

// Enter key support (Shift+Enter does NOT trigger send – allows multi-line paste)
userInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    sendMessage(userInput.value);
  }
});

// Suggestion chips – clicking sends the chip's data-message value
suggestionChips.forEach((chip) => {
  chip.addEventListener("click", () => {
    const message = chip.dataset.message;
    if (message) {
      sendMessage(message);
    }
  });
});

// Clear chat button
clearBtn.addEventListener("click", () => {
  // Remove all message rows
  chatMessages.innerHTML = "";
  // Re-show the welcome message so the chat doesn't feel empty
  showWelcomeMessage();
  userInput.focus();
});

// ── Utility Helpers ──────────────────────────────────────────────────────────

/**
 * Scroll the chat window to the very bottom.
 * Uses scrollTop + scrollHeight so the latest message is always visible.
 */
function scrollToBottom() {
  // Small setTimeout ensures the DOM has updated before we measure scrollHeight
  setTimeout(() => {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }, 30);
}

/**
 * Enable or disable interactive elements during an API call.
 * Prevents double-sends while waiting for a response.
 * @param {boolean} enabled – true to enable, false to disable.
 */
function setUiState(enabled) {
  userInput.disabled  = !enabled;
  sendBtn.disabled    = !enabled;

  // Chips stay interactive so users can queue another question right after
}

/**
 * Sanitize a string for safe innerHTML insertion.
 * Prevents XSS by escaping HTML special characters.
 * @param {string} str – Raw string.
 * @returns {string} HTML-escaped string.
 */
function escapeHtml(str) {
  const map = {
    "&":  "&amp;",
    "<":  "&lt;",
    ">":  "&gt;",
    '"':  "&quot;",
    "'":  "&#039;",
  };
  return String(str).replace(/[&<>"']/g, (char) => map[char]);
}

/**
 * Return a Promise that resolves after `ms` milliseconds.
 * Used to simulate the chatbot "thinking" before it replies.
 * @param {number} ms – Milliseconds to wait.
 * @returns {Promise<void>}
 */
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// ── Init ─────────────────────────────────────────────────────────────────────
// Show the welcome message as soon as the page loads
showWelcomeMessage();

// Auto-focus the input so the user can start typing immediately
userInput.focus();
