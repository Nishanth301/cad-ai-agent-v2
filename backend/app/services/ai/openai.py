from app.services.ai.base import AIProvider


class OpenAIProvider(AIProvider):

    async def generate_text(self, prompt: str) -> str:
        """
        Placeholder until deployment.
        """

        return "OpenAI provider connected successfully."
    