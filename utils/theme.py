import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    [data-testid="stAppViewContainer"]{
        background: linear-gradient(
            90deg,
            #0f2138 0%,
            #162d4d 45%,
            #2b2b78 100%
        );
        background-attachment: fixed;
    }

    [data-testid="stSidebar"]{
        background: linear-gradient(
            180deg,
            #091426 0%,
            #0f2138 100%
        );
    }

    h1,h2,h3,h4,h5,h6,p,label,li,span{
        color:white !important;
    }

    .stMarkdown{
        color:white;
    }

    </style>
    """, unsafe_allow_html=True)