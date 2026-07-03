from app.services.ai.base import AIProvider


class OpenAIProvider(AIProvider):

    async def generate_text(
        self,
        prompt: str,
        image_path: str | None = None,
    ) -> str:

        return "OpenAI provider placeholder."
    