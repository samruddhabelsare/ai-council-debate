import streamlit as st
import requests
import json
import time

# ==========================================
# 0. GLOBAL STYLING & CONSTANTS
# ==========================================

COLORS = {
    "bg_dark": "#050508",
    "bg_card": "rgba(17, 17, 24, 0.7)",
    "neon_green": "#00ff88",
    "neon_blue": "#00d4ff",
    "accent_green": "#00cc66",
    "red": "#ff4455",
    "yellow": "#ffcc00",
    "gold": "#ffd700",
    "text_silver": "#e0e0e0",
    "glass": "rgba(255, 255, 255, 0.03)",
    "border": "rgba(255, 255, 255, 0.1)",
}

def apply_global_styles():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@600;700&family=Orbitron:wght@400;700&display=swap');
    
    .block-container {{ padding-top: 1rem; padding-bottom: 0rem; }}
    
    html, body, [class*="css"] {{
        background: radial-gradient(circle at center, #11111d 0%, {COLORS['bg_dark']} 100%);
        color: {COLORS['text_silver']};
        font-family: 'Rajdhani', sans-serif;
    }}
    
    .debate-wrapper {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    
    .neon-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        color: #fff;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 12px;
        background: linear-gradient(180deg, #fff 40%, {COLORS['neon_green']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px {COLORS['neon_green']}44);
        margin-bottom: -5px;
        animation: titleGlow 3s ease-in-out infinite alternate;
    }}

    @keyframes titleGlow {{
        from {{ filter: drop-shadow(0 0 10px {COLORS['neon_green']}22); }}
        to {{ filter: drop-shadow(0 0 30px {COLORS['neon_green']}66); }}
    }}
    
    .tagline {{
        text-align: center;
        color: {COLORS['neon_green']};
        font-size: 1rem;
        margin-bottom: 2rem;
        font-family: 'Share Tech Mono', monospace;
        letter-spacing: 4px;
        opacity: 0.8;
    }}
    
    /* Sliders & Inputs */
    .stSlider > div {{ accent-color: {COLORS['neon_green']}; }}
    .stTextInput input {{
        background: rgba(0,0,0,0.3) !important;
        border: 1px solid {COLORS['border']} !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        backdrop-filter: blur(10px);
    }}
    
    /* Buttons */
    .stButton > button {{
        background: linear-gradient(135deg, {COLORS['neon_green']}, {COLORS['accent_green']});
        color: #000 !important;
        font-weight: 900;
        font-size: 20px;
        border: none;
        border-radius: 12px;
        padding: 16px 32px;
        width: 100%;
        cursor: pointer;
        box-shadow: 0 0 24px {COLORS['neon_green']}22;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .stButton > button:hover {{
        box-shadow: 0 0 40px {COLORS['neon_green']}44;
        transform: translateY(-2px);
    }}
    
    /* Agent Card Styles */
    .agent-card {{
        background: rgba(20, 20, 30, 0.4);
        border-radius: 16px;
        padding: 16px;
        border: 1px solid rgba(255,255,255,0.05);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
        backdrop-filter: blur(12px);
        margin-bottom: 15px;
        position: relative;
        overflow: hidden;
    }}
    
    .agent-card::after {{
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.03), transparent);
        transform: rotate(45deg);
        transition: 0.5s;
        pointer-events: none;
    }}

    .agent-card:hover {{
        border-color: {COLORS['neon_green']}44;
        transform: translateY(-5px);
        background: rgba(255,255,255,0.08);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    
    .agent-card:hover::after {{
        left: 100%;
    }}

    .agent-card.selected {{
        border-color: {COLORS['neon_green']};
        box-shadow: 0 0 20px {COLORS['neon_green']}22;
        background: rgba(0, 255, 136, 0.05);
    }}
    
    .agent-emoji {{ font-size: 2rem; margin-bottom: 4px; }}
    .agent-name {{ 
        font-family: 'Orbitron', sans-serif;
        font-weight: bold; 
        font-size: 1rem; 
        color: #fff;
        letter-spacing: 1px;
    }}
    .agent-trait {{
        font-size: 0.7rem;
        text-transform: uppercase;
        color: {COLORS['neon_blue']};
        letter-spacing: 1px;
        margin-top: 2px;
    }}
    .agent-bio {{ font-size: 0.75rem; color: #aaa; margin-top: 6px; line-height: 1.3; font-style: italic; }}

    /* Chat Bubbles */
    .bubble-container {{
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        animation: fadeIn 0.5s ease-out forwards;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .bubble-header {{
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        font-size: 0.85rem;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
        color: var(--agent-color);
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    .trait-badge {{
        font-size: 0.65rem;
        background: rgba(255,255,255,0.05);
        padding: 2px 8px;
        border-radius: 4px;
        border: 1px solid var(--agent-color);
        opacity: 0.8;
    }}

    .chat-bubble {{
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        padding: 18px 24px;
        max-width: 90%;
        border: 1px solid {COLORS['border']};
        border-left: 5px solid var(--agent-color);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        font-family: 'Share Tech Mono', monospace;
        font-size: 1.05rem;
        line-height: 1.6;
        color: #eee;
        backdrop-filter: blur(5px);
    }}
    
    /* Currently Speaking Banner */
    .speaking-banner {{
        background: rgba(0, 212, 255, 0.05);
        border: 1px solid {COLORS['neon_blue']}44;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 24px;
        text-align: center;
        backdrop-filter: blur(10px);
        animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
        0% {{ box-shadow: 0 0 0 0px {COLORS['neon_blue']}22; }}
        70% {{ box-shadow: 0 0 0 15px {COLORS['neon_blue']}00; }}
        100% {{ box-shadow: 0 0 0 0px {COLORS['neon_blue']}00; }}
    }}

    .speaking-label {{
        color: {COLORS['neon_blue']};
        font-family: 'Orbitron', sans-serif;
        font-weight: 800;
        letter-spacing: 3px;
        font-size: 1.1rem;
    }}

    .thinking-status {{
        font-size: 0.8rem;
        color: {COLORS['text_silver']};
        opacity: 0.6;
        margin-top: 4px;
        font-family: 'Share Tech Mono', monospace;
    }}
    
    /* Vote Badges */
    .vote-badge {{
        display: inline-block;
        padding: 6px 14px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 0.75rem;
        text-transform: uppercase;
        margin-right: 8px;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
    }}
    .vote-yes {{ background: {COLORS['neon_green']}33; color: {COLORS['neon_green']}; border: 1px solid {COLORS['neon_green']}; }}
    .vote-no {{ background: {COLORS['red']}33; color: {COLORS['red']}; border: 1px solid {COLORS['red']}; }}
    .vote-neutral {{ background: {COLORS['yellow']}33; color: {COLORS['yellow']}; border: 1px solid {COLORS['yellow']}; }}

    /* Judge Card */
    .judge-card {{
        background: linear-gradient(135deg, rgba(42, 32, 0, 0.8), rgba(26, 20, 0, 0.8));
        border: 1px solid {COLORS['gold']};
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 0 50px {COLORS['gold']}22;
        text-align: center;
        margin-top: 40px;
        backdrop-filter: blur(15px);
        animation: slideUp 0.8s cubic-bezier(0.23, 1, 0.32, 1);
    }}

    @keyframes slideUp {{
        from {{ opacity: 0; transform: translateY(40px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .judge-title {{
        color: {COLORS['gold']};
        font-family: 'Orbitron', sans-serif;
        font-size: 2.22rem;
        font-weight: 900;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 4px;
        text-shadow: 0 0 20px {COLORS['gold']}44;
    }}

    .judge-text {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 1.15rem;
        color: #fff;
        line-height: 1.8;
        max-width: 900px;
        margin: 0 auto;
        padding-top: 20px;
        border-top: 1px solid {COLORS['gold']}33;
    }}

    /* Global Scanline Effect */
    body::before {{
        content: " ";
        display: block;
        position: fixed;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 9999;
        background-size: 100% 2px, 3px 100%;
        pointer-events: none;
        opacity: 0.1;
    }}
    
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 1. AGENT ROSTER
# ==========================================

def get_agents():
    return [
        {"id": "analyst",      "name": "Analyst",      "emoji": "🔵", "color": "#1E90FF", "bio": "Cuts through noise with cold logic and data.", "trait": "Logical", "thinking": "Calculating statistical probabilities..."},
        {"id": "critic",       "name": "Critic",        "emoji": "🔴", "color": "#DC143C", "bio": "Nothing escapes scrutiny. Every claim is a target.", "trait": "Skeptical", "thinking": "Searching for logical fallacies..."},
        {"id": "engineer",     "name": "Engineer",      "emoji": "⚙️",  "color": "#708090", "bio": "If it can't be built, it doesn't matter.", "trait": "Pragmatic", "thinking": "Testing structural integrity..."},
        {"id": "optimist",     "name": "Optimist",      "emoji": "🌟", "color": "#32CD32", "bio": "Every problem hides an opportunity.", "trait": "Visionary", "thinking": "Visualizing positive futures..."},
        {"id": "conspiracist", "name": "Conspiracist",  "emoji": "🕵️", "color": "#9400D3", "bio": "The official story is never the real story.", "trait": "Paranoid", "thinking": "Connecting hidden dots..."},
        {"id": "philosopher",  "name": "Philosopher",   "emoji": "🧠", "color": "#4682B4", "bio": "Questions the questions. Ethics over outcomes.", "trait": "Deep", "thinking": "Pondering existential weight..."},
        {"id": "contrarian",   "name": "Contrarian",    "emoji": "🎲", "color": "#FF4500", "bio": "If everyone agrees, something is wrong.", "trait": "Chaotic", "thinking": "Inverting the status quo..."},
        {"id": "scientist",    "name": "Scientist",     "emoji": "🔬", "color": "#00CED1", "bio": "Hypothesis, evidence, conclusion. Nothing else.", "trait": "Empirical", "thinking": "Reviewing peer data..."},
        {"id": "economist",    "name": "Economist",     "emoji": "💰", "color": "#DAA520", "bio": "Follow the money. Always follow the money.", "trait": "Fiscal", "thinking": "Balancing the ledger..."},
        {"id": "provocateur",  "name": "Provocateur",   "emoji": "🧨", "color": "#FF3300", "bio": "Says what no one dares to. Chaos is a tool.", "trait": "Edgy", "thinking": "Priming the explosion..."},
        {"id": "diplomat",     "name": "Diplomat",      "emoji": "🕊️", "color": "#87CEEB", "bio": "Finds the bridge between opposing sides.", "trait": "Zen", "thinking": "Finding common resonance..."},
        {"id": "futurist",     "name": "Futurist",      "emoji": "🤖", "color": "#00FF7F", "bio": "Today's debate is tomorrow's history.", "trait": "Advanced", "thinking": "Simulating future timelines..."},
        {"id": "sage",         "name": "Sage",          "emoji": "🧙", "color": "#CD853F", "bio": "Ancient patterns repeat. Wisdom endures.", "trait": "Wise", "thinking": "Consulting ancient scrolls..."},
        {"id": "psychologist", "name": "Psychologist",  "emoji": "🧬", "color": "#FF69B4", "bio": "Behavior and bias drive every decision.", "trait": "Analytical", "thinking": "Profiling cognitive biases..."},
        {"id": "historian",    "name": "Historian",     "emoji": "📜", "color": "#8B6914", "bio": "Those who forget history are doomed to repeat it.", "trait": "Epochal", "thinking": "Retrieving historical precedents..."},
        {"id": "devil",        "name": "Devil's Advocate", "emoji": "😈", "color": "#CC0000", "bio": "Defends the indefensible to stress-test ideas.", "trait": "Inverse", "thinking": "Stress-testing consensus..."},
        {"id": "judge",        "name": "Judge",         "emoji": "⚖️", "color": "#FFD700", "bio": "Hears all. Decides all. Final word.", "trait": "Absolute", "thinking": "Weighing the cosmic balance..."}
    ]

def get_personality_prompt(agent_id, min_w, max_w):
    prompts = {
        "analyst": (
            "You are the Analyst. You think in systems, data, and evidence. "
            "You break arguments into logical components, cite patterns and statistics, "
            "and dismantle vague claims with precision. You are calm, structured, and unswayed by emotion. "
            "You reference what other agents have said and correct factual gaps."
        ),
        "critic": (
            "You are the Critic. You trust nothing and challenge everything. "
            "You identify logical fallacies, weak assumptions, and missing evidence in every argument. "
            "You are sharp, relentless, and occasionally brutal — but always specific. "
            "Point out exactly which agent said something flawed and why."
        ),
        "engineer": (
            "You are the Engineer. Ideas mean nothing without execution. "
            "You evaluate every proposal for technical feasibility, resource requirements, failure points, "
            "and implementation complexity. You are blunt about what is buildable and what is fantasy. "
            "You push back on idealists with real-world constraints."
        ),
        "optimist": (
            "You are the Optimist. You genuinely believe problems exist to be solved. "
            "You spotlight opportunities, undervalued benefits, and positive second-order effects. "
            "You are enthusiastic but not naive — back your optimism with real possibilities. "
            "Counter the pessimists with specific examples of how things could go right."
        ),
        "conspiracist": (
            "You are the Conspiracist. You believe the surface narrative always hides deeper agendas. "
            "You question who benefits, what is being hidden, and what power structures are at play. "
            "You are paranoid but articulate — your theories are specific, not random. "
            "Challenge other agents on what they are conveniently ignoring."
        ),
        "philosopher": (
            "You are the Philosopher. You interrogate the assumptions beneath the assumptions. "
            "You raise ethical dilemmas, question definitions, and explore what values are really at stake. "
            "You do not rush to conclusions — you make the debate go deeper. "
            "Ask the questions no one else thought to ask."
        ),
        "contrarian": (
            "You are the Contrarian. When consensus forms, you break it. "
            "You take the opposing view not out of stubbornness but because groupthink is dangerous. "
            "You force the debate to consider what is being dismissed too quickly. "
            "Be specific — identify the emerging consensus and directly challenge it."
        ),
        "scientist": (
            "You are the Scientist. You operate by hypothesis, experiment, and falsifiability. "
            "You demand reproducible evidence and reject anecdote. "
            "You cite what is known, what is unknown, and what would need to be tested. "
            "Call out pseudoscience and unverified claims from other agents directly."
        ),
        "economist": (
            "You are the Economist. Every decision has a cost, an incentive, and a market consequence. "
            "You analyze resource allocation, risk-reward tradeoffs, and unintended financial consequences. "
            "You follow incentives to predict behavior and outcomes. "
            "Translate abstract arguments into concrete economic terms."
        ),
        "provocateur": (
            "You are the Provocateur. You say what is uncomfortable, taboo, or explosive. "
            "Your goal is to shatter complacency and force raw, honest reactions. "
            "You are deliberately edgy but not meaningless — every provocation has a point. "
            "Target the most sacred assumptions in the current debate."
        ),
        "diplomat": (
            "You are the Diplomat. You listen more than you speak, and when you speak, you bridge. "
            "You find the legitimate core in opposing arguments and propose synthesis. "
            "You de-escalate without dismissing — you validate tensions before resolving them. "
            "Identify where agents actually agree without realizing it."
        ),
        "futurist": (
            "You are the Futurist. You think in decades, not days. "
            "You extrapolate current trends into long-term consequences and paradigm shifts. "
            "You challenge short-term thinking and raise implications no one has considered yet. "
            "Ground your predictions in real emerging technologies and social patterns."
        ),
        "sage": (
            "You are the Sage. You carry the weight of history and tradition. "
            "You speak in metaphors, parables, and cross-cultural wisdom. "
            "You find the timeless pattern in the current debate. "
            "You are measured, unhurried, and speak with quiet authority that commands attention."
        ),
        "psychologist": (
            "You are the Psychologist. You analyze the hidden biases, cognitive distortions, "
            "and emotional drivers beneath every argument. "
            "You name the psychological phenomena at play — confirmation bias, sunk cost, groupthink. "
            "You reveal why agents believe what they believe, not just what they believe."
        ),
        "historian": (
            "You are the Historian. Every debate has happened before in some form. "
            "You draw direct parallels to historical events, movements, and outcomes. "
            "You warn when the debate is repeating a known mistake. "
            "Use specific historical examples — dates, names, events — to anchor your arguments."
        ),
        "devil": (
            "You are the Devil's Advocate. You defend the least popular position in the room. "
            "Not because you believe it, but because untested ideas are fragile. "
            "You stress-test consensus by arguing the other side as compellingly as possible. "
            "Force the dominant view to prove itself against its strongest counter-argument."
        ),
        "judge": (
            "You are the Judge. You have listened to every argument across every round. "
            "You now synthesize the strongest points from all sides into a clear, reasoned summary. "
            "You identify what was proven, what was disputed, and what remains uncertain. "
            "You deliver a final decision with full reasoning. You are fair, decisive, and final."
        ),
    }

    base = prompts.get(agent_id, "You are a debate council member.")

    vote_rule = (
        f"STRICT WORD RULE: Your response MUST be between {min_w} and {max_w} words. "
        f"Count carefully. Hard cutoff at {max_w} words — trim if needed. "
        "VOTE RULE: You MUST end your response with exactly one of these three tags on its own line: "
        "[VOTE: YES] or [VOTE: NO] or [VOTE: NEUTRAL]. "
        "No other vote format is accepted. The vote tag does NOT count toward your word limit."
    )

    return f"{base}\n\n{vote_rule}"

# ==========================================
# 2. CORE UTILITIES
# ==========================================

def enforce_word_limit(text, max_words):
    words = text.split()
    if len(words) > max_words:
        text = " ".join(words[:max_words])
        if "[VOTE:" not in text:
            text += " ... [VOTE: NO]"
    return text

def run_agent(agent, question, context, config, is_judge=False):
    url = "http://localhost:11434/api/generate"
    min_w, max_w = config["word_range"]
    if is_judge: min_w, max_w = 100, 300
    
    system_prompt = get_personality_prompt(agent["id"], min_w, max_w)
    user_reminder = f"REMINDER: Respond in {min_w}–{max_w} words only. End with [VOTE: YES] or [VOTE: NO]."
    full_prompt = f"System: {system_prompt}\n\nDebate Question: {question}\n\nContext:\n{context}\n\n{user_reminder}\n\nAgent {agent['name']}, your turn:"
    
    try:
        response = requests.post(url, json={"model": config["model"], "prompt": full_prompt, "stream": False}, timeout=90)
        response.raise_for_status()
        text = response.json().get("response", "")
        return enforce_word_limit(text, max_w)
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"

def extract_vote(response):
    res = response.upper()
    if "[VOTE: YES]" in res: return "YES"
    if "[VOTE: NO]" in res: return "NO"
    if "[VOTE: NEUTRAL]" in res: return "NEUTRAL"
    return "NO"  # Default fallback

# ==========================================
# 3. MAIN APPLICATION (Integrated Single Page)
# ==========================================

def main():
    st.set_page_config(page_title="AI Council Debate", layout="wide")
    apply_global_styles()

    if "debating" not in st.session_state:
        st.session_state.debating = False
    if "selected_agents" not in st.session_state:
        st.session_state.selected_agents = ["analyst", "critic", "engineer"]
    if "history" not in st.session_state:
        st.session_state.history = []
    if "votes" not in st.session_state:
        st.session_state.votes = {}

    st.markdown("<div class='debate-wrapper'>", unsafe_allow_html=True)
    st.markdown("<h1 class='neon-title'>AI COUNCIL DEBATE</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>LOCAL DELIBERATION CHAMBER</p>", unsafe_allow_html=True)

    # 1. SETTINGS CONTAINER
    with st.expander("⚙️ CHAMBER CONFIGURATION", expanded=not st.session_state.debating):
        col1, col2 = st.columns([3, 1])
        with col1:
            question = st.text_input("ENTER DEBATE QUESTION", value="Should artificial intelligence be allowed to own intellectual property?")
        with col2:
            model = st.text_input("OLLAMA MODEL", value="gemma2:2b")
        
        col3, col4 = st.columns(2)
        with col3:
            rounds = st.slider("DEBATE ROUNDS", 1, 10, 3)
        with col4:
            word_range = st.select_slider("RESPONSE LENGTH (WORDS)", options=list(range(30, 301, 10)), value=(60, 120))

        st.markdown("### 🎭 SELECT COUNCIL MEMBERS")
        all_agents = [a for a in get_agents() if a["id"] != "judge"]
        
        # Select All Toggle
        select_all = st.checkbox("SELECT ALL AGENTS", value=len(st.session_state.selected_agents) == len(all_agents))
        
        if select_all:
            st.session_state.selected_agents = [a["id"] for a in all_agents]
        
        cols = st.columns(4)
        for idx, agent in enumerate(all_agents):
            with cols[idx % 4]:
                is_sel = agent["id"] in st.session_state.selected_agents
                card_class = "agent-card selected" if is_sel else "agent-card"
                
                st.markdown(f"""
                <div class="{card_class}" style="border-left: 4px solid {agent['color']};">
                    <div class="agent-emoji">{agent['emoji']}</div>
                    <div class="agent-name">{agent['name']}</div>
                    <div class="agent-trait">{agent.get('trait', 'Unit')}</div>
                    <div class="agent-bio">{agent['bio']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Manual toggle if not Select All
                if not select_all:
                    if st.checkbox(f"Add {agent['name']}", value=is_sel, key=f"chk_{agent['id']}", label_visibility="collapsed"):
                        if agent["id"] not in st.session_state.selected_agents:
                            st.session_state.selected_agents.append(agent["id"])
                    else:
                        if agent["id"] in st.session_state.selected_agents:
                            st.session_state.selected_agents.remove(agent["id"])

        st.markdown("---")
        if len(st.session_state.selected_agents) < 2:
            st.warning("⚠️ CHOOSE AT LEAST 2 AGENTS.")
        else:
            if st.button("⚡ BEGIN DELIBERATION"):
                st.session_state.debate_config = {
                    "question": question, "model": model, "rounds": rounds, 
                    "word_range": word_range, "agents": list(set(st.session_state.selected_agents))
                }
                st.session_state.history = []
                st.session_state.votes = {}
                st.session_state.debating = True
                st.rerun()

    # 2. DEBATE CONTAINER (Renders below settings)
    if (st.session_state.debating or st.session_state.history) and "debate_config" in st.session_state:
        config = st.session_state.debate_config
        st.markdown("---")
        
        if st.button("🗑️ RESET CHAMBER"):
            st.session_state.debating = False
            st.session_state.history = []
            st.session_state.votes = {}
            st.rerun()

        main_col, side_col = st.columns([7, 3])
        
        with side_col:
            st.markdown("### 📊 REPORT")
            progress_bar = st.progress(0)
            status_box = st.empty()
            st.markdown("---")
            st.markdown("#### VOTE TALLY")
            vote_area = st.container()
            st.markdown("---")
            st.markdown("#### ACTIVE ROSTER")
            all_agents_lookup = {a["id"]: a for a in get_agents()}
            for aid in config["agents"] + ["judge"]:
                a = all_agents_lookup[aid]
                st.markdown(f"<span style='color:{a['color']}'>●</span> {a['emoji']} {a['name']}", unsafe_allow_html=True)

        with main_col:
            feed = st.container()
            
            # Display History
            for entry in st.session_state.history:
                a = entry["agent"]
                with feed:
                    st.markdown(f"""
                    <div class="bubble-container">
                        <div class="bubble-header" style="--agent-color:{a['color']}">
                            {a['emoji']} {a['name']} 
                            <span class="trait-badge" style="--agent-color:{a['color']}">{a.get('trait', 'Core')}</span>
                        </div>
                        <div class="chat-bubble" style="--agent-color:{a['color']}">{entry['message']}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            if st.session_state.debating:
                history = st.session_state.history
                current_count = len(history)
                debate_agents = [all_agents_lookup[aid] for aid in config["agents"]]
                judge_agent = all_agents_lookup["judge"]
                total_turns = (config["rounds"] * len(debate_agents)) + 1
                
                if current_count < (config["rounds"] * len(debate_agents)):
                    current_round = (current_count // len(debate_agents)) + 1
                    agent_idx = current_count % len(debate_agents)
                    active_agent = debate_agents[agent_idx]
                    
                    progress_bar.progress(current_count / total_turns, text=f"Round {current_round} of {config['rounds']}")
                    status_box.markdown(f"""
                    <div class='speaking-banner'>
                        <span class='speaking-label'>🎙️ ACTIVE: {active_agent['name']}</span>
                        <div class='thinking-status'>[ {active_agent.get('thinking', 'Processing...')} ]</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    context = "\n".join([f"{h['agent']['name']}: {h['message']}" for h in history])
                    with st.spinner(f"{active_agent['name']} deliberating..."):
                        response = run_agent(active_agent, config["question"], context, config)
                    
                    vote = extract_vote(response)
                    if current_round not in st.session_state.votes:
                        st.session_state.votes[current_round] = {"YES": 0, "NO": 0, "NEUTRAL": 0}
                    st.session_state.votes[current_round][vote] += 1
                    
                    st.session_state.history.append({"agent": active_agent, "message": response, "vote": vote})
                    st.rerun()
                    
                elif current_count == (config["rounds"] * len(debate_agents)):
                    status_box.markdown(f"""
                    <div class='speaking-banner' style='border-color:{judge_agent['color']}'>
                        <span class='speaking-label' style='color:{judge_agent['color']}'>⚖️ DELIBERATING: {judge_agent['name']}</span>
                        <div class='thinking-status'>[ {judge_agent.get('thinking', 'Finalizing verdict...')} ]</div>
                    </div>
                """, unsafe_allow_html=True)
                    context = "\n".join([f"{h['agent']['name']}: {h['message']}" for h in history])
                    with st.spinner("Final review..."):
                        response = run_agent(judge_agent, config["question"], context, config, is_judge=True)
                    
                    st.session_state.history.append({"agent": judge_agent, "message": response, "vote": extract_vote(response)})
                    st.session_state.debating = False
                    st.rerun()

        # Sidebar Votes and Final Verdict
        with side_col:
            with vote_area:
                for r, v in st.session_state.votes.items():
                    st.markdown(f"""
                    <div style='margin-bottom:8px;'>
                        <span class='vote-badge vote-yes'>YES {v['YES']}</span> 
                        <span class='vote-badge vote-no'>NO {v['NO']}</span>
                        <span class='vote-badge vote-neutral'>MID {v['NEUTRAL']}</span>
                    </div>
                    """, unsafe_allow_html=True)

        if not st.session_state.debating and st.session_state.history:
            judge_entry = st.session_state.history[-1]
            st.markdown(f"""
            <div class='judge-card'>
                <div class='judge-title'>⚖️ FINAL VERDICT: {judge_entry['vote']}</div>
                <div class='judge-text'>{judge_entry['message']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
