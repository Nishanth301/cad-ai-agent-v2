import json

from app.services.ai.factory import get_ai_provider


class TutorialService:

    def __init__(self):
        self.ai = get_ai_provider()

    async def generate_tutorial(
        self,
        image_path: str,
        software: str,
        difficulty: str,
    ):

        prompt = f"""
You are a professional CAD instructor.

Analyze the uploaded CAD model.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "software":"{software}",
    "difficulty":"{difficulty}",
    "object_name":"",
    "estimated_time":"",
    "features":[],
    "tutorial_steps":[]
}}

Do not write markdown.

Do not explain.

Return JSON only.
"""

        response = await self.ai.generate_text(
            prompt=prompt,
            image_path=image_path,
        )

        return json.loads(response)
    