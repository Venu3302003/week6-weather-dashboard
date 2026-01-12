from weather_app.weather_api import WeatherAPI

def test_api_object():
    api = WeatherAPI("test", "http://test")
    assert api.cache_time == 600
