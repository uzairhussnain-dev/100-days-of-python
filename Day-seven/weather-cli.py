import requests

API_KEY = "5187c05b9f02128ab4bf976e15962e04"

def get_weather():
    city = input("Enter city: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("❌ City not found or API issue")
            return

        print(f"\n📍 City: {data['name']}")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"🌥️ Condition: {data['weather'][0]['description']}")

    except Exception as e:
        print("Error:", e)

get_weather()