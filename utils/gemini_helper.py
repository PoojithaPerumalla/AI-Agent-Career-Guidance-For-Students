import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.theme import apply_theme

apply_theme()

# Load environment variables
load_dotenv()

# Read API Key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"