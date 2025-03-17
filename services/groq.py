import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

async def get_ai_response(query: str) -> str:
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": "llama3-8b-8192", "messages": [{"role": "user", "content": query}]}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(GROQ_API_URL, json=payload, headers=headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")
        except httpx.HTTPStatusError as e:
            return f"API Error: {e.response.status_code}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"
