from datetime import datetime
from typing import NamedTuple

import requests

from exceptions import ApiServiceError, UnconfiguredEnvironment

try:
    import config
except UnconfiguredEnvironment:
    print("OPENWEATHER_API environment not configured")
    exit(1)

Celsius = int


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(city: str) -> Weather:
    url = config.OPENWEATHER_URL.format(city=city)
    try:
        response = requests.get(url).json()
    except requests.exceptions.RequestException:
        raise ApiServiceError
    return Weather(
        temperature=response["main"]["temp"],
        weather_type=response["weather"][0]["description"],
        sunrise=datetime.fromtimestamp(response["sys"]["sunrise"]),
        sunset=datetime.fromtimestamp(response["sys"]["sunset"]),
        city=city
    )
