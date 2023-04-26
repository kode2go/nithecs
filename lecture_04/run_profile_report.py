# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:08:18 2023

@author: BBarsch
"""

import pandas as pd
from ydata_profiling import ProfileReport
import subprocess
import os


def generate_profile_report(df):
    # Generate the profiling report
    profile = ProfileReport(df, title="Profiling Report")

    # Save the report to a file
    profile.to_file("your_report.html")

    # Get the path to the HTML file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = 'your_report.html'
    html_path = os.path.join(script_dir, html_file)

    # Open the report in the browser
    firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    subprocess.run([firefox_path, html_path])