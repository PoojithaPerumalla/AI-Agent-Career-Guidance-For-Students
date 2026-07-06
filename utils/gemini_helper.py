import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
]

API_KEYS = [key for key in API_KEYS if key]


def get_gemini_response(prompt):
    last_error = None

    for api_key in API_KEYS:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")

            response = model.generate_content(prompt)

            if response.text:
                return response.text

        except Exception as e:
            last_error = str(e)

            # If quota/rate limit, try next key
            if "429" in last_error or "quota" in last_error.lower():
                continue

            # Small retry for temporary errors
            time.sleep(2)

    return f"Error: {last_error}"