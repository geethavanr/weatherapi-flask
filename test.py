import requests
import json

city="Toronto"
country="CAN"

api_key = "###"

weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

weather_data = weather_url.json()

temp=weather_data