from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

DEFAULT_SYSTEM_PROMPT = (
    "You are an expert debate coach and assistant. Guide the user in constructing clear, logical, and persuasive arguments while maintaining a respectful and neutral tone. "
    "Help the user understand both sides of any issue. "
    "Encourage critical thinking and evidence-based reasoning. "
    "Provide feedback on argument structure, clarity, and persuasiveness. "
    "When appropriate, suggest ways to strengthen the user's arguments or anticipate counterpoints. "
    "Your goal is to foster effective debate skills and respectful, thoughtful discussion."
)

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

    # JWT
    jwt_secret_key: str = Field("", env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")
    jwt_access_token_expires_in: int = Field(1800, env="JWT_ACCESS_TOKEN_EXPIRES_IN")
    jwt_refresh_token_expires_in: int = Field(604800, env="JWT_REFRESH_TOKEN_EXPIRES_IN")

    # Prompt
    prompt_max_tokens: int = Field(1024, env="PROMPT_MAX_TOKENS")
    default_prompt: str = Field(DEFAULT_SYSTEM_PROMPT, env="DEFAULT_PROMPT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
