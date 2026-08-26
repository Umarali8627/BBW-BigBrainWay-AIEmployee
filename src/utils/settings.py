from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra = "ignore")

    GROQ_API_KEY: str
    MODEL: str
    OPEN_ROUTER_API_KEY:str


settings = Settings()


