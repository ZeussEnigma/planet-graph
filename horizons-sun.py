import requests

# Define the base URL of the Horizons API
base_url = 'https://ssd.jpl.nasa.gov/horizons_batch.cgi'

# Define the query parameters
params = {
    'batch': '1', # Retrieve one record
    'COMMAND': "'399'", # Specify the target object as the Sun
    'MAKE_EPHEM': "'YES'", # Make ephemeris
    'TABLE_TYPE': "'OBSERVER'", # Table type for the returned data
    'CENTER': "'500@10'", # Specify the observer location (in this case, Earth)
    'TIME_TYPE': "'UTC'", # Time type for the input time
    'START_TIME': "'2023-04-07'", # Start time for the ephemeris
    'STOP_TIME': "'2023-04-08'", # Stop time for the ephemeris
    'STEP_SIZE': "'1 d'", # Step size for the ephemeris
    'QUANTITIES': "'1,2,4,9,20,23'", # Quantities to return (x,y,z positions and velocities)
    'CSV_FORMAT': "'YES'" # Return the data in CSV format
}

# Send a GET request to the Horizons API with the query parameters
response = requests.get(base_url, params=params)

# Print the response content (which contains the ephemeris data in CSV format)
print(response.content.decode())
