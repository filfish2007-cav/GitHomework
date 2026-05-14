from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8080
    max_films: int | None = None
    data_file_path: str = "./films.json"
    MAX_FILMS: int = 100

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="utf-8",
    )


settings = Settings()
