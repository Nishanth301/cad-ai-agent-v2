from google import genai

from app.core.config import settings
from app.services.ai.base import AIProvider


class GeminiProvider(AIProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def generate_text(
        self,
        prompt: str,
        image_path: str | None = None,
    ) -> str:

        # For now we're ignoring image_path.
        # We'll implement Gemini Vision in the next sprint.

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text
    