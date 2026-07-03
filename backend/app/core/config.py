from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Go from:
# backend/app/core/config.py
# up three folders to:
# cad-ai-agent-v2/
BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    PROJECT_NAME: str = "CAD Tutor AI"
    VERSION: str = "1.0.0"

    DEBUG: bool = True

    AI_PROVIDER: str = "gemini"

    GEMINI_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
