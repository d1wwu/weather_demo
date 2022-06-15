import os

from exceptions import UnconfiguredEnvironment

LANGUAGE = "en"
OPENWEATHER_API = os.getenv('OPENWEATHER_API')
if not OPENWEATHER_API:
    raise UnconfiguredEnvironment

OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "q={city}&units=metric&lang=" + LANGUAGE + "&APPID=" + OPENWEATHER_API + ""
)
