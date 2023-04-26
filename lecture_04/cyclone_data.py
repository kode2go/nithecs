# -*- coding: utf-8 -*-
"""

@author: BBarsch
"""

import pandas as pd
import numpy as np


# Create dummy cyclone data
dates = pd.date_range(start='2022-01-01', periods=200, freq='D')
latitudes = np.random.uniform(low=-30, high=30, size=200)
longitudes = np.random.uniform(low=50, high=120, size=200)
intensities = np.random.randint(low=1, high=5, size=200)
cyclone_data = {'Date': dates, 'Latitude': latitudes, 'Longitude': longitudes, 'Intensity': intensities}
df = pd.DataFrame(cyclone_data)

# Display the first few rows of the DataFrame
print(df.head())

import matplotlib.pyplot as plt

# Create time series plot of cyclone intensity
plt.figure()
plt.plot(df['Date'], df['Intensity'], '-o')
plt.xlabel('Date')
plt.ylabel('Cyclone Intensity')
plt.title('Cyclone Intensity Over Time')

# Create multiple variable plot of cyclone location and intensity
plt.figure()
plt.scatter(df['Longitude'], df['Latitude'], s=df['Intensity']*10, c=df['Intensity'], cmap='Blues')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Cyclone Location and Intensity')
plt.colorbar()

plt.show()