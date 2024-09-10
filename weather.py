import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass


@dataclass
class WeatherData:
    main:str
    description: str
    icon:str
    temp : float 

load_dotenv()
api_key = os.getenv('API_KEY')
# print(api_key)

def get_lat_and_long(city_name,state_code,country_code,API_key):
    resp = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}",timeout=10).json()
    data = resp[0]
    lat,lon = data.get('lat') ,data.get('lon')
    return lat,lon

def get_current_weather(lat,lon,API_key):
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric",timeout=10).json()
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temp=resp.get('main').get('temp')
    )
    return data

def main(city_name,state_name,country_name):
    lat,lon =get_lat_and_long(city_name,state_name,country_name,api_key)
    weather = get_current_weather(lat,lon,api_key)
    return weather
if __name__ == "__main__":
    lat,lon =get_lat_and_long('Toronto','ON','Canada',api_key)
    print(get_current_weather(lat,lon,api_key))
# print(get_lat_and_long('Toronto','ON','Canada',api_key))
