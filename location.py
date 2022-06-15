from typing import NamedTuple

import requests

from exceptions import ApiServiceError


class Data(NamedTuple):
    ip: str
    city: str
    region: str
    country: str


def get_location() -> Data:
    ip_address = _get_ip()
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    except requests.exceptions.RequestException:
        raise ApiServiceError
    return Data(
        ip=ip_address,
        city=response.get("city"),
        region=response.get("region"),
        country=response.get("country_name")
    )


def _get_ip() -> str:
    try:
        response = requests.get('https://api64.ipify.org?format=json').json()
    except requests.exceptions.RequestException:
        raise ApiServiceError
    return response["ip"]
