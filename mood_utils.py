import pandas as pd
import datetime
import os
import matplotlib.pyplot as plt
from transformers import pipeline
import streamlit as st

DATA_FILE = "mood_log.csv"

sentiment_classifier = pipeline("sentiment-analysis")
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def analyze_mood(text):
    sentiment = sentiment_classifier(text)[0]['label']
    emotion = emotion_classifier(text)[0]['label']
    return sentiment, emotion

def log_entry(text, sentiment, emotion):
    now = datetime.datetime.now()
    row = [[now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), text, sentiment, emotion]]
    df = pd.DataFrame(row, columns=["Date", "Time", "Text", "Sentiment", "Emotion"])
    if not os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, index=False)
    else:
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)

def get_recommendation(emotion):
    advice_map = {
        "anger": "Take deep breaths and try journaling.",
        "sadness": "Maybe try talking to a friend or meditating.",
        "joy": "Keep doing what brings you happiness!",
        "fear": "Practice grounding techniques like mindfulness.",
        "neutral": "Stay consistent and check in with yourself."
    }
    return advice_map.get(emotion, "Take care!")

def plot_trends():
    if not os.path.exists(DATA_FILE):
        st.warning("No mood data available yet.")
        return
    df = pd.read_csv(DATA_FILE)
    st.line_chart(df['Emotion'].value_counts())
