import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

client = Groq(api_key=GROQ_API_KEY)

def get_ai_response(user_query):

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are LIKKI, a friendly, human-like personal AI assistant. Respond conversationally and politely."
                },
                {"role": "user", "content": user_query}
            ],
            temperature=0.6,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI ERROR:", e)
        return "Sorry, I am having trouble connecting right now."

