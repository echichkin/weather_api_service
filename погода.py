import asyncio
import winsdk.windows.devices.geolocation as wdg
import requests
from pprint import pprint
# Получаем координаты из геолокации
async def get_coords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return [pos.coordinate.latitude, pos.coordinate.longitude]

# Получаем координаты из геолокации
def get_loc():
    try:
        return asyncio.run(get_coords())
    except PermissionError:
        print("ERROR: Необходимо разрешить доступ приложению к геолокации в настройках Windows")

# # Выводим координаты в удобочитаемом виде
# print(get_loc())

# Получаем координаты из геолокации
[lat, lon] = get_loc()
print(lat, lon)

# Получаем API ключ из файла
with open('api_key.txt', 'r') as f:
    appid = f.read().strip()

# Формируем URL для запроса
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&lang=ru&units=metric'
# Выполняем запрос
response = requests.get(url)
# Преобразуем ответ в JSON
data = response.json()
# Выводим данные в удобочитаемом виде
pprint(data)