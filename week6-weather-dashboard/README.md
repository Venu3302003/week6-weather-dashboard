🌦️ Weather Dashboard Application

A Python-based Weather Dashboard that provides real-time weather data and 5-day forecasts for cities worldwide using the OpenWeatherMap API.
The project demonstrates API integration, modular design, caching, error handling, and CLI-based user interaction.
🚀 Features

. 🌍 Search weather for any city worldwide
. 🌡️ View current temperature, humidity, wind speed, and conditions
. 📅 5-day weather forecast
. 🔄 Temperature unit conversion (°C / °F)
. ⚡ API response caching to reduce API calls
. ❌ Graceful error handling (invalid city, network issues, API limits)
. ⭐ Save and manage favorite cities
. 🧩 Modular and scalable project structure
. 💻 Clean Command-Line Interface (CLI)

🛠️ Tech Stack

. Language: Python 3
. API: OpenWeatherMap
. Libraries: requests, python-dotenv
    . Concepts Used:
    . API Integration
    . File Handling
    . Modular Programming
    . Error Handling
    . Environment Variables
    . Caching Mechanism

📂 Project Structure
week6-weather-dashboard/
│── weather_app/
│   ├── __init__.py
│   ├── config.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   └── main.py
│
│── data/
│   ├── cache/
│   └── favorites.json
│
│── tests/
│   ├── test_api.py
│   ├── test_parser.py
│   └── test_display.py
│
│── .env.example
│── .gitignore
│── requirements.txt
│── README.md

🔑 API Setup
This project uses the OpenWeatherMap API.
1️⃣ Get API Key
1.Go to https://openweathermap.org/
2.Sign up / log in
3.Navigate to API Keys
4.Copy your API key
2️⃣ Configure Environment Variables
Rename .env.example to .env and add:
  WEATHER_API_KEY=your_api_key_here
▶️ How to Run the Project
Step 1: Install dependencies
  pip install -r requirements.txt
Step 2: Run the application
  python -m weather_app.main
🖥️ Sample Output
🌤️  WEATHER DASHBOARD
=======================

📍 Current Location: New York, US
🕐 Last Updated: 2024-01-25 14:30

Temperature: 12°C (Feels like: 10°C)
Conditions: Few clouds ☁️
Humidity: 65%
Wind: 15 km/h

5-Day Forecast:
Thu: 14°C / 8°C ☀️
Fri: 13°C / 7°C 🌤️
Sat: 11°C / 6°C 🌧️
Sun: 12°C / 7°C ⛅
Mon: 15°C / 9°C ☀️
🧪 Testing
Run tests using:
python -m unittest discover tests
🎯 Learning Outcomes
.Hands-on experience with real-world APIs
.Understanding modular project architecture
.Implementing clean CLI applications
.Working with JSON, caching, and environment variables
.Writing production-ready Python code

🚧 Future Enhancements
🌐 City autocomplete search
📍 Location detection by IP
📊 Weather statistics & charts
📁 Export weather data to CSV
⏰ Weather alerts & notifications
