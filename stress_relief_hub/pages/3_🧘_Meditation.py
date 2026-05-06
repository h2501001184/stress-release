import streamlit as st
import time
from utils.styles import load_css
from utils.data_manager import add_meditation_session
from utils.cbt_tools import GUIDED_MEDITATIONS
from utils.audio_utils import generate_binaural_beat, audio_to_bytes, SAMPLE_RATE
import numpy as np

st.set_page_config(page_title="Guided Meditation", page_icon="🧘", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🧘 Guided Meditations")

st.markdown("""
<div style="background: #e7f3ff; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
    <p>🎧 Each session includes optional background binaural audio. Find a comfortable position and begin.</p>
</div>
""", unsafe_allow_html=True)

# Filter by duration
duration_filter = st.selectbox("Filter by duration:", ["All", "Under 10 min", "10-15 min", "15+ min"])

for med in GUIDED_MEDITATIONS:
    show = True
    if duration_filter == "Under 10 min" and med['duration'] >= 10:
        show = False
    elif duration_filter == "10-15 min" and (med['duration'] < 10 or med['duration'] > 15):
        show = False
    elif duration_filter == "15+ min" and med['duration'] < 15:
        show = False

    if not show:
        continue

    with st.expander(f"🧘 {med['title']} ({med['duration']} min)"):
        st.write(f"*{med['description']}*")

        # Show script preview
        with st.expander("📖 Preview Script"):
            for i, line in enumerate(med['script']):
                st.write(f"{i+1}. {line}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"▶️ Start Session", key=f"med_{med['title']}", use_container_width=True):
                progress_bar = st.progress(0)
                status = st.empty()
                total_seconds = med['duration'] * 60
                elapsed = 0

                for i, line in enumerate(med['script']):
                    status.markdown(f"### {line}")
                    step_time = total_seconds // len(med['script'])
                    for j in range(100):
                        time.sleep(step_time / 100)
                        elapsed += step_time / 100
                        progress_bar.progress(min(int(elapsed / total_seconds * 100), 100))

                progress_bar.empty()
                status.empty()
                add_meditation_session(med['title'], med['duration'])
                st.success(f"🎉 {med['duration']} minutes of mindfulness complete!")
                st.balloons()

        with col2:
            if st.button(f"🎵 Background Audio", key=f"med_audio_{med['title']}", use_container_width=True):
                # Generate appropriate binaural beat based on meditation type
                if 'sleep' in med['title'].lower() or 'relax' in med['title'].lower():
                    audio = generate_binaural_beat(100, 4, med['duration'] * 60, 0.15)  # Delta
                elif 'focus' in med['title'].lower() or 'work' in med['title'].lower():
                    audio = generate_binaural_beat(250, 12, med['duration'] * 60, 0.15)  # Low beta
                else:
                    audio = generate_binaural_beat(200, 8, med['duration'] * 60, 0.15)  # Alpha
                st.audio(audio_to_bytes(audio, SAMPLE_RATE), format='audio/wav')

st.markdown("---")
st.subheader("💡 Meditation Tips")
st.write("""
- **Find a quiet space** where you won't be interrupted
- **Set a gentle alarm** so you don't worry about time
- **It's okay if your mind wanders** — noticing and returning IS the practice
- **Start small** — even 2 minutes counts
- **Consistency beats duration** — 5 minutes daily beats 30 minutes once a week
""")
