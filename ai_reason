import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_reason(user, scheme_name):
    prompt = f"""
    User: {user}
    Why eligible for {scheme_name}?
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text
