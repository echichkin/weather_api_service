import asyncio
import winsdk.windows.devices.geolocation as wdg
import requests
from pprint import pprint

async def get_coords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return [pos.coordinate.latitude, pos.coordinate.longitude]

def get_loc():
    try:
        return asyncio.run(get_coords())
    except PermissionError:
        print("ERROR: Необходимо разрешить доступ приложению к геолокации в настройках Windows")

print(get_loc())

[lat, lon] = get_loc()
print(lat, lon)
with open('api_key.txt', 'r') as f:
    appid = f.read().strip()
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&lang=ru&units=metric'
response = requests.get(url)
data = response.json()
pprint(data)