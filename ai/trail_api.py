from ai.trail import Trail, TrailList
import requests

"https://www.hikingproject.com/data/get-trails?lat=40.0274&lon=-105.2519&maxDistance=10&key=200932678-b6a96c1d20b73dc70bee2145176ce8a7"


class Trail_API:
    def __init__(self, latitude, longitude, distance=10):
        self._latitude = latitude
        self._longitude = longitude
        self._distance = distance
        self._key = '200932678-b6a96c1d20b73dc70bee2145176ce8a7'
        self._url = f"https://www.hikingproject.com/data/get-trails?lat={self._latitude}&lon={self._longitude}&maxDistance={self._distance}&key={self._key}"
        print(self._url)

    def getTrails(self):
        r = requests.get(self._url)
        self._data = r.json()
        all_trails = TrailList()
        for trail in self._data['trails']:
            new_trail = Trail(trail['name'], None, trail['length'], trail['high'], trail['summary'], trail['latitude'],
                              trail['longitude'], trail['difficulty'])
            all_trails.addTrail(new_trail)
        return all_trails


if __name__ == "__main__":
    la_latitude = 40.0274
    la_longitude = -105.2519
    myTrails = Trail_API(la_latitude, la_longitude)
    trails = myTrails.getTrails()