from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health():

    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
    }
