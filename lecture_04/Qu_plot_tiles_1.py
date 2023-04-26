import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "browser"

# Load data from text file into a pandas DataFrame
df = pd.read_csv("data.txt", header=None, delim_whitespace=True, names=['column1', 'column2', 'column3', 'column4'])

# Create four comparison plots using Plotly
fig = make_subplots(rows=2, cols=2, subplot_titles=("column 1 vs. column 2", "column 1 vs. column 3", "column 1 vs. column 4", "column 2 vs. column 3"))

fig.add_trace(go.Scatter(x=df['column1'], y=df['column2'], mode='markers'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['column1'], y=df['column3'], mode='markers'), row=1, col=2)
fig.add_trace(go.Scatter(x=df['column1'], y=df['column4'], mode='markers'), row=2, col=1)
fig.add_trace(go.Scatter(x=df['column2'], y=df['column3'], mode='markers'), row=2, col=2)


fig.update_layout(title="Four-tile plot", height=600, width=800)
fig.show()

fig.write_html("plot.html", auto_open=True)


