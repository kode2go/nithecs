# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:48:13 2023

@author: BBarsch
"""

# https://github.com/ydataai/ydata-profiling
# https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/custom_report_appearance.html
# store on github: # https://github.com/kode2go/nithecs/tree/main/nithecs



import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

import subprocess
import os

import streamlit as st

from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide")

iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())

profile = ProfileReport(iris, title="Profiling Report",dark_mode=True)

st.title("Pandas Profiling in Streamlit!")

st.write(iris)

st_profile_report(profile)


