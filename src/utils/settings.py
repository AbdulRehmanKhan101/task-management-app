from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
    DB_CONNECTION:str
    SECRET_KEY:str
    ALGORITHM:str
    EXP_TIME:int
    ALLOWED_ORIGINS:str="*"  # comma-separated list, e.g. "https://your-frontend.onrender.com"

settings=Settings()