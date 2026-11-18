# ReClaim 
import streamlit as st  
from PIL import Image
import csv

img = Image.open("chip.jpg")
width, height = img.size

# Crop the image
crop_box = (0, int(height * 0.75), width, height)
banner_img = img.crop(crop_box)

st.image(banner_img, use_container_width=True)

# Title and grading stuff
st.title("ReClaim")
st.caption("Check out how we grade: https://docs.google.com/document/d/1E9Cwvz3hkz6Ln80RBsq7MWUtxvZ3rgDkj11CJlBvvU4/edit?tab=t.0")
userChips = st.text_input(
    "Search or enter the name of a brand (Eg: 'Lays' instead of 'Lays Chips')"
)  

st.caption("chips-1.csv");
f=open('chips-1.csv','r');
fc=f.readlines();
if f!=None: 
    st.caption('file exists!');
    for i in fc[:5]: st.caption(i);
# TRIAL TRIAL TRIAL 
with open("data.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    columns = [list(col) for col in zip(*reader)]

chips = ["Lays", "Ruffles", "Calbee", "Kettle", "Tyrells"]
grade = [17, 40, 70, 86, 80]
reason = [
    "Packaging uses too much plastic",
    "oil problems",
    "some problem but pretty good",
    "idk",
    "organic British crisps yum yum yum. Young lad you have very good taste in chips. You should get the sweet chili flavor"
]  

if st.button("Enter") or userChips.strip():
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
else:
    # Only shows when the user hasn't searched yet
    st.markdown(
        "<h2 style='text-align: center; font-weight: 800; margin: 30px 0;'>AT RECLAIM, WE BELIEVE IN EATING WELL<br>WITHOUT SACRIFICING ENJOYMENT.</h2>",
        unsafe_allow_html=True
    )
