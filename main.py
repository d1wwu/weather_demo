from exceptions import ApiServiceError
from formatter import format_weather
from location import get_location
from weather import get_weather


def main():
    city = None
    weather = None

    try:
        city = get_location().city
    except ApiServiceError:
        print("Can't get location")
        exit(1)
    try:
        weather = get_weather(city)
    except ApiServiceError:
        print("Can't get weather data")
        exit(1)
    print(format_weather(weather))


if __name__ == '__main__':
    main()
