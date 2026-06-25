# StudyBuddy Mini

**A Rule-Based Learning Companion**

> Built by **Shivansh Pathak** · DecodeLabs AI Internship · Project 1

---

## Project Overview

StudyBuddy Mini is a fully offline, rule-based chatbot web application that helps students explore programming topics and study strategies through predefined, deterministic responses.

It contains **zero AI, zero machine learning, zero APIs, and zero internet dependency.**
Every response is a handcrafted string stored in a Python dictionary. The chatbot appears intelligent because of good software engineering — not because of any model or algorithm.

This project was built to satisfy the requirements of **DecodeLabs AI Internship – Project 1**, which teaches the foundational concept of rule-based systems, control flow, and the Input → Process → Output model.

---

## Features

- 💬 **25+ predefined intents** across 6 categories
- 🐍 Python, Java, C++, JavaScript, HTML, CSS, SQL, AI, DSA, GitHub topics
- 📚 Study tips, exam tips, concentration, revision, motivation advice
- 😄 Jokes, fun facts, and quotes
- 👋 Greetings and farewell handling
- 🎯 Suggestion chips for quick navigation
- ✨ Typing animation before each bot reply
- 🧹 Clear chat button
- 📱 Fully responsive — works on mobile and desktop
- 🌑 Dark mode with glassmorphism UI
- ⌨️ Enter key and click support for sending messages
- 🔒 Input sanitization (`.lower().strip()`)
- ⚡ Zero dependencies beyond Flask and gunicorn

---

## Folder Structure

```
StudyBuddy-Mini/
│
├── app.py              ← Flask web server (routes: GET / and POST /chat)
├── chatbot.py          ← Rule-based response engine (dictionary + logic)
├── requirements.txt    ← Flask + gunicorn only
├── README.md           ← This file
├── .gitignore          ← Standard Python + IDE ignores
│
├── templates/
│   └── index.html      ← Chat UI (semantic HTML5)
│
└── static/
    ├── style.css        ← Dark glassmorphism UI (pure CSS)
    └── script.js        ← fetch() + DOM logic (vanilla JS)
```

---

## Installation

**Prerequisites:** Python 3.9+ installed on your machine.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/StudyBuddy-Mini.git
cd StudyBuddy-Mini
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# On macOS / Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running Locally

```bash
python app.py
```

Then open your browser and navigate to:

```
http://localhost:5000
```

You should see the StudyBuddy Mini chat interface.

---

## Deploying on Render

StudyBuddy Mini is designed to deploy on **[Render](https://render.com)** with minimal configuration.

### Step 1 – Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit – StudyBuddy Mini"
git remote add origin https://github.com/your-username/StudyBuddy-Mini.git
git push -u origin main
```

### Step 2 – Create a Render Web Service

1. Log in to [render.com](https://render.com) and click **New → Web Service**
2. Connect your GitHub account and select the `StudyBuddy-Mini` repository
3. Fill in the settings:

| Setting          | Value                          |
|------------------|--------------------------------|
| **Name**         | studybuddy-mini                |
| **Environment**  | Python 3                       |
| **Build Command**| `pip install -r requirements.txt` |
| **Start Command**| `gunicorn app:app`             |

4. Click **Deploy Web Service**

Render will detect `requirements.txt`, install Flask and gunicorn, and start the server automatically. No Dockerfile or additional config is needed.

---

## Technologies Used

| Technology  | Role                              |
|-------------|-----------------------------------|
| Python 3    | Application logic                 |
| Flask 3     | Web framework (routing + templating) |
| gunicorn    | WSGI server for Render deployment |
| HTML5       | Semantic page structure           |
| CSS3        | Styling (glassmorphism dark mode) |
| Vanilla JS  | fetch() API, DOM manipulation     |
| Google Fonts| Space Grotesk + Inter typefaces   |

---

## Screenshots

> _Add screenshots of the chat interface here after deployment._

| Light/Dark Mode | Mobile View |
|-----------------|-------------|
| _(screenshot)_  | _(screenshot)_ |

---

## Future Improvements

- Add a keyword-matching layer (check if any known keyword appears inside longer user input)
- Support multiple response variants per intent to reduce repetition
- Add a conversation history display that persists across page reloads (localStorage)
- Build a simple admin panel to add/edit intents without touching Python code
- Add more intents: web development roadmap, career advice, book recommendations
- Dark/Light mode toggle

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## DecodeLabs Project 1 Compliance

This section documents exactly how StudyBuddy Mini satisfies every requirement of **DecodeLabs AI Internship – Project 1**.

| Requirement | Implementation |
|---|---|
| ✅ **Rule-Based Chatbot** | All responses are predefined strings stored in a Python dictionary. No dynamic generation. |
| ✅ **Predefined Responses** | `RESPONSES` dict in `chatbot.py` contains 25+ handcrafted responses, one per intent key. |
| ✅ **Decision-Making Logic** | `get_response()` uses `.get()` for lookups and an `if` guard for empty input. |
| ✅ **Control Flow** | `if not sanitized` guard → dictionary lookup → fallback to `DEFAULT_RESPONSE`. |
| ✅ **Input → Process → Output Model** | User types → `get_response()` sanitizes and looks up → bot bubble appears. |
| ✅ **Continuous Interaction** | Browser chat allows unlimited back-and-forth without page reload (mirrors the CLI while loop). |
| ✅ **Input Sanitization** | `user_message.lower().strip()` in `get_response()` normalises all casing and whitespace. |
| ✅ **Greetings** | Intents: `hello`, `hi`, `hey`, `good morning`, `good evening` – all return friendly responses. |
| ✅ **Exit Commands** | Intents: `bye`, `goodbye`, `exit` – return farewell messages. `is_exit_command()` utility also provided. |
| ✅ **Unknown Input Handling** | `DEFAULT_RESPONSE` returned whenever `.get()` finds no matching key. |
| ✅ **Dictionary Lookup** | `RESPONSES.get(sanitized)` is the primary response engine – no if-elif ladder. |
| ✅ **No APIs** | Zero external API calls anywhere in the project. |
| ✅ **No Machine Learning** | No models, no training, no inference. |
| ✅ **No AI Frameworks** | No OpenAI, LangChain, Transformers, TensorFlow, PyTorch, or similar. |
| ✅ **No NLP Libraries** | No NLTK, spaCy, or any text processing library. |
| ✅ **No Embeddings / Vector Search** | No FAISS, no sentence transformers, no semantic similarity. |
| ✅ **Fully Offline** | Works without an internet connection once dependencies are installed. |
| ✅ **Beginner Friendly** | Each file is fully commented; the entire codebase can be understood in under 15 minutes. |
| ✅ **PEP-8 Compliant Python** | Consistent naming, docstrings on all functions, proper spacing throughout. |
| ✅ **Clean HTML** | Semantic elements (`<header>`, `<main>`, roles, aria-labels). |
| ✅ **Pure CSS** | No Bootstrap, no Tailwind. CSS variables, Flexbox, transitions, and media queries only. |
| ✅ **Modern JavaScript** | `async/await`, `fetch()`, DOM API, `escapeHtml()` XSS guard – no jQuery or libraries. |
