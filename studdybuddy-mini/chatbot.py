# =============================================================================
# chatbot.py – StudyBuddy Mini
# Rule-Based Response Engine
#
# This module contains ALL chatbot logic.
# No AI, No ML, No APIs, No Internet – pure Python dictionary lookups.
# =============================================================================

# ---------------------------------------------------------------------------
# PRIMARY RESPONSE DICTIONARY
# Each key is a sanitized user input string.
# Each value is the predefined response StudyBuddy will return.
# ---------------------------------------------------------------------------
RESPONSES = {

    # ── Greetings ────────────────────────────────────────────────────────────
    "hello": (
        "Hey there! 👋 I'm StudyBuddy Mini, your rule-based learning companion. "
        "Ask me about programming, study tips, or just say hi anytime!"
    ),
    "hi": (
        "Hi! Great to see you here. 😊 I'm ready to help you learn. "
        "Type 'help' to see what I can do."
    ),
    "hey": (
        "Hey! What are we learning today? "
        "Try asking about Python, DSA, or grab some study tips!"
    ),
    "good morning": (
        "Good morning! ☀️ Starting the day with some learning? That's the spirit! "
        "What topic shall we tackle first?"
    ),
    "good evening": (
        "Good evening! 🌙 Evening study sessions can be super productive. "
        "What would you like to explore today?"
    ),

    # ── Farewells ────────────────────────────────────────────────────────────
    "bye": (
        "Goodbye! 👋 Keep up the great work. "
        "Every bit of learning adds up. See you next time!"
    ),
    "goodbye": (
        "Take care! 🚀 Remember: consistent practice beats cramming every time. "
        "Come back whenever you need a study buddy!"
    ),
    "exit": (
        "Exiting StudyBuddy Mini. Keep learning, keep growing! 💪"
    ),

    # ── Programming Topics ────────────────────────────────────────────────────
    "python": (
        "🐍 Python is one of the best first languages to learn!\n\n"
        "Key strengths:\n"
        "• Clean, readable syntax – almost like pseudocode\n"
        "• Massive standard library and ecosystem (pip)\n"
        "• Used in Web Dev, Data Science, AI/ML, Automation, and more\n\n"
        "Start with: variables → loops → functions → OOP → projects.\n"
        "Recommended resource: python.org/doc or freeCodeCamp Python course."
    ),
    "java": (
        "☕ Java is a rock-solid, object-oriented language used everywhere!\n\n"
        "Key strengths:\n"
        "• 'Write Once, Run Anywhere' – runs on the JVM\n"
        "• Strongly typed – teaches discipline early\n"
        "• Powers Android apps, enterprise systems, and big tech backends\n\n"
        "Start with: Hello World → data types → OOP concepts → collections → projects."
    ),
    "c++": (
        "⚡ C++ is powerful, fast, and teaches you how computers really work!\n\n"
        "Key strengths:\n"
        "• High performance – used in game engines, OS, embedded systems\n"
        "• Manual memory management builds deep understanding\n"
        "• Foundation for competitive programming\n\n"
        "Start with: syntax → pointers → OOP → STL → competitive problem solving."
    ),
    "javascript": (
        "🌐 JavaScript is the language of the web!\n\n"
        "Key strengths:\n"
        "• Runs natively in every browser – no setup needed\n"
        "• Full-stack capable: frontend (React/Vue) + backend (Node.js)\n"
        "• Huge job market demand\n\n"
        "Start with: DOM manipulation → events → async/await → React → Node.js."
    ),
    "html": (
        "🏗️ HTML is the skeleton of every webpage!\n\n"
        "Key concepts:\n"
        "• Semantic elements: <header>, <main>, <article>, <footer>\n"
        "• Forms, links, images, and media embeds\n"
        "• Accessibility (alt text, ARIA roles) matters from day one\n\n"
        "Tip: Always write semantic HTML before adding CSS. Structure first, style second."
    ),
    "css": (
        "🎨 CSS is where design meets code!\n\n"
        "Key concepts:\n"
        "• Box model: margin → border → padding → content\n"
        "• Flexbox for 1D layouts, Grid for 2D layouts\n"
        "• CSS Variables (--var-name) for maintainable themes\n"
        "• Responsive design with media queries\n\n"
        "Pro tip: Master Flexbox and Grid — they'll handle 90% of your layout needs."
    ),
    "sql": (
        "🗄️ SQL is the universal language of databases!\n\n"
        "Core commands to master:\n"
        "• SELECT, FROM, WHERE – querying data\n"
        "• JOIN – combining tables\n"
        "• GROUP BY + aggregate functions (COUNT, SUM, AVG)\n"
        "• INSERT, UPDATE, DELETE – data manipulation\n\n"
        "Practice on: SQLiteOnline.com or Mode Analytics SQL Tutorial."
    ),
    "ai": (
        "🤖 Artificial Intelligence is transforming every industry!\n\n"
        "The learning path:\n"
        "1. Python (strong foundation first)\n"
        "2. Math: Linear Algebra, Calculus, Probability\n"
        "3. Machine Learning (scikit-learn)\n"
        "4. Deep Learning (PyTorch or TensorFlow)\n"
        "5. Specializations: NLP, Computer Vision, Reinforcement Learning\n\n"
        "Fun fact: Even without AI models, smart rule-based systems like me "
        "can feel surprisingly capable! 😄"
    ),
    "dsa": (
        "🧩 Data Structures & Algorithms – the heart of software engineering!\n\n"
        "Study order:\n"
        "1. Arrays & Strings\n"
        "2. Linked Lists, Stacks, Queues\n"
        "3. Trees & Graphs\n"
        "4. Sorting & Searching\n"
        "5. Dynamic Programming\n\n"
        "Platforms to practice: LeetCode, HackerRank, Codeforces\n"
        "Rule of thumb: Understand the pattern, not just the solution."
    ),
    "github": (
        "🐙 GitHub is your coding portfolio and collaboration hub!\n\n"
        "Essential Git commands:\n"
        "• git init / git clone – start a repo\n"
        "• git add . && git commit -m 'msg' – save changes\n"
        "• git push origin main – upload to GitHub\n"
        "• git pull – sync with remote\n"
        "• git branch / git checkout -b – branching\n\n"
        "Tip: Commit small, commit often. Your commit history tells your story."
    ),

    # ── Study Help ────────────────────────────────────────────────────────────
    "study tips": (
        "📚 Here are proven study strategies that actually work:\n\n"
        "1. Pomodoro Technique – 25 min focus, 5 min break\n"
        "2. Active Recall – test yourself instead of re-reading\n"
        "3. Spaced Repetition – review material at growing intervals\n"
        "4. Feynman Technique – explain it simply to confirm you understand\n"
        "5. One topic at a time – multitasking kills deep learning\n\n"
        "Remember: Quality of study > Hours of study."
    ),
    "exam tips": (
        "📝 Exam preparation tips:\n\n"
        "• Start revision at least 7 days before the exam\n"
        "• Make a prioritized topic list – high weight topics first\n"
        "• Practice past papers under timed conditions\n"
        "• Sleep 7–8 hours the night before – memory consolidates during sleep\n"
        "• On exam day: read all questions first, then attempt easiest ones first\n\n"
        "You've got this! Preparation is the only antidote to exam anxiety. 💪"
    ),
    "concentration": (
        "🎯 Struggling to concentrate? Here's what helps:\n\n"
        "• Remove your phone from the room (not just silenced – removed)\n"
        "• Use website blockers during study blocks (Cold Turkey, Freedom)\n"
        "• Study in the same place every day – build a habit trigger\n"
        "• Background music? Try lo-fi beats or brown noise\n"
        "• Hydrate! Even mild dehydration reduces focus significantly\n\n"
        "The first 5 minutes are the hardest. Just start."
    ),
    "revision": (
        "🔄 Smart revision strategies:\n\n"
        "• Don't re-read passively – use flashcards or practice problems\n"
        "• Spaced repetition: Day 1 → Day 3 → Day 7 → Day 21\n"
        "• Mind maps help connect concepts visually\n"
        "• Teach what you've revised to a friend or even to yourself out loud\n"
        "• Review mistakes more than correct answers\n\n"
        "Revision is not re-learning – it's reinforcing what you know."
    ),
    "motivation": (
        "🔥 Feeling unmotivated? Let's fix that:\n\n"
        "• Remember your WHY – why did you start this journey?\n"
        "• Progress > Perfection. One step forward is still forward.\n"
        "• Comparison is the thief of joy – compete with yesterday's you\n"
        "• Break big goals into tiny daily wins\n"
        "• Celebrate small victories – they compound into big results\n\n"
        "You showed up today. That already puts you ahead of the version of "
        "you that didn't. Keep going. 🚀"
    ),

    # ── Fun ──────────────────────────────────────────────────────────────────
    "joke": (
        "😄 Here's one for you:\n\n"
        "Why do programmers prefer dark mode?\n\n"
        "...Because light attracts bugs! 🐛\n\n"
        "(Get it? Bugs in code? I'll see myself out.)"
    ),
    "fun fact": (
        "🤯 Fun fact time!\n\n"
        "The first computer bug was a real bug. In 1947, Grace Hopper's team "
        "found a moth stuck in a relay of the Harvard Mark II computer. "
        "They taped it into their logbook and wrote: 'First actual case of bug being found.'\n\n"
        "That's where the term 'debugging' comes from! 🦋"
    ),
    "quote": (
        "💬 Here's a quote to fuel your day:\n\n"
        "\"Any fool can write code that a computer can understand. "
        "Good programmers write code that humans can understand.\"\n\n"
        "— Martin Fowler\n\n"
        "Clean, readable code is a skill worth developing from day one."
    ),

    # ── About ─────────────────────────────────────────────────────────────────
    "who are you": (
        "👋 I'm StudyBuddy Mini – a rule-based learning companion built by Shivansh Pathak.\n\n"
        "What makes me special:\n"
        "• I work completely offline – no internet required\n"
        "• No AI, no ML, no APIs – just clean Python logic\n"
        "• I use a dictionary lookup system to respond deterministically\n"
        "• I was built as DecodeLabs AI Internship Project 1\n\n"
        "I appear intelligent because of good software engineering, not magic! 🧠"
    ),
    "help": (
        "🆘 Here's everything I know about:\n\n"
        "💻 Programming: python, java, c++, javascript, html, css, sql, ai, dsa, github\n"
        "📚 Study Help: study tips, exam tips, concentration, revision, motivation\n"
        "😄 Fun Stuff: joke, fun fact, quote\n"
        "👋 Greetings: hello, hi, hey, good morning, good evening\n"
        "👋 Farewell: bye, goodbye, exit\n"
        "ℹ️ About: who are you, help\n\n"
        "Just type any of those topics and I'll respond!"
    ),
}

