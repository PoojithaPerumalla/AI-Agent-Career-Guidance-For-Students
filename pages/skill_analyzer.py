import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("🧠 Skill Analyzer")

skills = st.text_area(
    "Enter your skills",
    placeholder="Python, SQL, Machine Learning, Communication"
)

if st.button("Analyze Skills"):
    st.session_state["skills"] = skills

    prompt = f"""
    Analyze these student skills:

    {skills}

    Give:
    1. Strengths
    2. Weaknesses
    3. Improvement Suggestions
    """

    result = get_gemini_response(prompt)

    st.write(result)