from pydantic import BaseModel
from typing import List


class TutorialStep(BaseModel):
    step: int
    title: str
    instruction: str


class TutorialResponse(BaseModel):
    software: str
    difficulty: str
    object_name: str
    estimated_time: str
    features: List[str]
    tutorial_steps: List[TutorialStep]
    