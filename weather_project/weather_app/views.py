import requests
from django.shortcuts import render

# Replace with your API key from OpenWeatherMap
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(request):
    city = request.GET.get('city', 'Nairobi')  # Default city
    weather_data = {}

    if city:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "City not found!"}

    return render(request, "weather_app/weather.html", {"weather": weather_data, "city": city})

