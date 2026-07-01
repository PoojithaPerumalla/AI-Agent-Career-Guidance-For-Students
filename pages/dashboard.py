import streamlit as st
import pandas as pd
from utils.theme import apply_theme

# -------------------------
# LOGIN PROTECTION
# -------------------------
if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
):
    st.warning("🔒 Please Login First")
    st.stop()

# -------------------------
# THEME
# -------------------------
apply_theme()

# -------------------------
# USER DATA
# -------------------------
if "user" not in st.session_state:
    st.error("User session not found")
    st.stop()

user = st.session_state.user

try:
    name = user[1]
    email = user[2]
    branch = user[4]
    year = user[5]
except:
    name = "Student"
    email = "Not Available"
    branch = "Not Available"
    year = "Not Available"

# -------------------------
# HEADER
# -------------------------
st.title("📊 CareerPilot AI Dashboard")

st.success(f"🚀 Welcome back, {name}!")

# -------------------------
# PROFILE SECTION
# -------------------------
st.subheader("👤 Student Profile")

col1, col2 = st.columns(2)

with col1:
    st.info(f"👤 Name: {name}")
    st.info(f"📧 Email: {email}")

with col2:
    st.info(f"🎓 Branch: {branch}")
    st.info(f"📚 Year: {year}")

st.divider()

# -------------------------
# SESSION DATA
# -------------------------
skills = st.session_state.get(
    "skills",
    "Not Available"
)

career = st.session_state.get(
    "career_recommendation",
    "Not Available"
)

score = st.session_state.get(
    "career_score",
    "Not Available"
)

goal = st.session_state.get(
    "goal",
    "Not Available"
)

# -------------------------
# SUMMARY
# -------------------------
st.subheader("📌 Student Summary")

col1, col2 = st.columns(2)

with col1:

    st.write("### 🧠 Skills")

    if skills != "Not Available":
        st.success(str(skills))
    else:
        st.warning("No skills available")

with col2:

    st.write("### 📚 Career Goal")

    if goal != "Not Available":
        st.success(str(goal))
    else:
        st.warning("Goal not available")

# -------------------------
# CAREER RECOMMENDATION
# -------------------------
st.write("### 🎯 Recommended Career")

if career != "Not Available":

    with st.expander(
        "View Recommendation"
    ):
        st.write(career)

else:
    st.warning(
        "Career Recommendation Not Available"
    )

# -------------------------
# CAREER SCORE
# -------------------------
st.write("### 🏆 Career Readiness Score")

if score != "Not Available":

    with st.expander(
        "View Score"
    ):
        st.write(score)

else:
    st.warning(
        "Career Score Not Available"
    )

st.divider()

# -------------------------
# PROGRESS OVERVIEW
# -------------------------
st.subheader("📈 Progress Overview")

# Skill Count
if isinstance(skills, str):

    if skills == "Not Available":
        skill_count = 0
    else:
        skill_count = len(
            [
                s.strip()
                for s in skills.split(",")
                if s.strip()
            ]
        )

elif isinstance(skills, list):
    skill_count = len(skills)

else:
    skill_count = 0

career_done = (
    100
    if career != "Not Available"
    else 0
)

score_done = (
    100
    if score != "Not Available"
    else 0
)

goal_done = (
    100
    if goal != "Not Available"
    else 0
)

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Skills Added",
        skill_count
    )

with col2:
    st.metric(
        "Career Analysis",
        f"{career_done}%"
    )

with col3:
    st.metric(
        "Career Score",
        f"{score_done}%"
    )

with col4:
    st.metric(
        "Goal Status",
        f"{goal_done}%"
    )

# -------------------------
# CHART
# -------------------------
chart_data = pd.DataFrame(
    {
        "Progress": [
            min(skill_count * 20, 100),
            career_done,
            score_done,
            goal_done
        ]
    },
    index=[
        "Skills",
        "Career",
        "Score",
        "Goal"
    ]
)

st.bar_chart(chart_data)

st.divider()

st.success(
    "✅ CareerPilot AI Dashboard Ready"
)