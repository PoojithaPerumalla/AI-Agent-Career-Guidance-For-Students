import streamlit as st

# ---- Authentication ----
from utils.auth import login_user, register_user
from utils.database import create_users_table

create_users_table()

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.title("🚀 CareerPilot AI")
    st.subheader("AI Career Guidance Platform")

    login_tab, register_tab = st.tabs(["🔑 Login", "📝 Register"])

    # LOGIN
    with login_tab:

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            user = login_user(email, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.success("Login Successful")
                st.rerun()
            else:
                st.error("Invalid Email or Password")

    # REGISTER
    with register_tab:

        name = st.text_input("Full Name")
        reg_email = st.text_input("Email", key="reg_email")
        reg_password = st.text_input(
            "Password",
            type="password",
            key="reg_pass"
        )

        branch = st.selectbox(
            "Branch",
            ["CSE", "ECE", "EEE", "IT", "MECH", "CIVIL"]
        )

        year = st.selectbox(
            "Year",
            ["1st", "2nd", "3rd", "4th"]
        )

        if st.button("Register"):

            success = register_user(
                name,
                reg_email,
                reg_password,
                branch,
                year
            )

            if success:
                st.success("Registration Successful")
            else:
                st.error("Email already exists")

# ---------------- HOME PAGE ----------------
else:

    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"]{
        background: linear-gradient(
            90deg,
            #0f2138 0%,
            #162d4d 45%,
            #2b2b78 100%
        );
    }

    [data-testid="stHeader"]{
        background: rgba(0,0,0,0);
    }

    [data-testid="stSidebar"]{
        background: #111827;
    }

    h1,h2,h3,h4,h5,h6,p,li{
        color:white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.success(
        f"👋 Welcome {st.session_state.user[1]}"
    )

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        del st.session_state.user
        st.rerun()

    st.image("banner.png", width="stretch")

    st.title("🚀 CareerPilot AI")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🧠 Skill Analysis")

    with col2:
        st.success("🎯 Career Recommendation")

    with col3:
        st.success("💼 Internship Guidance")

    st.divider()

    st.subheader("✨ Key Features")

    st.markdown("""
    - 🧠 Skill Analyzer
    - 🎯 Career Recommender
    - 📚 Learning Path Generator
    - 💼 Internship Matcher
    - 📄 Resume Analyzer
    - 🎤 Interview Coach
    - 🤖 AI Career Chatbot
    - 📊 Career Dashboard
    - 📄 PDF Career Reports
    """)

    st.divider()

    st.caption(
        "Built with ❤️ using Streamlit, Gemini AI, Pandas and Python"
    )