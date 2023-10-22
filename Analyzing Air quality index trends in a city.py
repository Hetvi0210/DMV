#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
# Task 1: Import the dataset
data = pd.read_csv("City_Air_Quality.csv")
# Task 2: Explore the dataset
print(data.head()) # Display the first few rows to understand the data structure
# Task 3: Identify relevant variables
date_column = "date"
aqi_column = "AQI"
pollutants = ["PM2.5", "PM10", "CO"]
# Task 4: Create a line plot for overall AQI trend
plt.figure(figsize=(12, 6))
plt.plot(data[date_column], data[aqi_column], label="AQI", color='b')
plt.xlabel("Date")
plt.ylabel("AQI")
plt.title("AQI Trend Over Time")
plt.legend()
plt.show()
# Task 5: Create line plots for individual pollutants
plt.figure(figsize=(12, 6))
for pollutant in pollutants:
 plt.plot(data[date_column], data[pollutant], label=pollutant)
plt.xlabel("Date")
plt.ylabel("Pollutant Level")
plt.title("Pollutant Trends Over Time")
plt.legend()
plt.show()
# Task 6: Use bar plots to compare AQI values across dates
plt.figure(figsize=(12, 6))
plt.bar(data[date_column], data[aqi_column], label="AQI")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.title("AQI Comparison Across Dates")
plt.xticks(rotation=45)
plt.legend()
plt.show()
# Task 7: Create box plots to analyze AQI value distribution
plt.figure(figsize=(10, 6))
plt.boxplot([data[pollutant] for pollutant in pollutants], labels=pollutants)
plt.xlabel("Pollutants")
plt.ylabel("AQI Values")
plt.title("AQI Value Distribution")
plt.show()
# Task 8: Create scatter plots to explore relationships
plt.figure(figsize=(10, 6))
plt.scatter(data["PM2.5"], data[aqi_column], label="PM2.5", alpha=0.5)
plt.scatter(data["PM10"], data[aqi_column], label="PM10", alpha=0.5)
plt.scatter(data["CO"], data[aqi_column], label="CO", alpha=0.5)
plt.xlabel("Pollutant Levels")
plt.ylabel("AQI")
plt.title("Scatter Plot of AQI vs Pollutant Levels")
plt.legend()
plt.show()
# Task 9: Customize visualizations
# You can customize each plot by adding labels, titles, legends, colors, and more.
# Save figures as image files (optional)
# plt.savefig("aqi_plots.png")

