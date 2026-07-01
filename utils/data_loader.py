import pandas as pd

def load_courses():
    return pd.read_csv("data/courses.csv")

def load_internships():
    return pd.read_csv("data/internships.csv")

def load_careers():
    return pd.read_csv("data/careers.csv")