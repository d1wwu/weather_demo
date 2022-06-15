from weather import Weather


def format_weather(weather: Weather) -> str:
    return (f"{weather.city}, {weather.temperature}\u00B0C, "
            f"{weather.weather_type}\n"
            f"\u263C\u2191 {weather.sunrise.strftime('%H:%M')}\n"
            f"\u263C\u2193 {weather.sunset.strftime('%H:%M')}")
