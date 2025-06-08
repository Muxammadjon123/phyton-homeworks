import requests

api_key = "25a7399acd4dd0eade84ac53f45bcafa"
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")
else:
    print("Failed to get data:", response.status_code, response.text)

