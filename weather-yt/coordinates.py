from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    "Returns current coordinates from GPS"
    return Coordinates(latitude=10, longitude=20)