# https://github.com/ydataai/ydata-profiling

import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

profile = ProfileReport(df, title="Profiling Report")

profile.to_file("your_report.html")

import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# html_file = 'C:\\Users\\BBarsch.CSIR\\.spyder-py3\\your_report.html'
html_file = 'your_report.html'
# Combine the script directory with the relative path to the HTML file
html_path = os.path.join(script_dir, html_file)

# html_file = 'your_report.html'
firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

subprocess.run([firefox_path, html_path])


