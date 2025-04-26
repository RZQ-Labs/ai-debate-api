from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    # Database
    database_url: str = Field("postgresql+asyncpg://postgres:postgres@db:5432/debate_trainer", env="DATABASE_URL")

    # Redis
    redis_url: str = Field("redis://redis:6379/0", env="REDIS_URL")

    # OpenAI
    openai_api_key: Optional[str] = Field(None, env="OPENAI_API_KEY")
    openai_model: str = Field("gpt-4o", env="OPENAI_MODEL")

    # OpenRouter
    openrouter_api_key: Optional[str] = Field(None, env="OPENROUTER_API_KEY")
    openrouter_api_url: str = Field("https://openrouter.ai/api/v1", env="OPENROUTER_API_URL")
    openrouter_model_name: str = Field("deepseek/deepseek-r1:free", env="OPENROUTER_MODEL_NAME")

    # IndoBERT
    indobert_model_path: str = Field("indobenchmark/indobert-base-p1", env="INDOBERT_MODEL_PATH")

    # LLM Provider
    llm_provider: str = Field("openrouter", env="LLM_PROVIDER")

    # Loguru
    loguru_level: str = Field("INFO", env="LOGURU_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
