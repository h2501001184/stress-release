import streamlit as st
import numpy as np
from utils.styles import load_css
from utils.data_manager import add_meditation_session
from utils.cbt_tools import SLEEP_STORIES, MORE_SLEEP_STORIES
from utils.audio_utils import (
    generate_binaural_beat, generate_sleep_story_bg, generate_brown_noise,
    generate_rain_sound, generate_ocean_waves, generate_white_noise,
    generate_pink_noise, audio_to_bytes, SAMPLE_RATE
)

st.set_page_config(page_title="Sleep & Sound", page_icon="🌙", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🌙 Sleep Stories & Soundscapes")

tab1, tab2, tab3 = st.tabs(["📖 Sleep Stories", "🎵 Soundscapes", "🔬 Binaural Beats"])

with tab1:
    st.subheader("📖 Bedtime Stories")
    all_stories = SLEEP_STORIES + MORE_SLEEP_STORIES

    for story in all_stories:
        with st.expander(f"📚 {story['title']} ({story['duration']})"):
            st.write(f"*{story['preview']}*")

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"▶️ Read Story", key=f"story_{story['title']}", use_container_width=True):
                    st.markdown(f"""
                    <div style="background: #1a1a2e; color: #e0e0e0; padding: 30px; 
                                border-radius: 15px; line-height: 2; font-size: 16px;">
                        {story['full_text'].replace(chr(10), '<br>')}
                    </div>
                    """, unsafe_allow_html=True)
            with col2:
                if st.button(f"🎵 Ambient Audio", key=f"story_audio_{story['title']}", use_container_width=True):
                    audio = generate_sleep_story_bg(120)
                    st.audio(audio_to_bytes(audio, SAMPLE_RATE), format='audio/wav')
            with col3:
                if st.button(f"🌙 Sleep Timer", key=f"timer_{story['title']}", use_container_width=True):
                    st.info("Set a timer below to auto-stop audio after you fall asleep.")

with tab2:
    st.subheader("🎵 Soundscapes")
    st.write("All sounds are procedurally generated in real-time. No external files needed.")

    sound_type = st.selectbox("Choose sound:", [
        "White Noise", "Brown Noise", "Pink Noise", 
        "Rain", "Ocean Waves", "Sleep Story Ambient"
    ])
    duration = st.slider("Duration (minutes)", 1, 60, 10)
    volume = st.slider("Volume", 0.05, 0.5, 0.15, 0.05)

    # Sound mixer
    st.subheader("🎛️ Sound Mixer (Beta)")
    mix_enabled = st.checkbox("Enable sound mixing")
    if mix_enabled:
        mix_col1, mix_col2 = st.columns(2)
        with mix_col1:
            mix_sound = st.selectbox("Mix with:", ["Rain", "Ocean Waves", "Brown Noise"], key="mix")
            mix_volume = st.slider("Mix volume", 0.05, 0.3, 0.1, 0.05, key="mix_vol")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Generate & Play", use_container_width=True):
            with st.spinner(f"Generating {sound_type}..."):
                duration_sec = duration * 60

                if sound_type == "White Noise":
                    audio = generate_white_noise(duration_sec, volume)
                elif sound_type == "Brown Noise":
                    audio = generate_brown_noise(duration_sec, volume)
                elif sound_type == "Pink Noise":
                    audio = generate_pink_noise(duration_sec, volume)
                elif sound_type == "Rain":
                    audio = generate_rain_sound(duration_sec, volume)
                elif sound_type == "Ocean Waves":
                    audio = generate_ocean_waves(duration_sec, volume)
                else:
                    audio = generate_sleep_story_bg(duration_sec, volume)

                # Mix if enabled
                if mix_enabled:
                    mix_sec = duration * 60
                    if mix_sound == "Rain":
                        mix_audio = generate_rain_sound(mix_sec, mix_volume)
                    elif mix_sound == "Ocean Waves":
                        mix_audio = generate_ocean_waves(mix_sec, mix_volume)
                    else:
                        mix_audio = generate_brown_noise(mix_sec, mix_volume)

                    # Ensure same length
                    min_len = min(len(audio), len(mix_audio))
                    audio = audio[:min_len] + mix_audio[:min_len]

                if len(audio.shape) == 1:
                    audio = np.vstack((audio, audio)).T

                st.session_state.generated_audio = audio_to_bytes(audio, SAMPLE_RATE)
                st.session_state.audio_type = sound_type

    if st.session_state.get('generated_audio') and st.session_state.get('audio_type'):
        st.audio(st.session_state.generated_audio, format='audio/wav')
        st.success(f"Playing {st.session_state.audio_type} for {duration} minutes 🎧")
        if st.button("⏹️ Stop & Clear"):
            st.session_state.generated_audio = None
            st.session_state.audio_type = None
            st.rerun()

    # Sleep timer
    st.markdown("---")
    st.subheader("⏰ Sleep Timer")
    timer_min = st.selectbox("Stop audio after:", [5, 10, 15, 20, 30, 45, 60, 90])
    st.write(f"Audio will fade out after {timer_min} minutes.")

