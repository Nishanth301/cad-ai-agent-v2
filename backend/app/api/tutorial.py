from fastapi import APIRouter

from app.services.tutorial.tutorial_service import TutorialService

router = APIRouter()

tutorial_service = TutorialService()


@router.get("/tutorial/test")
async def tutorial_test():

    response = await tutorial_service.generate_tutorial(
        image_path="uploads/test.png",
        software="Fusion 360",
        difficulty="Beginner",
    )

    return {
        "response": response
    }
