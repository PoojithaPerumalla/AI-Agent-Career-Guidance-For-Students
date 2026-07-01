import streamlit as st
from utils.data_loader import load_internships
from utils.theme import apply_theme

apply_theme()
st.title("💼 Internship Matcher")

skills = st.text_input(
    "Enter Skills",
    placeholder="Python SQL"
)

if st.button("Find Internships"):

    internships = load_internships()

    matched = []

    for _, row in internships.iterrows():

        required = row["Skills"].lower()

        user_skills = skills.lower()

        if any(skill in required for skill in user_skills.split()):

            matched.append(row)

    if matched:

        st.success("Matching Internships Found")

        for item in matched:

            st.write("###", item["Role"])
            st.write("Skills:", item["Skills"])
            st.write("Platform:", item["Platform"])

    else:

        st.warning("No matching internships found.")