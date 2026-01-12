def icon(condition):
    c = condition.lower()
    if "clear" in c:
        return "☀️"
    if "cloud" in c:
        return "☁️"
    if "rain" in c:
        return "🌧️"
    return "🌤️"

def show_dashboard(current, forecast, unit):
    print("\n🌤️  WEATHER DASHBOARD")
    print("=" * 23)

    print(f"\n📍 Current Location: {current['city']}, {current['country']}")
    print(f"🕐 Last Updated: {current['updated']}")

    print("\nCurrent Weather:")
    print("────────────────")
    print(f"Temperature: {current['temp']}°{unit} (Feels like: {current['feels_like']}°{unit})")
    print(f"Conditions:   {current['condition']} {icon(current['condition'])}")
    print(f"Humidity:     {current['humidity']}%")
    print(f"Wind:         {current['wind_speed']} km/h")
    print(f"Pressure:     {current['pressure']} hPa")
    print(f"Visibility:   {current['visibility']} km")

    print("\n5-Day Forecast:")
    print("───────────────")
    for d in forecast:
        print(f"{d['day']} {d['date']}:  {icon(d['condition'])}  {d['max']}°{unit} / {d['min']}°{unit}")
