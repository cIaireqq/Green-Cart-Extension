# ReClaim 
import streamlit as st
st.title("ReClaim")
userChips = st.text_input(
    "Search or enter a brand"
)  

if st.button("Enter"):
  chips = ["Lays", "Ruffles", "Calbee", "Kettle"]
  grade = [17, 40, 70, 86]
  reason = [
      "Packaging uses too much plastic",
      "oil problems",
      "some problem but pretty good",
      "idk",
  ]  

  cleanInput = userChips.strip().lower()
    
  for i in range(len(chips)):
    if cleanInput == chips[i].lower():
      st.subheader(f"{chips[i]} — {grade[i]}/100")
      st.progress(grade[i] / 100)

      if grade[i] <= 25:
        st.error("Rating: Not Eco-Friendly")  
      elif grade[i] <= 50:
        st.warning("Rating: Moderate")  
      elif grade[i] <= 75:
        st.success("Rating: Eco-Friendly") 
      else:
        st.info("Rating: Top Pick")  

      st.markdown(f"{reason[i]}")
      break
  else:
    st.warning(
        "We don't have that chips brand. Try checking your spelling. "
        "If we still do not have it, here are some sources that might:"
        "[some sources idk]"
    )
