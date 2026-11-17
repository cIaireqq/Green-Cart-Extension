import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Hide the top header bar and remove all outer page padding */
    header[data-testid="stHeader"] {
        display: none;
    }
    [data-testid="stMainBlockContainer"] {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    /* Make the banner flush with no rounded corners */
    [data-testid="stImage"] img {
        border-radius: 0px !important;
    }
    /* Add side padding back to everything EXCEPT the first element (the banner) */
    [data-testid="stVerticalBlock"] > div:not(:first-child):not(:nth-child(2)) {
        padding-left: 4rem;
        padding-right: 4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Crop and display the full-bleed thin banner
img = Image.open("chip.jpg")
width, height = img.size
banner_img = img.crop((0, int(height * 0.75), width, height))
st.image(banner_img, use_container_width=True)

# Title and grading stuff
st.title("ReClaim")
st.caption("Check out how we grade: https://docs.google.com/document/d/1E9Cwvz3hkz6Ln80RBsq7MWUtxvZ3rgDkj11CJlBvvU4/edit?tab=t.0")

userChips = st.text_input(
    "Search or enter the name of a brand (Eg: 'Lays' instead of 'Lays Chips')"
)

chips = ["Lays", "Ruffles", "Calbee", "Kettle", "Tyrells"]
grade = [17, 40, 70, 86, 80]
reason = [
    "Packaging uses too much plastic",
    "oil problems",
    "some problem but pretty good",
    "idk",
    "organic British crisps yum yum yum. Young lad you have very good taste in chips. You should get the sweet chili flavor"
]

if st.button("Enter"):
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
            "If we still do not have it, here are some sources that might: "
            "[some sources idk]"
        )

st.markdown(
    "<h2 style='text-align: center; font-weight: 800; margin: 30px 0;'>AT RECLAIM, WE BELIEVE IN EATING WELL<br>WITHOUT SACRIFICING ENJOYMENT.</h2>",
    unsafe_allow_html=True
)
