from api import Location, Weather, Geocoder, ApiProvider

# loc = Location()
# loc.api_request()

# lat, lon = loc.data['loc'].split(",")

geo = Geocoder()
geo.get_lat_lon("Nakhon Pathom")

print(geo.coords)

lat, lon = geo.coords['lat'], geo.coords['lon']

weather = Weather()
weather.get_current_weather(lat, lon)

print(weather.data)