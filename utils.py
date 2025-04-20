import json
from requests import get, RequestException
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather(lat: float, lon: float, location: str = "New York"):
    try:
        appid = os.getenv("WEATHER_API_KEY")
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}" 
    
        response = get(weather_url)
        
        data = response.json()
        
        # Trả về kết quả
        if data.get("cod") != 200:  # Kiểm tra nếu có lỗi
            print(f"Error: {data.get('message')}")
            return None
        
        weather_info = {
            "city": location,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        
        print(f"Weather data for {location}: {weather_info}")
        return weather_info
        
    except RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_location():
    try:
        loc = get('http://api.ipapi.com/api/161.185.160.93?access_key=e36e5da6ba1111853a66d6b1298b3db2')
        data = loc.json()
        return_values = {
            "city": data.get("city"),
            "country": data.get("country_name"),
            "region": data.get("region_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
        }
        print(return_values)
        return return_values
    except RequestException as e:
        print(f"Error fetching location: {e}")
        return None
    
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "lat": {
                        "type": "number",
                        "description": "The latitude of the city"
                    },
                    "lon": {
                        "type": "number",
                        "description": "The longitude of the city"
                    },
                    "location": {
                        "type": "string",
                        "description": "The name of the city from where to get the weather"
                    }
                },
                "required": ["lat", "lon", "location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_location",
            "description": "Get the current location of the user.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]


