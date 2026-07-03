from fastapi import APIRouter

from app.services.ai.factory import get_ai_provider

router = APIRouter()


@router.get("/tutorial/test")
async def tutorial_test():

    ai = get_ai_provider()

    response = await ai.generate_text(
        "Hello"
    )

    return {
        "provider": ai.__class__.__name__,
        "response": response,
    }
