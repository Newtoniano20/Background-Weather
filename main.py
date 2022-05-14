import requests
import ctypes
import pathlib
import geocoder
import json

CLEAR_SKY = "\clearsky.jpg"
FEW_CLOUDS = "\\brokenclouds.jpg"
rain = "\\rain.jpg"
thunderstorm = '\\thunderstorm.jpg'
snow = "\snow.jpg"
mist = "\mist.png"
drizzle = "\drizzle.jpg"

g = geocoder.ip('me')
coord = g.latlng
coord = (31.173741, 121.305441)
lat = coord[0]
lon = coord[1]

# API KEY FROM https://openweathermap.org/ :
API_KEY = ""
API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"


if __name__ == "__main__":
    content = json.loads(requests.get(API_URL).content)
    print(content)
    description = content["weather"][0]["main"]
    weather = {"Clear": CLEAR_SKY,
               "Drizzle": drizzle,
               "Clouds": FEW_CLOUDS,
               "Rain": rain,
               "Thunderstorm": thunderstorm,
               "Snow": snow,
               "Atmosphere": mist}

    path = str(pathlib.Path(__file__).parent.resolve()) + "\Pictures" + weather[description]
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
