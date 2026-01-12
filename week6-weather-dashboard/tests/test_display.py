def test_display():
    from weather_app.weather_display import show_current_weather
    show_current_weather({
        "city": "Test",
        "country": "IN",
        "temp": 30,
        "feels_like": 32,
        "humidity": 60,
        "wind": 10,
        "condition": "Clear Sky",
        "updated": "Now"
    })
