import asyncio
from dataclasses import dataclass
import winsdk.windows.devices.geolocation as wdg

from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


async def _get_position_async():
    locator = wdg.Geolocator()
    return await locator.get_geoposition_async()


def get_gps_coordinates() -> Coordinates:
    "Returns current coordinates using laptop GPS"
    try:
        try:
            pos = asyncio.run(_get_position_async())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            pos = loop.run_until_complete(_get_position_async())
            loop.close()

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