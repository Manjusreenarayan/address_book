from enum import Enum
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the database name and domain from the environment
DBNAME = os.getenv("DB_NAME")
DOMAIN = os.getenv("DOMAIN")

# Define an Enum for different environments
class Environment(str, Enum):
    LOCAL = "LOCAL"
    STAGING = "STAGING"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

    # Check if the environment is in debug mode
    @property
    def is_debug(self):
        return self in (self.LOCAL, self.STAGING, self.TESTING)

    # Check if the environment is for testing
    @property
    def is_testing(self):
        return self == self.TESTING

# Define a Config class with necessary configurations
class Config():
    # Set the database URL using the defined database name
    DATABASE_URL = f"sqlite:///./{DBNAME}.db"

    # Define the site domain
    SITE_DOMAIN = {DOMAIN}

    # Set the default environment as local
    ENVIRONMENT = Environment.LOCAL

    # Define the CORS origins and headers
    CORS_ORIGINS = ["*"]
    CORS_HEADERS = ["ALLOW_ORIGINS"]

    # Define the application version
    APP_VERSION = "0.1"
