from app.services.ai.base import AIProvider


class GeminiProvider(AIProvider):

    async def generate_text(self, prompt: str) -> str:
        """
        Temporary implementation.

        We are NOT connecting Gemini yet.
        """

        return "Gemini provider connected successfully."
    