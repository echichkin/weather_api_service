from dataclasses import dataclass # подключаем декоратор для лаконичного объявления классов с данными.
from datetime import datetime 
from typing import TypeAlias #добавляем поддержку псевдонимов, чтобы делать типы кода более понятными.
from enum import Enum
from coordinates import Coordinates # импортируем класс координат из файла coordinates.py

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
    """Requests weather data from the API and returns it"""
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat('2022-05-04 04:00:00'),
        sunset=datetime.fromisoformat('2022-05-04 20:25:00'),
        city='Moscow'
    )