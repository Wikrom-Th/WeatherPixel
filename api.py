import requests
from enum import Enum

#for parsing URLs in geocoding
import urllib.parse

from config import LOCATION_API_URL, WEATHER_API_URL, GOOGLE_GEOCODE_API_URL, OPENWEATHER_GEOCODE_API_URL
from secret import WEATHER_API_KEY

class ApiProvider(Enum):
    OPENWEATHER = 1
    GOOGLE = 2

DEFAULT_GEOCODING_PROVIDER = ApiProvider.OPENWEATHER

try:
    from secret import GOOGLE_MAPS_API_KEY
    DEFAULT_GEOCODING_PROVIDER = ApiProvider.GOOGLE
except ImportError:
    print("Could not find Google Maps API Key in `secret.py`")
    print("Defaulting to OpenWeather API for Geocoding")


class Api:
    def __init__(self, url, api_key=""):
        self.req_url = url
        self.api_key = api_key
        
    def api_request(self, url):
        req = requests.get(url)
        self.data = req.json()

class Location(Api):
    def __init__(self):
        super().__init__(LOCATION_API_URL)

    def api_request(self):
        super().api_request(self.req_url)

class Geocoder(Api):
    def __init__(self, provider=DEFAULT_GEOCODING_PROVIDER):
        self.provider = provider

        if self.provider == ApiProvider.GOOGLE:
            super().__init__(GOOGLE_GEOCODE_API_URL, GOOGLE_MAPS_API_KEY)
            
        elif self.provider == ApiProvider.OPENWEATHER:
            super().__init__(OPENWEATHER_GEOCODE_API_URL, WEATHER_API_KEY)
            print("WARNING: Using OpenWeather API for Geocoding, data input method will be restrictive to the format below:")
            print("input: `{city name},{state code (US only)},{country code}`")

    def get_lat_lon(self, input):
        if self.provider == ApiProvider.GOOGLE:
            self.api_request(self.req_url + f"json?address={urllib.parse.quote(input)}&key={self.api_key}")

            self.coords = self.data['results'][0]['geometry']['location']
            self.coords['lon'] = self.coords['lng']
            self.coords.pop('lng')
        
        elif self.provider == ApiProvider.OPENWEATHER:
            self.api_request(self.req_url + f"direct?q={input}&appid={self.api_key}")

            self.coords = {}

            self.coords['lat'] = self.data[0]['lat']
            self.coords['lon'] = self.data[0]['lon']
    
class Weather(Api):
    def __init__(self):
        super().__init__(WEATHER_API_URL, WEATHER_API_KEY)

    def get_current_weather(self, lat, lon):
        self.api_request(self.req_url + f"weather?lat={lat}&lon={lon}&appid={self.api_key}")