from pydantic_settings import BaseSettings, SettingsConfigDict


class RecipesDbSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RECIPES_DB_", env_file="../.env", extra="ignore"
    )
    user: str = "user"
    password: str = "password"
    db: str = "db"
    host: str = "localhost"
    port_host: int = 5432
    echo: bool = True


class FastAPISettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="FASTAPI_", env_file="../.env", extra="ignore"
    )
    host: str = "localhost"
    port: int = 8080


class Settings(BaseSettings):
    recipes_db: RecipesDbSettings = RecipesDbSettings()
    fastapi_settings: FastAPISettings = FastAPISettings()


settings = Settings()
