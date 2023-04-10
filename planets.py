import requests
import json

url = "https://api.nasa.gov/planetary/positions"

querystring = {"start_date":"2023-04-07","end_date":"2023-04-07","body":"sun","step":"1d"}

headers = {
    "Accept": "application/json",
    "api_key": "N3g6CYqWrbZh9FckuLinQQAUg6paaAKdhqNNaefG"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

for planet in data:
    print("Planet name:", planet["name"])
    print("Planet location (x, y, z):", planet["positions"][0]["x"], planet["positions"][0]["y"], planet["positions"][0]["z"])
    print()
