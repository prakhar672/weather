import requests

def get_weather(city):
    API_KEY = "dddf000a1b2948f486c212154250406"  # Your WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city.strip()}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print(f"❌ City not found: {data['error']['message']}")
            return

        location = data["location"]["name"] + ", " + data["location"]["country"]
        weather = data["current"]["condition"]["text"]
        temp = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        print(f"\n🌦 Weather in {location}:")
        print(f"Description : {weather}")
        print(f"Temperature : {temp}°C (feels like {feels_like}°C)")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind} km/h")

    except Exception as e:
        print("⚠️ Something went wrong:", e)

# --- Run App ---
city = input("Enter a city name: ")
get_weather(city)
