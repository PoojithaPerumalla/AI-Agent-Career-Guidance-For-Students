import streamlit as st
from utils.pdf_generator import generate_report
from utils.theme import apply_theme

apply_theme()
st.title("📄 Career Report Generator")

skills = st.session_state.get("skills", "")
career = st.session_state.get("career_recommendation", "")
score = st.session_state.get("career_score", "")
goal = st.session_state.get("goal", "")

if st.button("Generate PDF Report"):

    filename = "career_report.pdf"

    generate_report(
        filename,
        skills,
        career,
        score,
        goal
    )

    with open(filename, "rb") as file:

        st.download_button(
            label="📥 Download Report",
            data=file,
            file_name="CareerPilot_Report.pdf",
            mime="application/pdf"
        )