import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***")

    city = input("\nPlease enter a city name:").capitalize()

    request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric"
    # print(request_url)
    weather_data = requests.get(request_url).json()

    # print(weather_data)
    print(f"Current weather for :{city.rjust(5)}")
    print(f"Current temperature:{weather_data["main"]['temp']}")
    print(f"Feels like:{weather_data["main"]['feels_like']}")


get_current_weather()    