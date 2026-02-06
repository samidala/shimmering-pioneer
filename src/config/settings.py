from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import logging

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    # LLM Configuration
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL_NAME: str = "gpt-4o"
    
    # Tool Configuration
    SERPER_API_KEY: Optional[str] = None
    
    # App Settings
    LOG_LEVEL: str = "INFO"
    ENVIRONMENT: str = "development"

settings = Settings()

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
