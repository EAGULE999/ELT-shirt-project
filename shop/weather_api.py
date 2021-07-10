import requests
from tkinter import *
import math

city_name = "Riga,LV"
api_key = "8d57e070b401c3295a7f0fc3f2c6836f"


def get_weather(api_key,city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    res = requests.get(url).json()

    temp = res

    print(res)


get_weather(api_key, city_name)



