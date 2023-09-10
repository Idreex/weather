import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def current_weather(city='ibadan'):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == '__main__':
    city = input(
        '\nEnter the city to fetch its weather\n').lower().strip()
    weather_data = current_weather(city)
    pprint(weather_data)


    
