import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="MindWell AI Prototype", page_icon="🧠", layout="centered")

st.title("🧠 MindWell AI - Prototype")
st.write("Your AI-powered mental health companion (MVP Version)")

# Session state for storing chat + moods
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "moods" not in st.session_state:
    st.session_state["moods"] = []

# Chat input
user_input = st.text_input("How are you feeling today?")

if user_input:
    # Sentiment analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    if sentiment > 0.2:
        mood = "😊 Positive"
        response = "I'm glad to hear that! Keep it up 🌟"
    elif sentiment < -0.2:
        mood = "😔 Negative"
        response = "I hear you. It’s okay to feel this way. Let’s try a breathing exercise 🧘"
    else:
        mood = "😐 Neutral"
        response = "Got it. How about sharing more about your day?"

    # Save chat + mood
    st.session_state["messages"].append(("You", user_input))
    st.session_state["messages"].append(("AI", response))
    st.session_state["moods"].append(mood)

# Display chat history
st.subheader("💬 Chat History")
for sender, msg in st.session_state["messages"]:
    st.write(f"**{sender}:** {msg}")

# Mood trend
if st.session_state["moods"]:
    st.subheader("📊 Mood Tracking")
    st.line_chart([1 if "Positive" in m else -1 if "Negative" in m else 0 for m in st.session_state["moods"]])
