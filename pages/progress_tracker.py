import streamlit as st
import pandas as pd
from utils.theme import apply_theme

apply_theme()
st.title("📈 Skills Progress Tracker")

data = pd.DataFrame({
    "Skill": [
        "Python",
        "SQL",
        "Machine Learning",
        "Communication"
    ],
    "Progress": [
        85,
        75,
        70,
        80
    ]
})

st.bar_chart(
    data.set_index("Skill")
)