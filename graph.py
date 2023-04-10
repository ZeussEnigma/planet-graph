import requests
import numpy as np
import matplotlib.pyplot as plt

# Define the base URL of the Horizons System API
base_url = "https://api.nasa.gov/planetary/positions"

# Define the list of planets to retrieve and their corresponding IDs in the Horizons System
planets = {
    "Mercury": "1",
    "Venus": "2",
    "Earth": "3",
    "Mars": "4",
    "Jupiter": "5",
    "Saturn": "6",
    "Uranus": "7",
    "Neptune": "8",
}

# Define the dictionary of colors for each planet
planet_colors = {
    "Mercury": "gray",
    "Venus": "orange",
    "Earth": "blue",
    "Mars": "red",
    "Jupiter": "brown",
    "Saturn": "yellow",
    "Uranus": "cyan",
    "Neptune": "purple",
}

# Define the arrays to store the x,y,z positions of each planet
x_positions = np.zeros(len(planets))
y_positions = np.zeros(len(planets))
z_positions = np.zeros(len(planets))

# Define the date and time to retrieve the planet positions for (use UTC time)
date = "2023-04-07"
time = "12:00:00"

# Loop through each planet and retrieve its data from the API
for i, planet in enumerate(planets.keys()):
    response = requests.get(
        base_url,
        params={
            "id": planets[planet],
            "start_date": f"{date} {time}",
            "end_date": f"{date} {time}",
            "time_step": "1h",
            "units": "au",
            "velocity": "true",
            "api_key": "N3g6CYqWrbZh9FckuLinQQAUg6paaAKdhqNNaefG",  # Replace with your own API key
        },
    )
    data = response.json()["positions"][0]

    # Extract the x,y,z positions from the data
    x_positions[i] = float(data["x"])
    y_positions[i] = float(data["y"])
    z_positions[i] = float(data["z"])

# Create a 3D scatter plot of the positions of each planet
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
for i, planet in enumerate(planets.keys()):
    ax.scatter(
        x_positions[i],
        y_positions[i],
        z_positions[i],
        c=planet_colors[planet],
        label=planet,
    )
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Current Positions of the Planets ({date} {time} UTC)")
ax.legend()

plt.show()
