# Weather Program Python Project 
import requests
from pprint import pprint

API_Key = '0b3a83fcc8f48460a2755826b93ee7e4'

city = input("Enter the city name: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weateher_data = requests.get(base_url).json()

pprint(weateher_data)
if weateher_data['cod'] == '404':
    print("City Not Found")


