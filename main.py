from config import COM_PORT
from src.api import ApiManager
from src.serial_com import WeatherSerial
from src.gui import MyApp

import customtkinter

apimanager = ApiManager()
myserial = WeatherSerial(COM_PORT)

customtkinter.set_appearance_mode("system")

app = MyApp(apimanager, myserial)
app.geometry("800x600")

app.mainloop()