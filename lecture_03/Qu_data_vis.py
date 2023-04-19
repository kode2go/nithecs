# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 07:45:36 2023

@author: BBarsch
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# url = 'https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv'

# df = pd.read_csv(url, header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Create a figure with two subplots
fig, ax = plt.subplots(ncols=2, figsize=(12, 6))

# Create a distribution plot for the 'sepal_width' column
sns.histplot(data=iris_df, x='sepal_width', ax=ax[0], kde=True)

# Create a bar plot for the count of each species
sns.countplot(data=iris_df, x='species', ax=ax[1])

# Set the title for each subplot
ax[0].set_title('Distribution of Sepal Width')
ax[1].set_title('Count of Species')

# Show the plot
plt.show()



# Load the iris dataset
iris_df = sns.load_dataset('iris')

# Create a pairplot to visualize relationships between different features
sns.pairplot(iris_df, hue='species')

# Show the plot
plt.show()
