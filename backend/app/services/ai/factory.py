from app.core.config import settings

from app.services.ai.gemini import GeminiProvider
from app.services.ai.openai import OpenAIProvider


def get_ai_provider():
    """
    Returns whichever AI provider is selected
    inside .env
    """

    if settings.AI_PROVIDER.lower() == "gemini":
        return GeminiProvider()

    if settings.AI_PROVIDER.lower() == "openai":
        return OpenAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {settings.AI_PROVIDER}"
    )
