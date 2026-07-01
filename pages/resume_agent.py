import streamlit as st
import PyPDF2
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    if st.button("Analyze Resume"):

        prompt = f"""
        Analyze this resume:

        {resume_text}

        Give:

        1. ATS Score out of 100
        2. Strengths
        3. Missing Skills
        4. Resume Improvements
        5. Suggested Career Roles
        """

        result = get_gemini_response(prompt)

        st.write(result)