import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("📊 Skill Gap Detector")

current_skills = st.text_area(
    "Enter Current Skills"
)

goal = st.text_input(
    "Target Career",
    placeholder="AI Engineer"
)

if st.button("Analyze Gap"):

    prompt = f"""
    Current Skills:
    {current_skills}

    Target Career:
    {goal}

    Give:

    1. Missing Skills
    2. Technologies to Learn
    3. 3 Month Roadmap
    """

    result = get_gemini_response(prompt)

    st.write(result)