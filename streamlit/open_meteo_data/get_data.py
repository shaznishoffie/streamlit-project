import openmeteo_requests
import requests_cache
import pandas as pd
import polars as pl
from retry_requests import retry

#setup the Open Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 60)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# url of open-meteo
url = "https://api.open-meteo.com/v1/forecast"

# Starting coordinates
latitude = 1.240
longitude = 103.645

# create empty dataframe
results = pd.DataFrame(columns=[
    'date', 
    'temperature_2m', 
    'precipitation_probability', 
    'precipitation',
    'latitude',
    'longitude'
])

# Loop through the coordinates and get response from API
while latitude < 1.500:
    while longitude < 104.000:
        params = {
            "latitude" : latitude,
            "longitude" : longitude,
            "hourly" : [
                "temperature_2m", 
                "precipitation_probability", 
                "precipitation"
            ]
        }

        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]

        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")

        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        hourly_data = {"date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )}
        hourly_data["temperature_2m"] = hourly.Variables(0).ValuesAsNumpy()
        hourly_data["precipitation_probability"] = hourly.Variables(1).ValuesAsNumpy()
        hourly_data["precipitation"] = hourly.Variables(2).ValuesAsNumpy()
        hourly_data["latitude"] = response.Latitude()
        hourly_data["longitude"] = response.Longitude()

        hourly_dataframe = pd.DataFrame(data = hourly_data)
        print(hourly_dataframe.head(5))
        results = pd.concat([hourly_dataframe, results], axis=0)

        longitude += 0.125
    latitude += 0.125

print(results)
results.to_csv('data.csv', index=False)
