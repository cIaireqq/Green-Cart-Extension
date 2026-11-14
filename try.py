# ReClaim 
import streamlit as st

st.title("ReClaim")
user_text = st.text_area("Search or enter a brand")

if st.button("Enter"):
  # Put your team's Python code here
  answer = user_text.lower()
  st.write(answer)
