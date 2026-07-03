from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "CAD Tutor AI"
    VERSION: str = "1.0.0"

    DEBUG: bool = True

    AI_PROVIDER: str = "gemini"

    GEMINI_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
