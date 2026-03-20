"""Configuration via environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    anthropic_api_key: str = ""
    openai_api_key: str = ""
    docs_root: str = "../../docs"
    chroma_path: str = "./chroma_data"
    embedding_model: str = "text-embedding-3-small"
    generation_model: str = "claude-haiku-4-5-20251001"
    max_chunks: int = 6
    max_tokens: int = 1024
    api_host: str = "0.0.0.0"
    api_port: int = 8901
    allowed_origins: list[str] = ["https://ai-delivery.io"]
    rate_limit_rpm: int = 30
    embedding_dimensions: int = 1536

    model_config = {"env_prefix": "CHAT_", "env_file": ".env"}


settings = Settings()
