import streamlit as st
from utils.styles import load_css
from utils.data_manager import add_community_post, get_community_posts
import hashlib
from datetime import datetime

st.set_page_config(page_title="Community", page_icon="👥", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("👥 Anonymous Peer Support")

st.markdown("""
<div style="background: #fff3cd; padding: 15px; border-radius: 10px; margin-bottom: 20px; color: #856404;">
    <p>⚠️ <strong>Community Guidelines:</strong> This is a safe space. Be kind. No medical advice. 
    No identifying information. If you're in crisis, use the Crisis Resources page.</p>
</div>
""", unsafe_allow_html=True)

# Post creation
st.subheader("📝 Share Your Thoughts")
category = st.selectbox("Category", [
    "General", "Anxiety", "Depression", "Stress", "Sleep", 
    "Relationships", "Work", "Healing", "Celebration", "Need Support"
])
content = st.text_area("Your message (completely anonymous):", 
                       placeholder="Share what's on your heart...", height=100)

if st.button("📤 Post Anonymously", use_container_width=True):
    if content:
        anon_id = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:6]
        add_community_post(anon_id, category, content)
        st.success("Posted! Your voice matters. 💙")
        st.balloons()
        st.rerun()
    else:
        st.warning("Please write something first.")

st.markdown("---")

# Filter posts
st.subheader("💬 Community Feed")
filter_cat = st.selectbox("Filter by category:", ["All"] + [
    "General", "Anxiety", "Depression", "Stress", "Sleep", 
    "Relationships", "Work", "Healing", "Celebration", "Need Support"
])

posts = get_community_posts()
filtered_posts = [p for p in posts if filter_cat == "All" or p[2] == filter_cat]

if filtered_posts:
    for post in filtered_posts[:30]:
        # Color code by category
        cat_colors = {
            "Need Support": "#ff6b6b",
            "Celebration": "#51cf66",
            "Anxiety": "#ffd43b",
            "Depression": "#74c0fc",
            "Stress": "#ff922b",
            "Sleep": "#845ef7",
            "Relationships": "#f06595",
            "Work": "#339af0",
            "Healing": "#20c997",
            "General": "#667eea",
        }
        color = cat_colors.get(post[2], "#667eea")

        st.markdown(f"""
        <div style="background: white; padding: 15px; border-radius: 10px; 
                    border-left: 5px solid {color}; margin: 10px 0;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <small>🏷️ <span style="color: {color}; font-weight: bold;">{post[2]}</span> 
                | 🕐 {post[5][:10]} | 👤 Anonymous-{post[1][:4]}</small>
            </div>
            <p style="margin-top: 10px; font-size: 16px; line-height: 1.6;">{post[3]}</p>
        </div>
        """, unsafe_allow_html=True)

        # Support reactions
        support_reactions = ["💙", "🤗", "💪", "🌸", "🕯️", "🫂", "✨", "🌈"]
        reaction_cols = st.columns(len(support_reactions))
        for i, reaction in enumerate(support_reactions):
            with reaction_cols[i]:
                if st.button(reaction, key=f"react_{post[0]}_{i}"):
                    st.toast(f"Sent {reaction} to Anonymous-{post[1][:4]}!")
else:
    st.info("No posts yet. Be the first to share! 💙")
