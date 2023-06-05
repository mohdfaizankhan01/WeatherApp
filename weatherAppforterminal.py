import requests
from PIL import Image
from datetime import datetime, timedelta
import pandas as pd
from io import BytesIO
import time

api_key = "19c1a828e9ad1d24f57ee83f33d70d00"

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def getweather(city):
    try:
        result = requests.get(url.format(city, api_key))
        result.raise_for_status()  # Raises an exception for non-2xx status codes
        json = result.json()
        country = json['sys']['country']
        temp = json['main']['temp'] - 273.15
        temp_feels = json['main']['feels_like'] - 273.15
        humid = json['main']['humidity']
        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']
        ws = json['wind']['speed']
        res = [country, round(temp, 1), round(temp_feels, 1), humid, lon, lat, icon, des, ws]
        return res, json
    except requests.exceptions.HTTPError as errh:
        return None, f"Error in Search"
    except requests.exceptions.ConnectionError as errc:
        return None, f"Connection Error: {errc}"
    except requests.exceptions.Timeout as errt:
        return None, f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return None, f"Error: {err}"


print("WEATHER APP")
city_name = input("Enter a city name: ")
if city_name:
    res, json = getweather(city_name)
    if res is not None:
        print('Current Temp: ' + str(round(res[1], 2)) + '°C')
        print('Feels Like: ' + str(round(res[2], 2)) + '°C')
        print('Humidity: ' + str(round(res[3], 2)) + '%')
        print('Wind Speed: ' + str(round(res[8], 2)) + ' m/s')
        print('Status: ' + res[7])

    else:
        print('Error in Search!!!!') # Display the error message