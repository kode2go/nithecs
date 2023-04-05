# https://github.com/ydataai/ydata-profiling
# https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/custom_report_appearance.html
# store on github: https://github.com/kode2go/nithecs/tree/main/nithecs

import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

import seaborn as sns
import matplotlib.pyplot as plt

import subprocess
import os

iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())

# sns.pairplot(iris, hue='class', height=2.5)
# plt.show()
from IPython.display import Image
from io import BytesIO
# Save the plot to a file or buffer
sns.pairplot(iris, hue='class', height=2.5)
plot_buffer = BytesIO()
plt.savefig(plot_buffer, format='png')
plot_buffer.seek(0)

import base64
report = ProfileReport(iris, title="Profiling Report", explorative=True, html={'style':{'full_width':True}},dark_mode=True)
report_html = report.to_html()
report_html += f'<div style="text-align:center"><h2>Pairplot</h2><br><img src="data:image/png;base64,{base64.b64encode(plot_buffer.getvalue()).decode()}" /><br></div>'

with open("your_report_iris.html", "w") as f:
    f.write(report_html)

# profile = ProfileReport(iris, title="Profiling Report",dark_mode=True)

# report_html.to_file("your_report_iris.html")

script_dir = os.path.dirname(os.path.abspath(__file__))

html_file = 'your_report_iris.html'

html_path = os.path.join(script_dir, html_file)

firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

subprocess.run([firefox_path, html_path])

