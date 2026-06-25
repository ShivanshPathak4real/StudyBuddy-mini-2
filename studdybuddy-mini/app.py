# =============================================================================
# app.py – StudyBuddy Mini
# Flask Web Server
#
# Routes:
#   GET  /       → Serve the chat interface (index.html)
#   POST /chat   → Accept a JSON message, return a JSON response
#
# Run locally:  python app.py
# Deploy on:    Render (Web Service, Python)
# =============================================================================

from flask import Flask, render_template, request, jsonify
from chatbot import get_response  # Import the rule-based response engine

# ---------------------------------------------------------------------------
# App Initialization
# ---------------------------------------------------------------------------
# templates/ folder contains index.html; static/ folder contains style.css & script.js
app = Flask(__name__)


# ---------------------------------------------------------------------------
# Route: GET /
# Serves the main chat interface.
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    """Render and serve the main chat page."""
    return render_template("index.html")


# ---------------------------------------------------------------------------
# Route: POST /chat
# Accepts JSON: { "message": "user input here" }
# Returns JSON: { "response": "bot reply here" }
# ---------------------------------------------------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    """
    Handle an incoming chat message and return a bot response.

    Expected request body (JSON):
        { "message": "hello" }

    Returns (JSON):
        { "response": "Hey there! I'm StudyBuddy Mini..." }
        or
        { "error": "No message provided." }  on bad input
    """

    # Parse the incoming JSON body
    data = request.get_json()

    # Guard: ensure JSON was provided and contains a "message" field
    if not data or "message" not in data:
        return jsonify({"error": "No message provided."}), 400

    user_message = data["message"]

    # Guard: ensure message is a non-empty string
    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify({"error": "Message must be a non-empty string."}), 400

    # Get the rule-based response from chatbot.py
    bot_response = get_response(user_message)

    # Return the response as JSON
    return jsonify({"response": bot_response})


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True enables auto-reload during development.
    # Render will use gunicorn to serve the app in production.
    app.run(debug=True, host="0.0.0.0", port=5000)