with tab3:
    st.subheader("🔬 Binaural Beats Generator")
    st.write("""
    Binaural beats play slightly different frequencies in each ear. 
    Your brain perceives the difference as a "beat" that entrains your brainwaves.
    **Requires headphones for full effect.**
    """)

    preset = st.selectbox("Choose brainwave preset:", [
        "Delta (2.5 Hz) — Deep Sleep",
        "Theta (6 Hz) — Meditation & Creativity", 
        "Alpha (10 Hz) — Relaxation & Focus",
        "Alpha-Theta (7 Hz) — Deep Calm",
        "Low Beta (12 Hz) — Alert Focus",
        "Custom"
    ])

    if preset == "Custom":
        base_freq = st.slider("Base frequency (Hz)", 100, 400, 200)
        beat_freq = st.slider("Beat frequency (Hz)", 0.5, 30, 10.0, 0.5)
    else:
        presets = {
            "Delta (2.5 Hz) — Deep Sleep": (100, 2.5),
            "Theta (6 Hz) — Meditation & Creativity": (200, 6),
            "Alpha (10 Hz) — Relaxation & Focus": (250, 10),
            "Alpha-Theta (7 Hz) — Deep Calm": (180, 7),
            "Low Beta (12 Hz) — Alert Focus": (300, 12),
        }
        base_freq, beat_freq = presets[preset]
        st.write(f"Base: {base_freq} Hz | Beat: {beat_freq} Hz")

    bb_duration = st.slider("Duration (minutes)", 1, 60, 15)
    bb_volume = st.slider("Volume", 0.05, 0.5, 0.2, 0.05)

    if st.button("▶️ Generate Binaural Beat", use_container_width=True):
        with st.spinner("Generating binaural beat..."):
            audio = generate_binaural_beat(base_freq, beat_freq, bb_duration * 60, bb_volume)
            st.audio(audio_to_bytes(audio, SAMPLE_RATE), format='audio/wav')
            st.success(f"Playing {beat_freq} Hz binaural beat for {bb_duration} minutes 🎧")
            add_meditation_session(f"Binaural {beat_freq}Hz", bb_duration)

    st.markdown("---")
    st.subheader("🧠 Brainwave Guide")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        **Delta (0.5-4 Hz)**
        - Deep sleep, healing
        - Unconscious mind access
        - Physical regeneration

        **Theta (4-8 Hz)**
        - Deep meditation
        - Creativity, intuition
        - REM sleep, dreaming

        **Alpha (8-13 Hz)**
        - Relaxed awareness
        - Calm focus
        - Light meditation
        """)
    with col2:
        st.write("""
        **Beta (13-30 Hz)**
        - Active thinking
        - Problem solving
        - Avoid for sleep

        **Gamma (30-100 Hz)**
        - Peak concentration
        - Cognitive enhancement
        - Not for relaxation
        """)
