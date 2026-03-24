"""Configuration via environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ollama_api_key: str = ""
    ollama_host: str = "https://ollama.com"
    docs_root: str = "../../docs"
    chroma_path: str = "./chroma_data"
    generation_model: str = "gemma3:12b-cloud"
    max_chunks: int = 6
    max_tokens: int = 1024
    api_host: str = "0.0.0.0"
    api_port: int = 8901
    allowed_origins: list[str] = ["https://ai-delivery.io"]
    rate_limit_rpm: int = 30

    model_config = {"env_prefix": "CHAT_", "env_file": ".env"}


settings = Settings()
