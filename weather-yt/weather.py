from exceptions import ApiServiceError, CantGetCoordinates
from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    try:
        coordinates = get_gps_coordinates()
    except CantGetCoordinates:
        print("Can't get GPS coordinates")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print("Can't get weather by API")
        exit(1)
    formatted_weather = format_weather(weather)
    print(formatted_weather)

if __name__ == "__main__":
    main()
