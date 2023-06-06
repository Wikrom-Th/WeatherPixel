from src.api import ApiManager
from src.gui import MyApp

import customtkinter

apimanager = ApiManager()

customtkinter.set_appearance_mode("system")

app = MyApp(apimanager)
app.geometry("800x600")

app.mainloop()