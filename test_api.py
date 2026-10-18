import json
import urllib.request

house = {
    "MedInc": 8.3252, "HouseAge": 41, "AveRooms": 6.984127,
    "AveBedrms": 1.02381, "Population": 322, "AveOccup": 2.555556,
    "Latitude": 37.88, "Longitude": -122.23,
}

req = urllib.request.Request(
    "http://127.0.0.1:5000/predict",
    data=json.dumps(house).encode(),
    headers={"Content-Type": "application/json"},
)
print(urllib.request.urlopen(req).read().decode())