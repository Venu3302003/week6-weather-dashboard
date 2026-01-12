import requests

class WeatherAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_current_weather(self, city):
        url = f"{self.base_url}/weather"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        res = requests.get(url, params=params)

        if res.status_code == 200:
            return res.json()
        elif res.status_code == 404:
            print("❌ City not found. Try: City,CountryCode (e.g., Bangalore,IN)")
        else:
            print("❌ Failed to fetch weather data")
        return None

    def get_5day_forecast(self, city):
        url = f"{self.base_url}/forecast"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        res = requests.get(url, params=params)

        if res.status_code == 200:
            return res.json()
        return None
