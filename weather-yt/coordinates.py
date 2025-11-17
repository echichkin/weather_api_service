from dataclasses import dataclass
import winsdk.windows.devices.geolocation as wdg

from exceptions import CantGetCoordinates

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    "Returns current coordinates using laptop GPS"
    try:
        locator = wdg.Geolocator()
        pos = locator.get_geoposition_async().get()
        latitude = pos.coordinate.point.position.latitude
        longitude = pos.coordinate.point.position.longitude

        if latitude is None or longitude is None:
            raise CantGetCoordinates

        return Coordinates(longitude=longitude, latitude=latitude)

    except Exception as err:
        print(f"Can't get coordinates: {err}")
        raise CantGetCoordinates from err

if __name__ == "__main__":
    try:
        print(get_gps_coordinates)
    except CantGetCoordinates as err:
        print(f"Error: {err}")