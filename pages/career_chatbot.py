import streamlit as st
from utils.gemini_helper import get_gemini_response
from utils.theme import apply_theme

apply_theme()
st.title("🤖 CareerPilot AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask your career question...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    prompt = f"""
    You are an expert Career Guidance AI.

    Student Question:
    {user_input}

    Give practical and beginner-friendly guidance.
    """

    response = get_gemini_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)