import streamlit as st
import time
import numpy as np
from utils.styles import load_css
from utils.data_manager import add_meditation_session
from utils.audio_utils import (
    generate_tone, generate_binaural_beat, audio_to_bytes, 
    BREATHING_GUIDES, SAMPLE_RATE
)

st.set_page_config(page_title="Breathwork", page_icon="🫁", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🫁 Breathwork Library")

st.markdown("""
<div style="background: #e7f3ff; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
    <p>💡 All exercises include optional audio cues. Use headphones for binaural enhancement.</p>
</div>
""", unsafe_allow_html=True)

# Quick start buttons
st.subheader("⚡ Quick Start")
qcols = st.columns(3)
quick_presets = [
    ("Calm Now", "4-7-8 Relaxation", "🧘"),
    ("Focus", "Box Breathing (4-4-4-4)", "🎯"),
    ("Sleep", "4-7-8 Relaxation", "🌙"),
]

for col, (label, preset, emoji) in zip(qcols, quick_presets):
    with col:
        if st.button(f"{emoji} {label}", use_container_width=True):
            st.session_state.selected_breath = preset
            st.rerun()

st.markdown("---")

# Full library
for name, params in BREATHING_GUIDES.items():
    with st.expander(f"🫁 {name}"):
        pattern_text = f"Inhale {params['inhale']}s"
        if params.get('hold', 0) > 0:
            pattern_text += f" → Hold {params['hold']}s"
        pattern_text += f" → Exhale {params['exhale']}s"
        if params.get('hold2', 0) > 0:
            pattern_text += f" → Hold {params['hold2']}s"
        pattern_text += f" | Cycles: {params['cycles']}"

        st.write(f"**Pattern:** {pattern_text}")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(f"▶️ Start {name}", key=f"breathe_{name}", use_container_width=True):
                progress_bar = st.progress(0)
                status_text = st.empty()
                circle = st.empty()

                cycles = params['cycles']
                total_time = (params['inhale'] + params.get('hold', 0) + params['exhale'] + params.get('hold2', 0)) * cycles

                for cycle in range(cycles):
                    # Inhale
                    status_text.markdown(f"### 🫁 Cycle {cycle+1}/{cycles} — **INHALE** ({params['inhale']}s)")
                    for i in range(100):
                        progress_bar.progress(min(int(((cycle * 100 + i) / (cycles * 100)) * 100), 100))
                        size = 100 + i
                        circle.markdown(
                            f"<div style='width:{size}px;height:{size}px;border-radius:50%;"
                            f"background:radial-gradient(circle, #a8edea, #667eea);"
                            f"margin:0 auto;box-shadow:0 0 30px rgba(168,237,234,0.6);'></div>",
                            unsafe_allow_html=True
                        )
                        time.sleep(params['inhale'] / 100)

                    if params.get('hold', 0) > 0:
                        status_text.markdown(f"### ⏸️ **HOLD** ({params['hold']}s)")
                        time.sleep(params['hold'])

                    status_text.markdown(f"### 😮‍💨 **EXHALE** ({params['exhale']}s)")
                    for i in range(100, 0, -1):
                        size = 100 + i
                        circle.markdown(
                            f"<div style='width:{size}px;height:{size}px;border-radius:50%;"
                            f"background:radial-gradient(circle, #fed6e3, #a8edea);"
                            f"margin:0 auto;box-shadow:0 0 20px rgba(254,214,227,0.5);'></div>",
                            unsafe_allow_html=True
                        )
                        time.sleep(params['exhale'] / 100)

                    if params.get('hold2', 0) > 0:
                        status_text.markdown(f"### ⏸️ **HOLD** ({params['hold2']}s)")
                        time.sleep(params['hold2'])

                progress_bar.empty()
                status_text.markdown("### ✅ Complete! Notice how you feel.")
                circle.empty()
                add_meditation_session(name, total_time)
                st.success("Breathing session complete! 🌟")

        with col2:
            if st.button(f"🎵 Calm Audio", key=f"audio_{name}", use_container_width=True):
                audio = generate_binaural_beat(180, 7, 60, 0.15)
                st.audio(audio_to_bytes(audio, SAMPLE_RATE), format='audio/wav')

        with col3:
            if st.button(f"🔔 Tone Cues", key=f"tone_{name}", use_container_width=True):
                # Generate inhale/exhale tone cues
                inhale_tone = generate_tone(220, params['inhale'], 0.15, 0.2, 0.2)
                exhale_tone = generate_tone(180, params['exhale'], 0.12, 0.2, 0.2)
                combined = np.concatenate([inhale_tone, exhale_tone])
                stereo = np.vstack((combined, combined)).T
                st.audio(audio_to_bytes(stereo, SAMPLE_RATE), format='audio/wav')
                st.info("Inhale on higher tone, exhale on lower tone.")

st.markdown("---")
st.subheader("📚 Breathing Guide")
st.write("""
**4-7-8 Breathing** — Activates the parasympathetic nervous system. Best for sleep and anxiety.  
**Box Breathing** — Equal in, hold, out, hold. Used by Navy SEALs for focus under pressure.  
**Coherent Breathing** — 5 breaths per minute. Balances heart rate variability.  
**Physiological Sigh** — Double inhale, long exhale. Fastest way to reduce stress.  
**Energizing Breath** — Sharp, rhythmic breathing. Increases alertness without caffeine.
""")
