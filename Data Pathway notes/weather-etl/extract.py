import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    return response.json() if response.status_code == 200 else None

def extract_data(cities):
    data = []
    for city in cities:
        print(f"Fetching weather data for: {city}")
        weather = fetch_weather(city)
        if weather:
            data.append(weather)
        else:
            print(f"⚠️ Failed to fetch data for {city}")
    return data

