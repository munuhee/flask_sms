# config.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class Config:
    FLASK_ENV = os.getenv('FLASK_ENV')
    AT_USERNAME = os.getenv('AT_USERNAME')
    AT_API_KEY = os.getenv('AT_API_KEY')
