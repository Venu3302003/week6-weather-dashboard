from datetime import datetime
from collections import defaultdict

def convert_temp(temp, unit):
    if unit == "F":
        return round((temp * 9 / 5) + 32)
    return round(temp)

def parse_current_weather(data):
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "visibility": int(data.get("visibility", 0) / 1000),
        "wind_speed": round(data["wind"]["speed"] * 3.6),
        "condition": data["weather"][0]["description"].title(),
        "updated": datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
    }

def parse_5day_forecast(data):
    daily = {}

    # group forecast items by date
    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]  # YYYY-MM-DD
        daily.setdefault(date, []).append(item)

    forecast = []

    # sort by date and take first 5 days
    for date in sorted(daily.keys())[:5]:
        items = daily[date]
        temps = [i["main"]["temp"] for i in items]

        date_obj = datetime.strptime(date, "%Y-%m-%d")

        forecast.append({
            "day": date_obj.strftime("%a"),
            "date": date_obj.strftime("%d %b %Y"),
            "min": round(min(temps)),
            "max": round(max(temps)),
            "condition": items[0]["weather"][0]["description"].title()
        })

    return forecast