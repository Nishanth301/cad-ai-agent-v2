from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Base class for every AI provider.
    Every AI model (Gemini, OpenAI, Ollama, etc.)
    must implement these methods.
    """

    @abstractmethod
    async def generate_text(self, prompt: str) -> str:
        """Generate a text response."""
        pass
    