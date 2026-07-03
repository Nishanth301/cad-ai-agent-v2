from fastapi import APIRouter

from app.services.ai.factory import get_ai

router = APIRouter()


@router.get("/hello-ai")
async def hello_ai():

    ai = get_ai()

    response = await ai.generate(
        "Say hello in one sentence."
    )

    return {
        "response": response
    }
