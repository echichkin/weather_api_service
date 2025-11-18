# Weather CLI (Windows)

Simple command-line helper that grabs your current GPS coordinates from the Windows Geolocation API and queries OpenWeather for human-readable conditions in Russian.

## Features
- Synchronous wrapper around WinRT geolocation (`winsdk.windows.devices.geolocation`) with proper asyncio handling.
- Typed weather domain layer with enums, dataclasses, and formatter for localized output.
- Fault-tolerant API client with custom exceptions (`CantGetCoordinates`, `ApiServiceError`).
- Optional history writer (`history.py`) to persist previously fetched forecasts into a text file.

## Requirements
- Windows 10+ with location services enabled for Python.
- Python 3.10+ (tested on 3.13).
- OpenWeather API key stored in `api_key.txt` inside the project directory.

### Dependencies
Install the required packages (only `winsdk` plus stdlib):
```bash
pip install winsdk
```

## Setup
1. Create a virtual environment (optional but recommended).
2. Place your OpenWeather key in `weather-yt/api_key.txt` (single line, no quotes).
3. Ensure Windows Settings → Privacy & security → Location allows desktop apps (Python) to read location.

## Usage
```bash
python weather.py
```
The script will:
1. Request GPS coordinates.
2. Fetch current weather from OpenWeather.
3. Print a string like `Moscow, температура 3°C, Облачно`.

If you want to persist results, import `history.save_weather` and pass a `PlainFileWeatherStorage` pointing to the file you want to append to.

## Troubleshooting
- **`Can't get coordinates`**: grant location permissions or run from a device with GPS / Wi-Fi positioning.
- **`Can't get weather by API`**: check the API key, network connectivity, or OpenWeather quota.
- **Empty output**: verify `api_key.txt` is not blank; the app raises a `RuntimeError` otherwise.

## Project Structure
- `weather.py` — main entry point.
- `coordinates.py` — GPS retrieval helpers.
- `weather_api_service.py` — OpenWeather client and parsing logic.
- `weather_formatter.py` — formatting helper.
- `history.py` — optional storage abstraction.
- `config.py` — configuration and API key loader.


