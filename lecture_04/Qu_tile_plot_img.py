import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio

# Load data
df = pd.read_csv("data.txt", header=None, delim_whitespace=True, names=['column1', 'column2', 'column3', 'column4'])

# Create Matplotlib plot
sns.set(style="ticks")
sns_plot = sns.pairplot(df)

import plotly.express as px
from PIL import Image
import numpy as np

# Open image using Pillow
img = Image.open('plot.png')
# Convert to numpy array
img_array = np.array(img)
  
fig = px.imshow(img_array)

fig.write_html("plotly.html")