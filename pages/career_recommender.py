import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("🎯 Career Recommender")

skills = st.text_area(
    "Enter your skills",
    placeholder="Python, SQL, ML"
)

if st.button("Recommend Career"):

    prompt = f"""
    Based on these skills:

    {skills}

    Recommend:

    1. Best Career Role
    2. Why it suits the student
    3. Required skills
    4. Salary range
    5. Learning path
    """

    result = get_gemini_response(prompt)
    st.session_state["career_recommendation"] = result

    st.write(result)