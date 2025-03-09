from fastapi import FastAPI
import requests

app = FastAPI()

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
def get_weather(city: str):
    """Fetch weather data for a given city"""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
    else:
        return {"error": "City not found"}


# from fastapi import FastAPI
# import requests

# app = FastAPI()

# # Replace with your OpenWeatherMap API key
# API_KEY = "your_api_key"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# @app.get("/weather/{city}")
# def get_weather(city: str):
#     """Fetch weather data for a given city"""
#     params = {"q": city, "appid": API_KEY, "units": "metric"}
#     response = requests.get(BASE_URL, params=params)
    
#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "city": data["name"],
#             "temperature": data["main"]["temp"],
#             "humidity": data["main"]["humidity"],
#             "weather": data["weather"][0]["description"],
#         }
#     else:
#         return {"error": "City not found"}
