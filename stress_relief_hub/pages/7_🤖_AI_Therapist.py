import streamlit as st
import random
import os
from utils.styles import load_css
from utils.data_manager import add_chat_message, get_chat_history, clear_chat_history
from utils.cbt_tools import POSITIVE_AFFIRMATIONS

st.set_page_config(page_title="AI Therapist", page_icon="🤖", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🤖 AI Virtual Therapist")

st.markdown("""
<div style="background: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
    <p>💬 I'm an AI companion using CBT principles. Not a replacement for a licensed therapist, 
    but here 24/7 to help you process thoughts and feelings.</p>
    <p><small>All conversations are stored locally on your device only.</small></p>
</div>
""", unsafe_allow_html=True)

# OpenAI integration option
openai_key = os.getenv("OPENAI_API_KEY", "")
use_openai = False
if openai_key:
    use_openai = st.checkbox("Use OpenAI GPT for enhanced responses (requires API key)", value=False)
    if use_openai:
        try:
            import openai
            openai.api_key = openai_key
        except:
            st.warning("OpenAI package not installed. Using built-in therapist.")
            use_openai = False

def ai_therapist_response(user_message):
    if use_openai and openai_key:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a supportive CBT-based therapist. Be empathetic, use evidence-based techniques, validate feelings, and suggest specific coping strategies. Keep responses concise (2-3 paragraphs max). If the user is in crisis, direct them to emergency resources."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI error: {e}. Falling back to built-in therapist.\n\n" + rule_based_response(user_message)
    else:
        return rule_based_response(user_message)

def rule_based_response(user_message):
    msg_lower = user_message.lower()
    responses = {
        "anxious": "I hear that you're feeling anxious. Anxiety often tricks us into believing worst-case scenarios. Let's try grounding: name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste. What triggered this?",
        "worried": "Worry is like a rocking chair — it gives you something to do but gets you nowhere. Try the 'Worry Time' technique: write it down and schedule 15 minutes later to think about it. Right now, let it go.",
        "sad": "I'm sorry you're feeling sad. Sadness is valid, not something to fix immediately. Can you tell me more? Naming feelings helps them feel manageable.",
        "stressed": "Stress comes from feeling overwhelmed. What's ONE small thing you can do in 10 minutes? Tiny action relieves pressure.",
        "angry": "Anger often masks hurt or fear. Try the physiological sigh: two quick inhales through nose, long slow exhale through mouth. Repeat 3 times.",
        "tired": "Being tired makes everything harder. Have you rested? The most productive thing is sometimes allowing yourself to pause.",
        "lonely": "Loneliness is painful and brave to share. Is there someone you could text? Connection starts with a small step.",
        "panic": "You're having a panic attack. You are SAFE. Your body has a false alarm. Breathe: in 4, hold 4, out 6. Feel your feet. This WILL pass.",
        "sleep": "Sleep troubles are frustrating. Try tensing and releasing each muscle group from toes up. Also 4-7-8 breathing helps.",
        "overwhelmed": "Shrink your world to the next breath, then the next step. You don't have to solve everything now.",
        "grateful": "Gratitude is powerful. What's one small thing you appreciate right now? Even tiny moments count.",
        "happy": "That's wonderful! Savor it. Positive emotions deserve attention too. What contributed to this feeling?",
        "depressed": "I'm really sorry you're feeling this way. Depression lies to us about our worth. Can you do one tiny self-care act today — even brushing your teeth or opening a window? You matter.",
        "hopeless": "Hopelessness is a symptom, not a truth. You've felt differently before, and you can again. What's one thing that has helped in the past?",
        "self-harm": "I'm concerned about you. Please reach out to a crisis line: 988 or text HOME to 741741. You don't have to go through this alone. Your life matters.",
        "suicide": "Please call 988 right now. You are not alone. People care about you. This pain is temporary, even if it doesn't feel that way. Help is available 24/7.",
    }
    for keyword, response in responses.items():
        if keyword in msg_lower:
            return response
    defaults = [
        "Thank you for sharing. What thoughts are going through your mind? In CBT, thoughts shape feelings more than situations.",
        "I appreciate you opening up. What would you like to focus on — a thought, feeling, or situation?",
        "That sounds difficult. Remember: feelings are temporary visitors. What evidence supports your thought? What contradicts it?",
        "I'm here with you. Let's breathe together: inhale 4... hold 4... exhale 6. Our nervous system needs a reset.",
        "You matter, and your struggles are valid. You've survived difficult moments before. What helped then?",
    ]
    return random.choice(defaults)

# Chat interface
st.subheader("💬 Conversation")

# Load chat history
history = get_chat_history(50)
chat_container = st.container()
with chat_container:
    for role, content in history:
        if role == "user":
            st.markdown(f"<div style='text-align: right;'><div style='background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 10px 15px; border-radius: 15px 15px 5px 15px; display: inline-block; max-width: 80%; margin: 5px 0;'>{content}</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background: #f0f2f6; color: #333; padding: 10px 15px; border-radius: 15px 15px 15px 5px; display: inline-block; max-width: 80%; margin: 5px 0;'>{content}</div>", unsafe_allow_html=True)

user_input = st.chat_input("How are you feeling right now?")

if user_input:
    add_chat_message("user", user_input)
    response = ai_therapist_response(user_input)
    add_chat_message("assistant", response)
    st.rerun()

st.markdown("---")

# Conversation starters
st.subheader("💡 Conversation Starters")
starters = [
    "I'm feeling anxious about tomorrow",
    "I can't stop overthinking",
    "I had a panic attack today",
    "I'm having trouble sleeping",
    "I feel overwhelmed by everything",
    "I need help reframing a negative thought",
    "I'm feeling really down today",
    "I want to practice gratitude",
]

cols = st.columns(4)
for i, starter in enumerate(starters):
    with cols[i % 4]:
        if st.button(starter, key=f"starter_{i}", use_container_width=True):
            add_chat_message("user", starter)
            response = ai_therapist_response(starter)
            add_chat_message("assistant", response)
            st.rerun()

st.markdown("---")

# Tools section
st.subheader("🛠️ Quick Tools")
tool_col1, tool_col2, tool_col3 = st.columns(3)
with tool_col1:
    if st.button("🎲 Random Affirmation", use_container_width=True):
        aff = random.choice(POSITIVE_AFFIRMATIONS)
        st.info(aff)
with tool_col2:
    if st.button("🧠 CBT Thought Record", use_container_width=True):
        st.info("Go to CBT Tools → Thought Reframing to work through a specific thought.")
with tool_col3:
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        clear_chat_history()
        st.success("Chat history cleared.")
        st.rerun()
