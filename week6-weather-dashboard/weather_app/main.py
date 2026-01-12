from weather_app.config import API_KEY, BASE_URL
from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import (
    parse_current_weather,
    parse_5day_forecast,
    convert_temp
)
from weather_app.weather_display import show_dashboard

def main():
    api = WeatherAPI(API_KEY, BASE_URL)
    unit = "C"

    while True:
        user_input = input(
            "\nSearch city or command (help/unit/quit): "
        ).strip()

        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break

        if user_input.lower() == "help":
            print("\nCommands:")
            print(" help  - show commands")
            print(" unit  - toggle °C / °F")
            print(" quit  - exit program")
            continue

        if user_input.lower() == "unit":
            unit = "F" if unit == "C" else "C"
            print(f"✅ Unit changed to °{unit}")
            continue

        current_data = api.get_current_weather(user_input)
        forecast_data = api.get_5day_forecast(user_input)

        if current_data and forecast_data:
            current = parse_current_weather(current_data)
            forecast = parse_5day_forecast(forecast_data)

            current["temp"] = convert_temp(current["temp"], unit)
            current["feels_like"] = convert_temp(current["feels_like"], unit)

            for d in forecast:
                d["min"] = convert_temp(d["min"], unit)
                d["max"] = convert_temp(d["max"], unit)

            show_dashboard(current, forecast, unit)

if __name__ == "__main__":
    main()
