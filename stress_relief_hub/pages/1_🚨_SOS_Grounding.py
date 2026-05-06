import streamlit as st
import time
from utils.styles import load_css
from utils.data_manager import add_meditation_session
from utils.cbt_tools import GROUNDING_TECHNIQUES, PANIC_FIRST_AID, PROGRESSIVE_MUSCLE_RELAXATION
from utils.audio_utils import generate_tone, audio_to_bytes, SAMPLE_RATE
import numpy as np

st.set_page_config(page_title="SOS & Grounding", page_icon="🚨", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🚨 SOS Panic Support")

st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #ff416c, #ff4b2b); 
            border-radius: 15px; color: white; margin-bottom: 20px;">
    <h2>If you are in immediate danger, call 988 or emergency services.</h2>
    <p>You are safe. This moment is temporary. Help is available.</p>
</div>
""", unsafe_allow_html=True)

# Panic First Aid
st.subheader("📋 Panic Attack First Aid")
for step, text in PANIC_FIRST_AID.items():
    idx = list(PANIC_FIRST_AID.keys()).index(step) + 1
    with st.expander("Step " + str(idx) + ": " + step):
        st.write(text)

st.markdown("---")

# Emergency breathing with visual pacer
st.subheader("🫁 Emergency Breathing Pacer")
st.write("Follow the expanding and contracting circle. Breathe with it.")

if st.button("🆘 Start Emergency Breathing (4-7-8)", use_container_width=True, type="primary"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    circle = st.empty()

    cycles = 4
    for cycle in range(cycles):
        status_text.markdown("### 🫁 Cycle " + str(cycle+1) + "/" + str(cycles) + " — **INHALE** (4s)")
        for i in range(100):
            progress_bar.progress(min(int(((cycle * 100 + i) / (cycles * 100)) * 100), 100))
            size = 120 + int(i * 1.5)
            circle.markdown(
                "<div style='width:" + str(size) + "px;height:" + str(size) + "px;border-radius:50%;"
                "background:radial-gradient(circle, #a8edea, #667eea);"
                "margin:0 auto;box-shadow:0 0 40px rgba(102,126,234,0.6);'></div>",
                unsafe_allow_html=True
            )
            time.sleep(4 / 100)

        status_text.markdown("### ⏸️ **HOLD** (7s)")
        time.sleep(7)

        status_text.markdown("### 😮‍💨 **EXHALE** (8s)")
        for i in range(100, 0, -1):
            size = 120 + int(i * 1.5)
            circle.markdown(
                "<div style='width:" + str(size) + "px;height:" + str(size) + "px;border-radius:50%;"
                "background:radial-gradient(circle, #fed6e3, #ff416c);"
                "margin:0 auto;box-shadow:0 0 30px rgba(255,65,108,0.5);'></div>",
                unsafe_allow_html=True
            )
            time.sleep(8 / 100)

    progress_bar.empty()
    status_text.empty()
    circle.empty()
    st.success("You did it. The wave has passed. You are safe. 💙")
    add_meditation_session("Emergency Breathing", 76)

st.markdown("---")

st.subheader("🧊 Cold Water Reset")
st.write("Activates the mammalian dive reflex — rapidly calms your nervous system.")
st.info("Hold ice cubes, splash cold water on your face, or hold a cold pack to your chest for 30 seconds.")

if st.button("⏱️ Start 30-Second Timer", use_container_width=True):
    timer = st.empty()
    for i in range(30, 0, -1):
        timer.markdown("### ⏱️ " + str(i) + " seconds remaining...")
        time.sleep(1)
    timer.markdown("### ✅ Done! Notice your heart rate slowing.")

st.markdown("---")

st.subheader("👁️ 5-4-3-2-1 Senses Grounding")
for step in GROUNDING_TECHNIQUES["5-4-3-2-1 Senses"]["steps"]:
    st.write(step)

st.markdown("---")

st.subheader("🛠️ More Grounding Techniques")
for name, technique in GROUNDING_TECHNIQUES.items():
    if name == "5-4-3-2-1 Senses":
        continue
    with st.expander(name):
        st.write(technique["description"])
        for step in technique["steps"]:
            st.write(step)

st.markdown("---")

st.subheader("💪 Progressive Muscle Relaxation")
st.write("Systematically tense and release muscle groups. 15-minute session.")

if st.button("▶️ Start PMR Session", use_container_width=True):
    progress = st.progress(0)
    status = st.empty()
    total = len(PROGRESSIVE_MUSCLE_RELAXATION)
    for i, item in enumerate(PROGRESSIVE_MUSCLE_RELAXATION):
        muscle = item[0]
        instruction = item[1]
        status.markdown("### " + muscle + "\n\n" + instruction)
        progress.progress(int((i + 1) / total * 100))
        time.sleep(8)
    progress.empty()
    status.empty()
    st.success("PMR complete! Feel the relaxation throughout your body. 🧘")
    add_meditation_session("PMR", 15)
