from location import Location

loc = Location()
loc.api_request()

data = loc.get_location()
print(data['city'])
print(data['region'])