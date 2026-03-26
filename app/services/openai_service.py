from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("CHAT_GPT_API_KEY")

client = OpenAI(api_key=api_key)

def ask_chatgpt(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": prompt}]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"response": f"OpenAI Error: {str(e)}"}
