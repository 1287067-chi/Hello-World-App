import streamlit as st
import streamlit.components.v1 as components
import time
import random

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="Hello World Motion Lab", layout="wide")

# -------------------------------------------------
# USER CONTROLS
# -------------------------------------------------
st.sidebar.header("Controls")

name = st.sidebar.text_input("Enter your name", "Hello World")

font_family = st.sidebar.selectbox(
    "Font type",
    ["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana", "Trebuchet MS", "Tahoma"]
)

font_size = st.sidebar.slider("Font size (px)", 20, 120, 48)

background = st.sidebar.selectbox(
    "Background",
    ["Light", "Dark", "Ocean", "Sunset"]
)

name_mode = st.sidebar.selectbox(
    "Name display mode",
    ["Centered", "Ticker Tape", "Repeated"]
)

effect = st.sidebar.selectbox(
    "Dynamic action",
    ["None", "Rain", "Snow", "Hail", "Wind", "Confetti", "Tornado"]
)

speed = st.sidebar.slider("Animation speed", 0.05, 0.5, 0.15)

# -------------------------------------------------
# SESSION STATE FOR ANIMATION
# -------------------------------------------------
if "tick" not in st.session_state:
    st.session_state.tick = 0
st.session_state.tick += 1

# -------------------------------------------------
# COLORS
# -------------------------------------------------
bg_map = {
    "Light": ("#ffffff", "#000000"),
    "Dark": ("#000000", "#ffffff"),
    "Ocean": ("#0b1f2a", "#dff6ff"),
    "Sunset": ("#3a1c71", "#ffd6a5"),
}

bg_color, text_color = bg_map[background]

# -------------------------------------------------
# EFFECT SYMBOLS
# -------------------------------------------------
effect_symbols = {
    "Rain": "💧",
    "Snow": "❄️",
    "Hail": "🧊",
    "Wind": "💨",
    "Confetti": "🎉",
    "Tornado": "🌪️",
    "None": ""
}
symbol = effect_symbols[effect]

# -------------------------------------------------
# NAME HTML
# -------------------------------------------------
if name_mode == "Ticker Tape":
    offset = st.session_state.tick % 100
    name_html = f"""
    <div style="
        white-space:nowrap;
        margin-left:{offset * 8}px;
        font-weight:bold;
        letter-spacing:1px;
    ">
        {name}
    </div>
    """
elif name_mode == "Repeated":
    name_html = "<br>".join([name] * 6)
else:
    name_html = f"""
    <div style="text-align:center; font-weight:bold; letter-spacing:1px;">
        {name}
    </div>
    """

# -------------------------------------------------
# DYNAMIC EFFECT FIELD (BEHIND NAME)
# -------------------------------------------------
effect_html = ""
if effect != "None":
    for _ in range(12):
        line = "".join(random.choice([symbol, "&nbsp;"]) for _ in range(80))
        effect_html += f"<div style='white-space:nowrap; font-size:{font_size // 2}px;'>{line}</div>"

# -------------------------------------------------
# FINAL HTML (LAYERS)
# -------------------------------------------------
html = f"""
<div style="
    position:relative;
    background: linear-gradient(135deg, {bg_color}, {bg_color});
    color:{text_color};
    height:80vh;
    padding:40px;
    font-family:{font_family};
    overflow:hidden;
    border-radius:18px;
    box-shadow: inset 0 0 20px rgba(255,255,255,0.08);
">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0.8;">
        {effect_html}
    </div>

    <div style="
        position:relative;
        z-index:10;
        font-size:{font_size}px;
        text-align:center;
        width:100%;
        margin-top:15vh;
        text-shadow: 0 0 12px rgba(255,255,255,0.25);
    ">
        {name_html}
    </div>
</div>
"""

components.html(html, height=650)

# -------------------------------------------------
# CONTROLLED ANIMATION LOOP
# -------------------------------------------------
time.sleep(speed)
st.rerun()