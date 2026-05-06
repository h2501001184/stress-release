import streamlit as st
import random
from utils.styles import load_css
from utils.data_manager import (
    add_worry_entry, get_worry_entries, complete_worry_entry,
    add_thought_jar, get_thought_jar, delete_thought_jar,
    add_cbt_entry, get_cbt_entries, add_gratitude_entry, get_gratitude_entries
)
from utils.cbt_tools import COGNITIVE_DISTORTIONS, GRATITUDE_PROMPTS

st.set_page_config(page_title="CBT Tools", page_icon="🧠", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🧠 CBT Tools for Overthinking")

tab1, tab2, tab3, tab4 = st.tabs(["📝 Worry Time", "🔍 Thought Reframing", "🫙 Brain Dump", "🙏 Gratitude"])

with tab1:
    st.subheader("⏰ Worry Time Scheduler")
    st.write("Schedule your worrying for a specific time. Right now, you have permission to let it go.")

    worry = st.text_area("What's worrying you?", placeholder="Write it all out here...", height=100)
    scheduled_time = st.time_input("Schedule worry time for", value=__import__('datetime').datetime.strptime("19:00", "%H:%M").time())

    if st.button("📅 Schedule Worry", use_container_width=True):
        if worry:
            time_str = scheduled_time.strftime("%H:%M")
            add_worry_entry(worry, time_str)
            st.success(f"Worry scheduled for {time_str}. Let it go for now. 🕊️")
            st.balloons()
        else:
            st.warning("Please write down your worry first.")

    st.markdown("---")
    st.subheader("📋 Your Scheduled Worries")
    worries = get_worry_entries()
    if worries:
        for w in worries[:10]:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{w[1]}** (Scheduled: {w[2]})")
            with col2:
                badge_color = "🟢" if w[3] == 'completed' else "🟡"
                st.caption(f"{badge_color} {w[3]}")
            with col3:
                if w[3] == 'pending':
                    with st.popover("✅ Complete"):
                        reflection = st.text_area("Reflection:", key=f"ref_{w[0]}")
                        if st.button("Save", key=f"save_ref_{w[0]}"):
                            complete_worry_entry(w[0], reflection)
                            st.success("Marked complete!")
                            st.rerun()
    else:
        st.info("No worries scheduled. That's wonderful! 🌟")

with tab2:
    st.subheader("🔄 Cognitive Reframing Journal")
    st.write("Identify cognitive distortions and rewrite them into balanced thoughts.")

    situation = st.text_area("Describe the situation:", placeholder="What happened?")
    automatic_thought = st.text_area("What automatic thought came up?", placeholder="e.g., 'I'm going to fail everything'")

    distortion = st.selectbox("Identify the cognitive distortion:", list(COGNITIVE_DISTORTIONS.keys()))

    if distortion:
        info = COGNITIVE_DISTORTIONS[distortion]
        st.info(f"**{info['icon']} {distortion}**: {info['description']}")
        st.write(f"Example: *{info['example']}*")
        st.write(f"Reframe: *{info['reframe']}*")

    balanced_thought = st.text_area("Write a balanced, realistic thought:", placeholder="e.g., 'I've prepared well and will do my best'")

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        mood_before = st.slider("Mood before (1-10)", 1, 10, 3)
    with col_m2:
        mood_after = st.slider("Mood after reframing (1-10)", 1, 10, 6)

    if st.button("💾 Save Entry", use_container_width=True):
        if situation and automatic_thought and balanced_thought:
            add_cbt_entry(situation, automatic_thought, distortion, balanced_thought, mood_before, mood_after)
            st.success("Entry saved! You're building healthier thought patterns. 🌱")
            if mood_after > mood_before:
                st.balloons()
        else:
            st.warning("Please fill in all fields.")

    st.markdown("---")
    st.subheader("📖 Past Entries")
    entries = get_cbt_entries()
    if entries:
        for entry in entries[:5]:
            with st.expander(f"{entry[1][:50]}... ({entry[2]})"):
                st.write(f"**Situation:** {entry[1]}")
                st.write(f"**Automatic Thought:** {entry[3]}")
                st.write(f"**Distortion:** {entry[4]}")
                st.write(f"**Balanced Thought:** {entry[5]}")
                improvement = entry[7] - entry[6]
                emoji = "📈" if improvement > 0 else "📉" if improvement < 0 else "➡️"
                st.write(f"**Mood:** {entry[6]} → {entry[7]} {emoji} ({improvement:+d})")
    else:
        st.info("No entries yet. Start reframing! 🔄")

with tab3:
    st.subheader("🫙 Brain Dump / Thought Jar")
    st.write("Dump all your racing thoughts here. Get them out of your head.")

    thought = st.text_area("What's on your mind?", placeholder="No filters. No judgment. Just dump it all here...")
    category = st.selectbox("Category", ["General", "Work", "Relationships", "Health", "Future", "Random", "Anxiety", "Overthinking"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 Dump Thought", use_container_width=True):
            if thought:
                add_thought_jar(thought, category)
                st.success("Thought captured! It's out of your head now. 🗑️")
                st.rerun()
            else:
                st.warning("Write something first!")
    with col2:
        if st.button("🎲 Random Distraction", use_container_width=True):
            distractions = [
                "Name 10 animals alphabetically 🦓",
                "Count backwards from 100 by 7s 🔢",
                "Spell your full name backwards ✏️",
                "List 5 things that are blue around you 🔵",
                "Do 10 jumping jacks right now 🏃",
                "Hold your breath for 10 seconds 🫁",
                "Wiggle your toes and focus only on that sensation 🦶",
                "Name 5 countries starting with 'S' 🌍",
                "Recite the alphabet backwards 🔤",
                "Describe your room in extreme detail 🏠",
            ]
            st.info(random.choice(distractions))

    st.markdown("---")
    st.subheader("🗂️ Your Thought Jar")
    thoughts = get_thought_jar()
    if thoughts:
        for t in thoughts:
            col1, col2, col3 = st.columns([4, 1, 1])
            with col1:
                st.write(f"**{t[1]}** *({t[2]})*")
            with col2:
                st.caption(t[3][:10])
            with col3:
                if st.button("🗑️", key=f"del_thought_{t[0]}"):
                    delete_thought_jar(t[0])
                    st.rerun()
    else:
        st.info("Your jar is empty. That's okay too. 🫙")

with tab4:
    st.subheader("🙏 Gratitude Journal")
    st.write("What are you grateful for today?")

    prompt = random.choice(GRATITUDE_PROMPTS)
    st.info(f"💭 **Prompt:** {prompt}")

    gratitude = st.text_area("Your gratitude entry:", placeholder="I am grateful for...", height=100)

    if st.button("💾 Save Gratitude", use_container_width=True):
        if gratitude:
            add_gratitude_entry(gratitude)
            st.success("Gratitude saved! 💙")
            st.balloons()
            st.rerun()
        else:
            st.warning("Write something first!")

    st.markdown("---")
    st.subheader("📖 Your Gratitude Entries")
    entries = get_gratitude_entries(30)
    if entries:
        for date, entry in entries[:10]:
            st.markdown(f"**{date}**: {entry}")
    else:
        st.info("Start your gratitude practice! Even small things count. 🌱")
