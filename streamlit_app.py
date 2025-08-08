import streamlit as st
from mood_utils import analyze_mood, log_entry, get_recommendation, plot_trends

st.title("🧠 Daily Mood Tracker")

text = st.text_area("How are you feeling today?")

if st.button("Analyze Mood"):
    sentiment, emotion = analyze_mood(text)
    log_entry(text, sentiment, emotion)
    st.success(f"**Sentiment:** {sentiment}")
    st.info(f"**Detected Emotion:** {emotion}")
    st.write(f"📝 **Advice:** {get_recommendation(emotion)}")

if st.button("Show Mood Trends"):
    plot_trends()
