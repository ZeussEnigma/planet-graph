import requests

url = "https://api.nasa.gov/planetary/apod"

querystring = {"api_key":"N3g6CYqWrbZh9FckuLinQQAUg6paaAKdhqNNaefG"}

headers = {
    "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
