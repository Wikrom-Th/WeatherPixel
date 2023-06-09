# WeatherPixel
 A weather to dynamic LED visualization using Adafruit's NeoPixel

 ## Dependencies
 - Python3
 - Arduino or supporting boards
 
 ## Setup
 1. Install [Adafruit NeoPixel Library](https://github.com/adafruit/Adafruit_NeoPixel) on Arduino IDE
 2. Install requirements on python side with `pip install -r requirements.txt`
 3. Change the `LED_PIN` and `LED_COUNT` in [lighting.ino](./arduino_src/lighting/lighting.ino) to the pin you connected neopixel to and the amount of neopixel LEDs respectively
 4. Change the `COM_PORT` in [config.py](./config.py) to the current arduino com port number
 5. Make a `secret.py` in the repository folder
    - Put your [OpenWeather API Key](https://openweathermap.org/api) in the format of `WEATHER_API_KEY = "your_api_key"`
    - (Optional) Put your [Google Maps API Key](https://developers.google.com/maps) in the format of `GOOGLE_MAPS_API_KEY = "your_api_key"`

 ## Running the program
 1. Compile and Upload [lighting.ino](./arduino_src/lighting/lighting.ino) to your arduino board (with Neopixel connected to it)
 2. Run [main.py](./main.py)

 ## Potential TODOs
 - Weather Forecast
 - More precise lighting controls