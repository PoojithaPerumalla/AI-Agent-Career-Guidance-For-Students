import streamlit as st
from utils.data_loader import load_courses
from utils.theme import apply_theme

apply_theme()
st.title("📚 Course Recommender")

skill = st.text_input("Enter Skill")

if st.button("Recommend Courses"):

    courses = load_courses()

    result = courses[
        courses["Skill"].str.contains(skill, case=False)
    ]

    if not result.empty:
        st.dataframe(result)
    else:
        st.warning("No course found.")