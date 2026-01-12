from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

if not API_KEY:
    raise ValueError("API key not found. Set WEATHER_API_KEY in .env file")
