from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from schemas import ChatRequest
from services.groq import get_ai_response

router = APIRouter()

@router.post("/chat", summary="Chat with GroqAI", response_class=PlainTextResponse)
async def chat(query: ChatRequest):
    response = await get_ai_response(query.query)
    return response

