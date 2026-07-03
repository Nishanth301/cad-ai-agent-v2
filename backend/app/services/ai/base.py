from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    async def generate_text(
        self,
        prompt: str,
        image_path: str | None = None,
    ) -> str:
        pass
    