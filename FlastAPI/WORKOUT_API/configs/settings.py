from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DB_URL: str = Field(default = '')

settings = Settings()