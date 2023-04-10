import requests

# URL for the API that provides the positions of the planets
url = "https://api.nasa.gov/planetary/positions"

# Parameters for the API request
params = {
    "body": "sun",
    "time": "now",
    "km": True,
    "verbose": False,
    "api_key": "N3g6CYqWrbZh9FckuLinQQAUg6paaAKdhqNNaefG",
}

# Make a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()

    # Print the current positions of the planets
    for planet in data:
        print(f"{planet['name']}: x={planet['x']}, y={planet['y']}, z={planet['z']}")
else:
    print("Error: Unable to retrieve planet positions")
