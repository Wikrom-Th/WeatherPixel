# WeatherPixel
 A weather to dynamic LED visualization using Adafruit's NeoPixel

 ## Dependencies
 - Python3
 - Arduino or supporting boards
 
 ## Installation
 1. Install [Adafruit NeoPixel Library](https://github.com/adafruit/Adafruit_NeoPixel) on Arduino IDE
 2. Install requirements on python side with `pip install -r requirements.txt`
 3. Make a `secret.py` in the repository folder
    - Put your [OpenWeather API Key](https://openweathermap.org/api) in the format of `WEATHER_API_KEY = "your_api_key"`
    - (Optional) Put your [Google Maps API Key] in the format of `GOOGLE_MAPS_API_KEY = "your_api_key"`
