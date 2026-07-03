from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    async def generate_tutorial(
        self,
        image_path: str,
        software: str,
        level: str,
    ) -> dict:
        """
        Generate CAD tutorial.
        """
        pass
    
    from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str
    ) -> str:
        pass
    