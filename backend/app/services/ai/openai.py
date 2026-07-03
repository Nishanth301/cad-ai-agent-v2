from .base import AIProvider


class OpenAIProvider(AIProvider):

    async def generate_tutorial(
        self,
        image_path,
        software,
        level,
    ):

        raise NotImplementedError
    