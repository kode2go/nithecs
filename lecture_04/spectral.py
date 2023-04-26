# -*- coding: utf-8 -*-
"""

@author: BBarsch

Using pandas for spectral data peak integration.
"""

import pandas as pd

# # Read spectral data file into a pandas DataFrame
df = pd.read_csv('data/spec.csv', header=None, names=['wavelength', 'absorbance'])

# from scipy.integrate import trapz

# # Select the subset of data within the desired wavelength limits
# subdf = df[(df['wavelength'] >= 210) & (df['wavelength'] <= 230)]

# # Integrate the absorbance values over the corresponding wavelength range
# area = trapz(df['absorbance'], df['wavelength'])

# # Print the integrated area
# print('Integrated area:', area)























# # Read spectral data file into a pandas DataFrame
# df = pd.read_csv('data/spec.csv', skiprows=1,header=None, names=['wavelength', 'absorbance'])

# # Convert the 'wavelength' and 'absorbance' columns to float type
# df['wavelength'] = df['wavelength'].astype(float)
# df['absorbance'] = df['absorbance'].astype(float)