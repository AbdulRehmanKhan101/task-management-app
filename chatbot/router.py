import os

import httpx
from fastapi import APIRouter, HTTPException, status

from chatbot.dtos import ChatRequest, ChatResponse


chat_routes = APIRouter(prefix="/chat", tags=["chat"])


@chat_routes.post("", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat(body: ChatRequest) -> ChatResponse:
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The chatbot is not configured yet.",
        )

    payload = {
        "model": os.getenv("HUGGINGFACE_MODEL", "Qwen/Qwen2.5-72B-Instruct"),
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a general planning and productivity assistant. "
                    "You cannot access or change the user's task or account data."
                ),
            },
            *[message.model_dump() for message in body.messages],
        ],
        "temperature": 0.7,
        "max_tokens": 500,
    }

    try:
        async with httpx.AsyncClient(timeout=45) as client:
            response = await client.post(
                "https://router.huggingface.co/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json=payload,
            )
    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The chatbot service could not be reached.",
        ) from error

    if response.is_error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The chatbot service returned an error.",
        )

    try:
        message = response.json()["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError, ValueError) as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The chatbot service returned an unexpected response.",
        ) from error

    return ChatResponse(message=message)