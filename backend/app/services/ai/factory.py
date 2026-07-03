from app.core.config import settings
from app.services.ai.gemini import GeminiProvider


def get_ai():
    if settings.AI_PROVIDER == "gemini":
        return GeminiProvider()

    raise Exception(f"Unknown AI provider: {settings.AI_PROVIDER}")
