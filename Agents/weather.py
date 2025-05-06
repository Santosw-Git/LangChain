from langchain_core.tools import tool
import requests

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city by finding its latitude and longitude.
    """
    
    api_key = "95b99501eaa94ee59ae121239250605"
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    return str(response.json())
