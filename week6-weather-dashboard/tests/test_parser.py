def test_parser():
    sample = {
        "name": "Test",
        "sys": {"country": "IN"},
        "main": {"temp": 30, "feels_like": 32, "humidity": 60},
        "wind": {"speed": 5},
        "weather": [{"description": "clear sky"}],
        "dt": 1700000000
    }

    from weather_app.weather_parser import parse_current_weather
    data = parse_current_weather(sample)
    assert data["city"] == "Test"
