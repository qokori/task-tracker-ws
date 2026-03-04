from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DATABASE_URL: str
    DATABASE_ECHO: bool

    SECRET_KEY: str
    JWT_ALGORITHM: str

    FASTAPI_HOST: str
    FASTAPI_PORT: int
    FASTAPI_RELOAD: bool


settings = Settings()
