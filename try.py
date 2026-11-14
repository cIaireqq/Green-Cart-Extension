# ReClaim 
import streamlit as st
st.title("ReClaim")
user_Chips = st.text_input(
    "Search or enter a brand"
)  # Changed to a sleeker single-line search bar!

if st.button("Enter"):
  chips = ["Lays", "Ruffles", "Calbee", "Kettle"]
  grade = [17, 40, 70, 86]
  reason = [
      "Packaging uses too much plastic",
      "oil problems",
      "some problem but pretty good",
      "idk",
  ]
  
  # .strip() removes accidental spaces if someone types "Lays "
  clean_input = user_Chips.strip()

  for i in range(len(chips)):
    if clean_input.lower() == chips[i].lower():  # Works even if they type "lays" in lowercase!
      st.subheader(f"{chips[i]} Grade: {grade[i]}/100")
      st.info(reason[i])
      break
  else:
    st.warning(
        "We don't have that chips brand. Here are some sources that might:"
        " [some sources idk]"
    )
