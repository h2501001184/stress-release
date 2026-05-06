"""
🧘 Stress Relief Hub — Complete Mental Wellness Application
A comprehensive Streamlit app for stress management, anxiety relief, and mental wellness.
"""

import streamlit as st
from utils.styles import load_css
from utils.data_manager import init_db, get_affirmation

st.set_page_config(
    page_title="Stress Relief Hub",
    page_icon="🧘",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_db()
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🧘 Stress Relief Hub")

# Daily affirmation banner
affirmation = get_affirmation()
st.markdown(f"""
<div style="background: linear-gradient(135deg, #667eea, #764ba2); 
            padding: 25px; border-radius: 15px; color: white; 
            text-align: center; margin-bottom: 30px;">
    <h2>✨ Welcome Back</h2>
    <p style="font-size: 20px; font-style: italic; margin-top: 10px;">{affirmation}</p>
    <p style="font-size: 14px; opacity: 0.8; margin-top: 15px;">
        Use the sidebar to navigate through your wellness toolkit.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h3>Your Wellness Toolkit Includes:</h3>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
features = [
    ("🚨", "SOS & Grounding", "Immediate panic relief and grounding techniques"),
    ("🫁", "Breathwork", "Guided breathing exercises with audio"),
    ("🧘", "Meditation", "Guided sessions for every situation"),
    ("🧠", "CBT Tools", "Worry time, thought reframing, brain dump"),
    ("🌙", "Sleep & Sound", "Sleep stories, binaural beats, soundscapes"),
    ("📊", "Mood Tracker", "Track patterns and triggers over time"),
    ("🤖", "AI Therapist", "24/7 CBT-based chat support"),
    ("🌱", "Zen Garden", "Gamified growth and achievements"),
    ("👥", "Community", "Anonymous peer support"),
]

for i, (emoji, title, desc) in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 12px; 
                    text-align: center; margin: 10px 0; border: 1px solid #e9ecef;">
            <div style="font-size: 40px; margin-bottom: 10px;">{emoji}</div>
            <h4>{title}</h4>
            <p style="font-size: 13px; color: #666;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.info("💙 All your data is stored locally on your device. Nothing leaves your computer.")
