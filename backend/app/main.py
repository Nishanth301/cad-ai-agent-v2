from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.tutorial import router as tutorial_router
from app.api.upload import router as upload_router

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

app.include_router(health_router)
app.include_router(tutorial_router)
app.include_router(upload_router)


@app.get("/")
async def root():

    return {
        "message": "CAD Tutor AI Backend Running"
    }
