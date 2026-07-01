import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("🏆 Career Readiness Score")

skills = st.text_area("Skills")

projects = st.number_input(
    "Number of Projects",
    min_value=0
)

if st.button("Calculate Score"):
    

    prompt = f"""
    Skills:
    {skills}

    Projects:
    {projects}

    Calculate:

    1. Career Readiness Score out of 100
    2. Technical Score
    3. Project Score
    4. Communication Score
    5. Improvement Suggestions
    """

    result = get_gemini_response(prompt)
    st.session_state["career_score"] = result

    st.write(result)