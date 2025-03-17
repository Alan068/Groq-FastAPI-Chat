from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from schemas import ChatRequest, ChatResponse
from services.groq import get_ai_response

router = APIRouter()

@router.post("/chat", summary="Chat with GroqAI", response_class=PlainTextResponse)
async def chat(query: ChatRequest):
    response = await get_ai_response(query.query)
    return response





# response_model=ChatResponse)
# async def chat_with_ai(request: ChatRequest):
#     response = await get_ai_response(request.query)
#     return ChatResponse(response=response)
