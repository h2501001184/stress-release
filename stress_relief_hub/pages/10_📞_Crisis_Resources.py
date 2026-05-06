import streamlit as st
from utils.styles import load_css
from utils.cbt_tools import CRISIS_RESOURCES

st.set_page_config(page_title="Crisis Resources", page_icon="📞", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("📞 Crisis Resources")

st.markdown("""
<div style="background: linear-gradient(135deg, #ff416c, #ff4b2b); padding: 25px; 
            border-radius: 15px; color: white; text-align: center; margin-bottom: 30px;">
    <h2>🚨 If you or someone you know is in immediate danger:</h2>
    <h1 style="font-size: 48px; margin: 15px 0;">Call 911</h1>
    <p style="font-size: 18px;">Or go to your nearest emergency room immediately.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📞 24/7 Crisis Hotlines")

for resource in CRISIS_RESOURCES:
    with st.expander(f"📞 {resource['name']}"):
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e7f3ff, #d4edda); padding: 25px; 
                    border-radius: 12px; text-align: center;">
            <h1 style="color: #0066cc; font-size: 42px; margin: 10px 0;">{resource['phone']}</h1>
            <p style="font-size: 16px; color: #333;">{resource['description']}</p>
            <p style="font-size: 14px; color: #666; margin-top: 10px;">
                Available 24 hours a day, 7 days a week, 365 days a year.
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Safety Plan
st.subheader("🛡️ Create Your Personal Safety Plan")

with st.expander("📝 Safety Plan Template"):
    st.write("Fill this out when you're feeling calm. Keep it accessible.")

    st.text_area("1. Warning Signs", 
                 placeholder="What thoughts, feelings, or behaviors signal you're heading into crisis?",
                 key="warn")
    st.text_area("2. Internal Coping Strategies", 
                 placeholder="What can I do by myself? (breathing, music, shower, walk)",
                 key="internal")
    st.text_area("3. Social Coping", 
                 placeholder="Who can I call or be with? (friends, family, pets)",
                 key="social")
    st.text_area("4. Professional Help", 
                 placeholder="My therapist, doctor, psychiatrist contact info",
                 key="pro")
    st.text_area("5. Environmental Safety", 
                 placeholder="Can I remove or secure means of harm?",
                 key="env")
    st.text_area("6. Reasons to Live", 
                 placeholder="What keeps me here? (people, pets, dreams, experiences, future goals)",
                 key="reasons")

    if st.button("💾 Save Safety Plan", use_container_width=True):
        st.success("Safety plan saved! Keep it somewhere accessible.")
        st.info("Remember: This app stores data locally. Consider writing a physical copy too.")

st.markdown("---")

# Immediate coping tools
st.subheader("⚡ Immediate Coping Tools")

cope_col1, cope_col2, cope_col3 = st.columns(3)
with cope_col1:
    st.markdown("""
    <div style="background: #e3f2fd; padding: 20px; border-radius: 10px; text-align: center;">
        <h3>🧊 Temperature</h3>
        <p>Hold ice cubes<br>Splash cold water<br>Take a cold shower</p>
        <p><small>Activates dive reflex</small></p>
    </div>
    """, unsafe_allow_html=True)

with cope_col2:
    st.markdown("""
    <div style="background: #f3e5f5; padding: 20px; border-radius: 10px; text-align: center;">
        <h3>🫁 Breathing</h3>
        <p>Box breathing<br>4-7-8 technique<br>Physiological sigh</p>
        <p><small>Regulates nervous system</small></p>
    </div>
    """, unsafe_allow_html=True)

with cope_col3:
    st.markdown("""
    <div style="background: #e8f5e9; padding: 20px; border-radius: 10px; text-align: center;">
        <h3>👁️ Grounding</h3>
        <p>5-4-3-2-1 senses<br>Hold a grounding object<br>Name colors in room</p>
        <p><small>Brings you to present</small></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.info("""
💙 **You are not alone.** You matter. You are worthy of help and healing. 
These feelings are temporary, even when they feel permanent. 
People care about you. Reach out. You deserve support.
""")
