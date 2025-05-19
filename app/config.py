import os
from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "Organic Food E-commerce Platform"
    ENVIRONMENT: str = "development"  # Options: development, staging, production
    DEBUG: bool = True

    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # Security settings
    SECRET_KEY: SecretStr = SecretStr(os.getenv("SECRET_KEY", "supersecretkey"))
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Payment gateway settings
    PAYMENT_GATEWAY_API_KEY: SecretStr = SecretStr(os.getenv("PAYMENT_GATEWAY_API_KEY", "your_payment_gateway_api_key"))
    PCI_DSS_COMPLIANCE: bool = True

    # Social sign-in settings
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "your_google_client_id")
    GOOGLE_CLIENT_SECRET: SecretStr = SecretStr(os.getenv("GOOGLE_CLIENT_SECRET", "your_google_client_secret"))
    APPLE_CLIENT_ID: str = os.getenv("APPLE_CLIENT_ID", "your_apple_client_id")
    APPLE_CLIENT_SECRET: SecretStr = SecretStr(os.getenv("APPLE_CLIENT_SECRET", "your_apple_client_secret"))

    # Performance settings
    MAX_USERS: int = 1000000
    HOME_PAGE_LOAD_TIME: float = 2.0  # in seconds
    CHECKOUT_FLOW_TIME: float = 4.0  # in seconds

    # Encryption settings
    ENCRYPTION_KEY: SecretStr = SecretStr(os.getenv("ENCRYPTION_KEY", "your_encryption_key"))

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Instantiate the settings
settings = Settings()