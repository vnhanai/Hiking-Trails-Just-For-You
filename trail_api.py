from pprint import pprint
import requests
import os

class Trail_API:
    def __init__(self, latitude, longitude, distance=10):
        self._latitude = latitude
        self._longitude = longitude
        self._distance = distance
        self._key = key = os.getenv('TRAIL_API_KEY')
        self._url = f"https://www.hikingproject.com/data/get-trails?lat={self._latitude}&lon={self._longitude}&maxDistance={self._distance}&key={key}"
        print(self._url)

    def getTrails(self):
        r = requests.get("https://www.hikingproject.com/data/get-trails?lat=40.0274&lon=-105.2519&maxDistance=10&key=200932678-b6a96c1d20b73dc70bee2145176ce8a7")
        response = r.json()
        print("response is")
        print(response)
    
if __name__ == "__main__":
    la_latitude = 40.0274
    la_longitude = -105.2519
    myTrails = Trail_API(la_latitude, la_longitude)
    myTrails.getTrails()
