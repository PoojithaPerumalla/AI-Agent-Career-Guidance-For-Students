import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("💼 Internship Advisor")

skills = st.text_area("Enter Skills")

if st.button("Suggest Internships"):

    prompt = f"""
    Skills:
    {skills}

    Suggest:

    1. Suitable internships
    2. Required skills
    3. Preparation tips
    """

    result = get_gemini_response(prompt)

    st.write(result)