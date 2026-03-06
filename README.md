# ⚡ AI Council Debate Chamber

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_AI-black?style=for-the-badge&logo=ollama&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Cloud](https://img.shields.io/badge/Cloud-None-red?style=for-the-badge)

**_17 AI Personalities. One Question. Pure Local Chaos._**

⚡ Debate Hard &nbsp;·&nbsp; 🧠 Think Deep &nbsp;·&nbsp; ⚖️ Judge Fair

</div>

---

## 📌 Overview

**AI Council Debate Chamber** is a fully local, cinematic multi-agent debate system where 17 distinct AI personalities argue, challenge each other, and vote on any question you throw at them — all running on your own machine with zero cloud, zero APIs, and zero data leaving your device.

Built with **Python**, **Streamlit**, and **Ollama**, the app lets you hand-pick your council, set response word limits, define debate rounds, then watch the chamber come alive with live chat bubbles, per-round vote tallies, and a final Judge verdict — all inside a dark neon UI with scanline effects and glowing animations.

> *"17 agents walk into a debate. Only the Judge walks out with the final word."*

---

## ✨ Features

### ⚙️ Chamber Configuration
- Enter any debate question — philosophy, tech, ethics, geopolitics, anything
- Select your **Ollama model** (default: `gemma2:2b`, works with `llama3`, `mistral`, etc.)
- Set **Debate Rounds** via slider (1–10)
- Set **Agent Response Word Range** via dual slider (30–300 words)
- All settings auto-injected into every agent's system prompt

### 🎭 Agent Selection — 17 Unique Personalities
Pick any combination of agents using checkbox cards in a 4-column grid. The **Judge** is always included automatically.

| Agent | Trait | Role |
|---|---|---|
| 🔵 Analyst | Logical | Cold data and structured reasoning |
| 🔴 Critic | Skeptical | Destroys weak arguments on sight |
| ⚙️ Engineer | Pragmatic | Reality-checks every proposal |
| 🌟 Optimist | Visionary | Finds the opportunity in every problem |
| 🕵️ Conspiracist | Paranoid | Connects hidden dots and questions motives |
| 🧠 Philosopher | Deep | Ethics, definitions, and deeper meaning |
| 🎲 Contrarian | Chaotic | Breaks consensus the moment it forms |
| 🔬 Scientist | Empirical | Demands peer-reviewed evidence only |
| 💰 Economist | Fiscal | Follows the money, always |
| 🧨 Provocateur | Edgy | Says what no one dares to say |
| 🕊️ Diplomat | Zen | Bridges opposites and seeks synthesis |
| 🤖 Futurist | Advanced | Thinks in decades, not days |
| 🧙 Sage | Wise | Ancient wisdom meets modern questions |
| 🧬 Psychologist | Analytical | Exposes the bias behind every argument |
| 📜 Historian | Epochal | Finds the historical parallel every time |
| 😈 Devil's Advocate | Inverse | Defends the indefensible to stress-test ideas |
| ⚖️ Judge | Final | Delivers the verdict — always last |

### 🗣️ Multi-Round Debate Engine
- Agents speak sequentially each round — no parallel overload on your machine
- Every agent receives the full prior conversation as context
- Agents reference and challenge each other by name
- Configurable word limit enforced via both prompt injection and hard code truncation fallback

### 🗳️ Per-Round Voting System
- Every agent ends their response with `[VOTE: YES]`, `[VOTE: NO]`, or `[VOTE: NEUTRAL]`
- Votes are parsed and tallied automatically after each round
- Live vote badges displayed in the sidebar: 
  `YES ✅` · `NO ❌` · `MID ⚡`

### ⚖️ Final Judge Verdict
- After all debate rounds complete, the **Judge** reviews the entire transcript
- Delivers a synthesized summary and a clear final decision
- Displayed in a gold-bordered animated verdict card

### 🎨 Cinematic Dark UI
- Orbitron + Share Tech Mono + Rajdhani fonts via Google Fonts
- Animated neon glowing title with `titleGlow` CSS keyframe
- Scanline CRT effect overlay across the entire app
- Chat bubbles with agent-colored left borders and glassmorphism styling
- Pulsing `🎙️ ACTIVE:` speaking banner during live debate
- Agent cards with shimmer hover effect and selection glow
- Judge card with gold gradient border and `slideUp` entrance animation

---

## 🖥️ Interface Layout

```
╔══════════════════════════════════════════════════════════════════╗
║  ⚡ AI COUNCIL DEBATE CHAMBER                                   ║
║  ─────────────────────────────────────────────────────────────  ║
║  [ Question Input ]      [ Ollama Model ]                       ║
║  [ Rounds Slider  ]      [ Word Range Slider ]                  ║
║  ─────────────────────────────────────────────────────────────  ║
║  🎭 SELECT COUNCIL MEMBERS  [ 4-column agent checkbox grid ]    ║
║                              [ ⚡ BEGIN DELIBERATION ]          ║
╠══════════════════════════════════════════════════════════════════╣
║  DEBATE FEED (70%)          │  REPORT PANEL (30%)              ║
║  ┌───────────────────────┐  │  Round X of Y  [progress bar]    ║
║  │ 🔵 ANALYST  [Logical] │  │  ─────────────────────────────  ║
║  │ response bubble here  │  │  VOTE TALLY                      ║
║  └───────────────────────┘  │  YES 3 │ NO 1 │ MID 2           ║
║  ┌───────────────────────┐  │  ─────────────────────────────  ║
║  │ 🔴 CRITIC  [Skeptical]│  │  ACTIVE ROSTER                  ║
║  │ response bubble here  │  │  ● 🔵 Analyst                   ║
║  └───────────────────────┘  │  ● 🔴 Critic ...                ║
╠══════════════════════════════════════════════════════════════════╣
║  ⚖️  FINAL VERDICT: YES                                          ║
║  [ Judge summary and full reasoning text ]                      ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🗂️ Project Structure

```
ai-council-debate-chamber/
│
├── app.py           # Single-file Streamlit application — everything lives here
└── README.md        # This file
```

> This is a **single-file project** — all UI, agents, debate logic, styling, and vote handling are in `app.py`.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `streamlit` | Web app framework — UI, layout, state, widgets |
| `requests` | Calls Ollama REST API at `localhost:11434` |
| `json` | Parses Ollama API responses |
| `ollama` (local) | Runs the LLM locally — not a Python package |

---

## 📦 Installation

### Prerequisites

- Python **3.8 or higher**
- [Ollama](https://ollama.com) installed and running locally
- At least one model pulled in Ollama (e.g. `llama3`, `gemma2:2b`, `mistral`)

### Step 1 — Pull an Ollama Model

```bash
ollama pull gemma2:2b
# or
ollama pull llama3
```

### Step 2 — Clone the Repository

```bash
git clone https://github.com/your-username/ai-council-debate-chamber.git
cd ai-council-debate-chamber
```

### Step 3 — Install Dependencies

```bash
pip install streamlit requests
```

### Step 4 — Start Ollama

```bash
ollama serve
```

### Step 5 — Launch the App

```bash
streamlit run app.py
```

App opens at **`http://localhost:8501`**

---

## 🚀 Usage

1. Open the app — the **Chamber Configuration** expander is open by default
2. Type your debate question in the input field
3. Set your Ollama model name (must match what you have pulled locally)
4. Adjust the **Rounds** and **Word Range** sliders
5. Check or uncheck agents from the 4-column grid — minimum 2 required
6. Click **⚡ BEGIN DELIBERATION**
7. Watch agents debate live in the feed — speaking banner updates each turn
8. Track votes per round in the sidebar Report panel
9. After the final round, the **Judge verdict card** appears at the bottom
10. Click **🗑️ RESET CHAMBER** to start a new debate

---

## 🧠 Agent System Design

Each agent has:
- A **personality system prompt** defining their unique worldview and debate behavior
- A **word limit rule** injected into both the system prompt and the user message each turn
- A **`thinking` status** string shown in the speaking banner while they generate
- A **`trait` label** displayed as a badge on their chat bubble

Word limit is enforced at two levels:
1. **Prompt level** — agents are instructed to count words and stay within range
2. **Code level** — `enforce_word_limit()` hard-truncates any response that exceeds `max_words` and re-attaches a vote tag if it was cut off

---

## ⚠️ Known Limitations

- Response quality and word adherence depend on the local model used — larger models follow instructions better
- The app requires Ollama to be running at `http://localhost:11434` before launching
- No debate history is saved between sessions — everything resets on page refresh
- Very long debates (10 rounds × 16 agents) may take significant time depending on hardware

---

## 🔮 Future Improvements

- [ ] Export full debate transcript as `.txt` or `.pdf`
- [ ] Add a temperature slider per agent for personality intensity control
- [ ] Custom agent creator — define your own personality via the UI
- [ ] Debate replay mode — step through history without re-running
- [ ] Agent agreement heatmap showing who sided with whom each round
- [ ] Support for multi-model debates (different agents using different local models)

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Make your changes in `app.py`
4. Test: `streamlit run app.py`
5. Commit: `git commit -m "Add: your feature"`
6. Push and open a **Pull Request**

---

## 📄 License

```
MIT License — free to use, modify, and distribute.
```

---

## 👨‍💻 Author

<div align="center">

**Samruddha Belsare**

🇮🇳 &nbsp; India &nbsp;·&nbsp; Built with ❤️ and Local LLMs

*"17 agents walk into a debate. Only the Judge walks out with the final word."*

---

*Built for anyone who ever wanted to watch AI argue with itself  and actually learn something from it.* ⚡

</div>

---

<div align="center">

```
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█   ⚡ AI COUNCIL DEBATE CHAMBER  ·  Local. Private. Raw  █
█   Built with  Streamlit  ·  Ollama  ·  Pure Python      █
█   ──────────────────────────────────────────────────    █
█         ⚡ Debate Hard   🧠 Think Deep   ⚖️ Judge Fair   █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
```

*© 2026 · AI Council Debate Chamber · No cloud. No API keys. Just your machine and 17 opinions.* ⚡

⭐ If this project made you think, give it a star on GitHub!

</div>
