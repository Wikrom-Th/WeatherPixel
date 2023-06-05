from config import API_URL
import requests

class Location:
    def api_request(self):
        req = requests.get(API_URL)
        self.data = req.json()

    def get_location(self):
        return self.data