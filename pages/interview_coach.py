import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("🎤 Interview Coach")

role = st.selectbox(
    "Select Role",
    [
        "Data Analyst",
        "Data Scientist",
        "AI Engineer",
        "ML Engineer",
        "Python Developer"
    ]
)

if st.button("Generate Question"):

    prompt = f"""
    Generate one interview question
    for a {role}.
    """

    question = get_gemini_response(prompt)

    st.session_state["question"] = question

if "question" in st.session_state:

    st.subheader("Question")

    st.write(st.session_state["question"])

    answer = st.text_area("Your Answer")

    if st.button("Evaluate Answer"):

        prompt = f"""
        Role: {role}

        Question:
        {st.session_state["question"]}

        Candidate Answer:
        {answer}

        Evaluate:

        1. Score out of 10
        2. Strengths
        3. Weaknesses
        4. Better Answer
        """

        feedback = get_gemini_response(prompt)

        st.write(feedback)