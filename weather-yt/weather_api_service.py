from dataclasses import dataclass # подключаем декоратор для лаконичного объявления классов с данными.
from datetime import datetime 
from typing import TypeAlias, Literal #добавляем поддержку псевдонимов, чтобы делать типы кода более понятными.
from enum import Enum
import json
from json.decoder import JSONDecodeError
import ssl
import urllib.request
from urllib.error import URLError

from coordinates import Coordinates # импортируем класс координат из файла coordinates.py
import config
from exceptions import ApiServiceError

Celsius: TypeAlias = int # теперь если в аннотациях указано Celsius, ясно, что это именно температура в градусах °C

class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    CLOUDS = "Облачно"
    FOG = "Туман"

@dataclass(slots=True, frozen=True) # декоратор, который генерирует конструктор, repr, eq и другие служебные методы. Экономит время и делает код чище.
# slots=True — ускоряет работу и экономит память: все поля заранее фиксируются, запрещая новые атрибуты.
# frozen=True — делает объекты неизменяемыми (immutable): после создания нельзя поменять значения полей, как в namedtuple.
class Weather: # класс, который будет содержать данные о погоде.
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather from OpenWeather API and returns it"""
    openweather_response = _get_openweather_response(
        latitude = coordinates.latitude,
        longitude = coordinates.longitude
    )
    weather = _parse_openweather_respose(openweather_response)
    return weather

def _get_openweather_response(latitude: float, longitude: float) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError("Request error to OpenWeather")

def _parse_openweather_respose(openweather_response: str) -> Weather:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError("Error answer decoding")
    
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrize"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=_parse_city(openweather_dict)
    )

def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])

def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError("Weather type parsing error")
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError("Unknown weather type")

def _parse_sun_time(openweather_dict: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])

def _parse_city(openweather_dict: dict) -> str:
    return openweather_dict["name"]

if __name__ == "__main__":
    coords = Coordinates(latitude=55.7, longitude=37.6)
    try:
        print(get_weather(coords))
    except ApiServiceError as err:
        print(f"Error: {err}")