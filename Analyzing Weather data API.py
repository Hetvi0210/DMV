#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import datetime
# Set your OpenWeatherMap API key
api_key = 'fb365aa6104829b44455572365ff3b4e'
lat = 18.184135
lon = 74.610764
# Construct the API URL
api_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
# Send a GET request to the API
response = requests.get(api_url)
# Check if the request was successful
if response.status_code == 200:
    weather_data = response.json()
    # Extract relevant weather information
    timestamps = [pd.to_datetime(item['dt'], unit='s') for item in weather_data['list']]
    temperatures = [item['main']['temp'] - 273.15 for item in weather_data['list']]
    humidity = [item['main']['humidity'] for item in weather_data['list']]
    wind_speed = [item['wind']['speed'] for item in weather_data['list']]
    weather_description = [item['weather'][0]['description'] for item in weather_data['list']]
    
    # Create a pandas DataFrame with the extracted weather data
    weather_df = pd.DataFrame({
        'Timestamp': timestamps,
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidity,
        'Wind Speed (m/s)': wind_speed,
        'Weather Description': weather_description
    })
    # Set the Timestamp column as the DataFrame's index
    weather_df.set_index('Timestamp', inplace=True)
    # Calculate max and min temperatures
    max_temp = weather_df['Temperature (°C)'].max()
    min_temp = weather_df['Temperature (°C)'].min()
    # Handling missing values (fillna) and inconsistent format
    weather_df.fillna(0, inplace=True)  # Replace missing values with 0 or appropriate value    
    # Print the weather data
    print(weather_df)    
    # Print max and min temperatures
    print(f"Max Temperature: {max_temp}°C")
    print(f"Min Temperature: {min_temp}°C")
else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")


# In[ ]:




