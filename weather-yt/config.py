from pathlib import Path

USE_ROUNDED_COORDS = True

API_KEY_PATH = Path(__file__).with_name("api_key.txt")

try:
    with API_KEY_PATH.open("r", encoding="utf-8") as file:
        OPENWEATHER_API = file.read().strip()
except FileNotFoundError as err:
    raise RuntimeError(f"Не найден файл с API ключом: {API_KEY_PATH}") from err

if not OPENWEATHER_API:
    raise RuntimeError("api_key.txt пуст — добавьте ключ OpenWeather")

OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&appid={api_key}&lang=ru&units=metric"
)