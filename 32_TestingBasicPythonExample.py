import requests

API_KEY = "369e933d7ba437eedc340c61c2b03d9e"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
                weather = data['weather'][0]['description']
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                
                print("\n📡 ရာသီဥတုပြချက်")
                print(f"မြို့: {city}")
                print(f"ရာသီဥတုအခြေအနေ: {weather}")
                print(f"အပူချိန်: {temp}°C")
                print(f"ခံစားရသောအပူချိန်: {feels_like}°C")
                print(f"စိုထိုင်းဆ: {humidity}%")
                print(f"လေတိုက်နှုန်း: {wind_speed} m/s")
        else:
            print("❌ City not found. Please try again.\n")

    except requests.exceptions.RequestException as e:
        print("📡 Network error occurred.")
        print("Error:", e)

# 🔁 Loop until user exits
while True:
    city = input("Enter city name (type 'exit' to quit): ")
    if city.lower() == "exit":
        print("👋 Exiting... Goodbye!")
        break
    get_weather(city)

