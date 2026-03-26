import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_me(user_input: str, user_email: str | None = None) -> dict:
    prompt = f"User age: {user_email}. Question: {user_input}" if user_email else user_input

    try:
       
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt
        )
        return {"response": response.text}
    except Exception as e:
        print(f"DEBUG ERROR: {e}")
        return {"response": f"Помилка: {str(e)}"}