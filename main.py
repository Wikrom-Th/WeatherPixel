from api import ApiManager

apimanager = ApiManager()

apimanager.get_curr_loc()
apimanager.get_curr_weather()
print(apimanager.weather)

apimanager.get_input_loc("London")
apimanager.get_curr_weather()
print(apimanager.weather)