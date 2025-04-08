import streamlit as st

st.title("Growth Mindset Challenge")
st.write("Welcome! Take on daily challenges to grow your mindset.")

challenge = st.text_input("Enter your today's challenge:")
if challenge:
    st.success(f"Great! You've committed to: {challenge}")
