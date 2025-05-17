import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_aws_command(natural_language_query):
    prompt = f"Convert this to an AWS CLI command: {natural_language_query}"
    response = model.generate_content(prompt)
    return response.text.strip()
