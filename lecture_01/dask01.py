# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:36:24 2023

@author: BBarsch
"""


import pandas as pd
import time

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                  names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

numeric_cols = df.select_dtypes(include=['float64', 'int64'])
start = time.time()
means = numeric_cols.mean()
end = time.time()
print(f"Pandas took {end - start:.4f} seconds to compute the mean:\n{means}\n")


print(means)

import dask.dataframe as dd

ddf = dd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                  names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

numeric_cols = ddf.select_dtypes(include=['float64', 'int64'])
start = time.time()
means = numeric_cols.mean().compute()
end = time.time()
print(f"Dask took {end - start:.4f} seconds to compute the mean:\n{means}\n")
print(means)

