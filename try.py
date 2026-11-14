# ReClaim 
import streamlit as st

st.title("ReClaim")
user_Chips = st.text_area("Search or enter a brand")

if st.button("Enter"):
  # Put your team's Python code here
  chips = ["Lays", "Ruffles", "Calbee", "Kettle"]
  grade = [17, 40, 70, 86]
  reason = ["Packaging uses too much plastic", "oil problems", "some problem but pretty good", "idk"]
  for i in range(len(chips)):
   if userChips == chips[i]:
     print(chips[i] + " grade:", grade[i])
     print(reason[i])
  if userChips not in chips:
   print("We don't have that chips brand. Here are some sources that might: [some sources idk]")
