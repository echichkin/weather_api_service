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
    pass

print(WeatherType.CLEAR)  # WeatherType.CLEAR 
print(WeatherType.CLEAR.value)  # Ясно 
print(WeatherType.CLEAR.name)  # CLEAR


# for weather_type in WeatherType:
#     print(weather_type.name, weather_type.value)

def what_should_i_do(weather_type: WeatherType) -> None:
    match weather_type:
        case WeatherType.THUNDERSTORM | WeatherType.RAIN:
            print('Уф, лучше сиди дома')
        case WeatherType.CLEAR:
            print('O, отличная погодка')
        case _:
            print('Ну так, выходить можно')

what_should_i_do(WeatherType.RAIN)