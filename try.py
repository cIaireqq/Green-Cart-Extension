# ReClaim 
import streamlit as st
st.set_page_config(layout="wide") 

#top banner
st.image("https://upload.wikimedia.org/wikipedia/commons/6/69/Potato-Chips.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original", use_container_width=True)

st.title("ReClaim")
st.caption("Check out how we grade: https://docs.google.com/document/d/1E9Cwvz3hkz6Ln80RBsq7MWUtxvZ3rgDkj11CJlBvvU4/edit?tab=t.0")
userChips = st.text_input(
    "Search or enter the name of a brand (Eg: 'Lays' instead of 'Lays Chips')"
)  


if st.button("Enter"):
  chips = ["Lays", "Ruffles", "Calbee", "Kettle", "Tyrells"]
  grade = [17, 40, 70, 86, 80]
  reason = [
      "Packaging uses too much plastic",
      "oil problems",
      "some problem but pretty good",
      "idk",
      "organic British crisps yum yum yum. Young lad you have very good taste in chips. You should get the sweet chili flavor"
  ]  

#banners and headers and stuff
 
st.markdown(
    "<h2 style='text-align: center; font-weight: 800; margin: 30px 0;'>AT RECLAIM, WE BELIEVE IN EATING WELL<br>WITHOUT SACRIFICING ENJOYMENT.</h2>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
with col1:
    st.image("img1.jpg", use_container_width=True)
with col2:
    st.image("img2.jpg", use_container_width=True)
with col3:
    st.image("img3.jpg", use_container_width=True)

    
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
