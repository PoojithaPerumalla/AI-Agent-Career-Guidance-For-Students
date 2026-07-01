import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("📚 Learning Path Generator")

goal = st.text_input(
    "Enter Career Goal",
    placeholder="Data Scientist"
)

if st.button("Generate Roadmap"):
    st.session_state["goal"] = goal

    prompt = f"""
    Create a 3 month roadmap
    for becoming a {goal}.

    Include:

    Month 1
    Month 2
    Month 3

    Add skills and projects.
    """

    result = get_gemini_response(prompt)

    st.write(result)