# ---------------------------------------------------------------------------
# DEFAULT RESPONSE
# Returned when the user's input doesn't match any key in RESPONSES.
# ---------------------------------------------------------------------------
DEFAULT_RESPONSE = (
    "🤔 Hmm, I don't have a predefined answer for that.\n\n"
    "I'm a rule-based chatbot, so I only know what I've been taught!\n"
    "Try typing 'help' to see all the topics I can discuss."
)

# ---------------------------------------------------------------------------
# EXIT KEYWORDS
# If the user types any of these, the response will signal a farewell.
# ---------------------------------------------------------------------------
EXIT_KEYWORDS = {"bye", "goodbye", "exit"}


# ---------------------------------------------------------------------------
# get_response()
# Core function – takes raw user input, sanitizes it, and returns a response.
#
# Input Processing (IPO Model):
#   INPUT  → raw string from the user
#   PROCESS → sanitize (lower + strip), dictionary lookup, fallback to default
#   OUTPUT → predefined response string
# ---------------------------------------------------------------------------
def get_response(user_message: str) -> str:
    """
    Process user input and return a predefined response.

    Args:
        user_message (str): Raw text typed by the user.

    Returns:
        str: The matched predefined response, or the default fallback.
    """

    # Step 1: Input Sanitization
    # Convert to lowercase and remove leading/trailing whitespace.
    # This ensures 'Hello', 'HELLO', 'hello' all map to the same key.
    sanitized = user_message.lower().strip()

    # Step 2: Guard clause – empty input
    if not sanitized:
        return "It looks like you didn't type anything. Try 'help' to see what I can do! 😊"

    # Step 3: Dictionary Lookup (primary decision engine)
    # .get() returns the matched response or None if no key found.
    response = RESPONSES.get(sanitized)

    # Step 4: Fallback to default if no match
    if response is None:
        return DEFAULT_RESPONSE

    return response


def is_exit_command(user_message: str) -> bool:
    """
    Check whether the user's message is an exit/farewell command.

    Args:
        user_message (str): Raw text typed by the user.

    Returns:
        bool: True if the message is an exit keyword, False otherwise.
    """
    sanitized = user_message.lower().strip()
    return sanitized in EXIT_KEYWORDS
