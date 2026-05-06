import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from utils.styles import load_css
from utils.data_manager import get_mood_history, add_mood_checkin

st.set_page_config(page_title="Mood Tracker", page_icon="📊", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

st.title("📊 Mood Tracker & Insights")

# Quick check-in at top
st.subheader("📍 Quick Mood Check-In")
mood = st.select_slider(
    "How are you feeling right now?",
    options=["😢 Very Low", "😕 Low", "😐 Okay", "🙂 Good", "😊 Great"],
    value="😐 Okay"
)
col_m1, col_m2 = st.columns(2)
with col_m1:
    trigger = st.text_input("What's contributing? (optional)")
with col_m2:
    notes = st.text_area("Notes (optional)", height=68)

if st.button("💾 Log Mood", use_container_width=True):
    mood_map = {"😢 Very Low": 1, "😕 Low": 2, "😐 Okay": 3, "🙂 Good": 4, "😊 Great": 5}
    add_mood_checkin(mood, mood_map[mood], trigger, notes)
    st.success("Mood logged! 🌱")
    st.balloons()
    st.rerun()

st.markdown("---")

mood_data = get_mood_history(30)

if mood_data:
    df = pd.DataFrame(mood_data, columns=["Date", "Mood", "Intensity", "Trigger"])
    df['Date'] = pd.to_datetime(df['Date'])

    # Summary stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        avg_mood = df['Intensity'].mean()
        st.metric("📊 Avg Mood", f"{avg_mood:.1f}/5")
    with col2:
        total_entries = len(df)
        st.metric("📝 Total Entries", total_entries)
    with col3:
        best_day = df.loc[df['Intensity'].idxmax(), 'Date'].strftime('%b %d')
        st.metric("😊 Best Day", best_day)
    with col4:
        streak = 0
        dates = sorted(df['Date'].dt.date.unique(), reverse=True)
        for i, d in enumerate(dates):
            expected = (datetime.now().date() - timedelta(days=i))
            if d == expected:
                streak += 1
            else:
                break
        st.metric("🔥 Check-in Streak", f"{streak} days")

    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 Mood Over Time")
        fig = px.line(df, x='Date', y='Intensity', color='Mood', markers=True,
                     title='Daily Mood Intensity',
                     labels={'Intensity': 'Level (1-5)'},
                     height=350)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🎯 Mood Distribution")
        mood_counts = df['Mood'].value_counts()
        fig2 = px.pie(values=mood_counts.values, names=mood_counts.index,
                     title='Mood Distribution', hole=0.4,
                     color_discrete_sequence=px.colors.sequential.Plasma)
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🔍 Trigger Analysis")
    trigger_df = df[df['Trigger'].notna() & (df['Trigger'] != '')]
    if not trigger_df.empty:
        trigger_counts = trigger_df['Trigger'].value_counts().head(10)
        fig3 = px.bar(x=trigger_counts.index, y=trigger_counts.values,
                     title='Top Triggers',
                     labels={'x': 'Trigger', 'y': 'Frequency'},
                     color=trigger_counts.values,
                     color_continuous_scale='Viridis')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("Add triggers to your mood entries to see pattern analysis.")

    # Weekly pattern
    st.subheader("📅 Weekly Pattern")
    df['DayOfWeek'] = df['Date'].dt.day_name()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekly = df.groupby('DayOfWeek')['Intensity'].mean().reindex(day_order)
    fig4 = px.bar(x=weekly.index, y=weekly.values,
                 title='Average Mood by Day of Week',
                 labels={'x': 'Day', 'y': 'Avg Mood'},
                 color=weekly.values,
                 color_continuous_scale='RdYlGn')
    st.plotly_chart(fig4, use_container_width=True)

    # Heatmap
    st.subheader("🗓️ Mood Calendar Heatmap")
    df['Week'] = df['Date'].dt.isocalendar().week
    df['DayNum'] = df['Date'].dt.dayofweek
    pivot = df.pivot_table(values='Intensity', index='DayNum', columns='Week', aggfunc='mean')
    fig5 = px.imshow(pivot, 
                     labels=dict(x="Week", y="Day", color="Mood"),
                     y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                     color_continuous_scale='RdYlGn',
                     aspect='auto')
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("📋 Recent Entries")
    st.dataframe(df.tail(10)[['Date', 'Mood', 'Intensity', 'Trigger', 'Notes']], use_container_width=True)

    # Export
    st.markdown("---")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Mood Data (CSV)",
        data=csv,
        file_name='mood_data.csv',
        mime='text/csv',
        use_container_width=True
    )
else:
    st.info("No mood data yet. Start checking in daily to see your patterns! 📊")

    st.subheader("📊 Preview (Demo Data)")
    demo_dates = pd.date_range(end=datetime.now(), periods=14)
    demo_df = pd.DataFrame({
        'Date': demo_dates,
        'Intensity': [3, 4, 2, 3, 5, 4, 3, 2, 4, 5, 3, 4, 4, 5],
        'Mood': ['Okay', 'Good', 'Low', 'Okay', 'Great', 'Good', 'Okay', 
                'Low', 'Good', 'Great', 'Okay', 'Good', 'Good', 'Great']
    })
    fig = px.line(demo_df, x='Date', y='Intensity', color='Mood', markers=True,
                 title='Your trends will look like this',
                 labels={'Intensity': 'Mood Level (1-5)'})
    st.plotly_chart(fig, use_container_width=True)
