from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # --- APP ---
    APP_ENV: str = "dev"
    DATABASE_URL: str

    ## --- RabbitMQ ---
    RABBITMQ_URL: str
    RABBITMQ_QUEUE: str
    
    class Config: 
        env_file = ".env"

settings = Settings()

    


