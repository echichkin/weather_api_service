# Получаем API ключ из файла


USE_ROUNDED_COORDS = True
with open('api_key.txt', 'r') as f:
    OPENWEATHER_API = f.read().strip()
OPENWEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&lang=ru&units=metric'