# ReClaim 
import streamlit as st

st.title("My Hackathon Project")
user_text = st.text_area("Type here:")

if st.button("Run"):
  # Put your team's Python code here
  answer = user_text.upper()
  st.write(answer)
