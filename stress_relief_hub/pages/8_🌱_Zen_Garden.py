import streamlit as st
from utils.styles import load_css
from utils.data_manager import get_meditation_stats, get_garden_level

st.set_page_config(page_title="Zen Garden", page_icon="🌱", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🌱 Your Zen Garden")

stats = get_meditation_stats()
level = get_garden_level()
minutes = stats[0]

# Garden definitions with more visual detail
garden_levels = {
    1: {
        "name": "🌱 Seedling",
        "plants": ["🌱"],
        "ground": "🟫",
        "sky": "☁️",
        "desc": "Every great garden starts with a single seed. Keep nurturing your practice.",
        "color": "#8B7355"
    },
    2: {
        "name": "🌿 Sprout",
        "plants": ["🌱", "🌿", "🌱"],
        "ground": "🟫🟫",
        "sky": "☁️ ☁️",
        "desc": "Your consistency is showing! New growth emerges from daily care.",
        "color": "#7CB342"
    },
    3: {
        "name": "🌸 Blooming",
        "plants": ["🌱", "🌿", "🌸", "🌺", "🌿"],
        "ground": "🟫🟫🟫",
        "sky": "🌤️",
        "desc": "Beautiful! Your garden is coming to life with color and fragrance.",
        "color": "#E91E63"
    },
    4: {
        "name": "🌲 Flourishing",
        "plants": ["🌲", "🌸", "🌺", "🌻", "🦋", "🌿"],
        "ground": "🟫🟫🟫🟫",
        "sky": "☀️",
        "desc": "A thriving sanctuary of calm. Birds and butterflies visit your garden.",
        "color": "#4CAF50"
    },
    5: {
        "name": "🦚 Zen Paradise",
        "plants": ["🌲", "🌸", "🌺", "🌻", "🦋", "🦚", "🌈", "💎"],
        "ground": "🟫🟫🟫🟫🟫",
        "sky": "🌈",
        "desc": "Master of mindfulness. Your garden reflects the peace you've cultivated within.",
        "color": "#9C27B0"
    },
}

garden = garden_levels.get(level, garden_levels[1])

# Visual garden display
st.markdown(f"""
<div style="text-align: center; padding: 40px; 
            background: linear-gradient(180deg, #87CEEB 0%, #98FB98 60%, #8B7355 100%); 
            border-radius: 20px; margin-bottom: 20px; position: relative;">
    <div style="font-size: 30px; margin-bottom: 10px;">{garden['sky']}</div>
    <h2 style="color: #2d3748; text-shadow: 1px 1px 2px white;">{garden['name']} Garden</h2>
    <p style="font-size: 18px; color: #2d3748; text-shadow: 1px 1px 2px white;">{garden['desc']}</p>
    <div style="font-size: 50px; padding: 20px; letter-spacing: 10px;">
        {' '.join(garden['plants'] * 2)}
    </div>
    <div style="font-size: 25px; margin-top: 10px;">{garden['ground']}</div>
</div>
""", unsafe_allow_html=True)

# Stats row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🌱 Garden Level", garden['name'])
with col2:
    st.metric("⏱️ Mindful Minutes", minutes)
with col3:
    st.metric("🧘 Total Sessions", stats[1])
with col4:
    if level < 5:
        thresholds = {2: 30, 3: 120, 4: 300, 5: 600}
        needed = thresholds.get(min(level + 1, 5), 600) - minutes
        st.metric("📈 To Next Level", f"{needed} min")
    else:
        st.metric("🏆 Status", "Zen Master!")

st.markdown("---")

# Progress to next level
if level < 5:
    thresholds = {1: 0, 2: 30, 3: 120, 4: 300, 5: 600}
    current_threshold = thresholds[level]
    next_threshold = thresholds[level + 1]
    progress = (minutes - current_threshold) / (next_threshold - current_threshold)
    st.progress(min(progress, 1.0))
    st.caption(f"Progress to next level: {minutes}/{next_threshold} minutes")

st.markdown("---")
st.subheader("🏅 Achievements")

achievements = [
    ("🌱 First Step", "Complete your first meditation", stats[1] >= 1, "Begin your journey"),
    ("🔥 3-Day Streak", "Check in for 3 days straight", stats[2] >= 3, "Building momentum"),
    ("🔥🔥 7-Day Streak", "One week of consistency!", stats[2] >= 7, "Habit forming"),
    ("🔥🔥🔥 14-Day Streak", "Two weeks strong", stats[2] >= 14, "Unstoppable"),
    ("🔥🔥🔥🔥 30-Day Streak", "A full month!", stats[2] >= 30, "Legendary"),
    ("⏱️ 30 Minutes", "Accumulate 30 mindful minutes", minutes >= 30, "Getting started"),
    ("⏱️⏱️ 2 Hours", "Accumulate 120 mindful minutes", minutes >= 120, "Deepening practice"),
    ("⏱️⏱️⏱️ 5 Hours", "Accumulate 300 mindful minutes", minutes >= 300, "Dedicated practitioner"),
    ("⏱️⏱️⏱️⏱️ 10 Hours", "Accumulate 600 mindful minutes", minutes >= 600, "Zen Master"),
    ("🧘 10 Sessions", "Complete 10 meditation sessions", stats[1] >= 10, "Regular practitioner"),
    ("🧘🧘 50 Sessions", "Complete 50 sessions", stats[1] >= 50, "Devoted"),
    ("🌸 Bloom", "Reach Garden Level 3", level >= 3, "Flowering"),
    ("🌲 Wise Oak", "Reach Garden Level 4", level >= 4, "Ancient wisdom"),
    ("🦚 Zen Paradise", "Reach Garden Level 5", level >= 5, "Enlightenment"),
]

for name, desc, unlocked, subtitle in achievements:
    if unlocked:
        st.success(f"**{name}** — {desc} ✅ *({subtitle})*")
    else:
        st.markdown(f"<div style='opacity: 0.4; padding: 5px;'>**{name}** — {desc} 🔒 <br><small>{subtitle}</small></div>", unsafe_allow_html=True)

st.markdown("---")
st.info("💡 Tip: Every minute of mindfulness, every mood check-in, and every breathing session counts toward your garden's growth!")
