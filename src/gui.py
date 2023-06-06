from src.api import ApiManager
from src.serial_com import WeatherSerial
import customtkinter

class MyApp(customtkinter.CTk):
    def __init__(self, apimanager: ApiManager, serial: WeatherSerial, blink_words = ["drizzle", "rain", "snow", "thunderstorm"]):
        super().__init__()
        self.apimanager = apimanager
        self.serial = serial
        self.blink_words = blink_words

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.location = customtkinter.CTkLabel(master=self.frame, text="Waiting for Location", font=("Verdana", 26))
        self.location.pack(padx=10, pady=30)

        self.weather = customtkinter.CTkLabel(master=self.frame, text="", font=("Verdana", 40))
        self.weather.pack(padx=10, pady=30)

        self.temp = customtkinter.CTkLabel(master=self.frame, text="", font=("Verdana", 40))
        self.temp.pack(padx=10, pady=30)

        self.btn = customtkinter.CTkButton(master=self.frame, text="Get Weather from Current Location", command=self.get_weather_curr_loc)
        self.btn.pack(padx=10, pady=60)

        self.loc_input = customtkinter.CTkEntry(master=self.frame, placeholder_text="Input Location")
        self.loc_input.pack(padx=10, pady=10)

        self.btn2 = customtkinter.CTkButton(master=self.frame, text="Get Weather from Inputted Location", command=self.get_weather_input_loc)
        self.btn2.pack(padx=10, pady=10)

    def get_curr_weather(self):
        self.apimanager.get_curr_weather()
        self.weather.configure(text=self.apimanager.weather['status'])
        self.temp.configure(text=f"{self.apimanager.weather['temp']}°C")

        status = self.apimanager.weather['status'].lower()
        blink = 0

        for word in self.blink_words:
            if word in status:
                blink = 1

        self.serial.write_temp(self.apimanager.weather['temp'], blink)

    def get_weather_curr_loc(self):
        self.apimanager.get_curr_loc()
        self.location.configure(text=self.apimanager.loc_text)

        self.get_curr_weather()

    def get_weather_input_loc(self):
        self.loc_input_text = self.loc_input.get()
        self.apimanager.get_input_loc(self.loc_input_text)
        self.location.configure(text=self.apimanager.loc_text)

        self.get_curr_weather()
        self.loc_input.delete(0, len(self.loc_input_text))