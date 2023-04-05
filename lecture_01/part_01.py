# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 2023

@author: BBarsch
"""

import pandas as pd
import numpy as np


# df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

df = pd.read_csv('iris.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])



sepal_len_s = df['sepal_length']
sepal_wid_s = df['sepal_width']
sepal_len_s[0]



# ndarry:

s1 = pd.Series(np.random.randn(5))
s2 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

# dict:
    
d = {"b": 1, "a": 0, "c": 2}

s3 = pd.Series(d)

## If an index is passed, the values in data corresponding to the labels in the index will be pulled out.

s4 = pd.Series(d, index=["b", "c", "d", "a"])

# scalar (index must be provided):
    
s5 = pd.Series(5.0, index=["a", "b", "c", "d", "e"])

    
df.head()

d_2 = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df_2 = pd.DataFrame(d_2)
df_2

df_3 = pd.DataFrame(d_2, index=["d", "b", "a"])
df_3

df_4 = pd.DataFrame(d_2, index=["d", "b", "a"], columns=["two", "three"])
df_4


df_4.index

df_4.columns



d_5 = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
df_5 = pd.DataFrame(d_5)
df_5


df["sepal_length"]
type(df["sepal_length"])
df["sepal_length"].values

# column names can be accessed like an attribute
df.sepal_length.values
type(df.sepal_length.values)
df[['sepal_length']]
type(df[['sepal_length']])

df["feature"] = df["sepal_length"] * df["sepal_width"]

df["flag"] = df["feature"] > 20

#Columns can be deleted
del df["feature"]

#insert scalar
df["tmp"] = 0.0

# insert a series:
df["tmp2"] = s1

# By default, columns get inserted at the end. DataFrame.insert() inserts at a particular location in the columns:
    
df.insert(1,"tmp3",s1)

# DataFrame has an assign() method that allows you to easily create new columns that are potentially derived from existing columns.

df.assign(sepal_ratio=df["sepal_width"] / df["sepal_length"]).head()

#...assign() always returns a copy of the data, leaving the original DataFrame untouched.


# Chaining commands

df.query("sepal_length > 5").assign(sepal_ratio=df["sepal_width"] / df["sepal_length"]).head()
    

# more on assign


dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

dfa.assign(C=lambda x: x["A"] + x["B"], D=lambda x: x["A"] + x["C"])

# In the second expression, x['C'] will refer to the newly created column, that’s equal to dfa['A'] + dfa['B'].


# Indexing/ Selection

# loc - row by label

df_3.loc["b"]

# iloc - row by integer location

df_3.iloc[1]


#Data alignment between DataFrame objects automatically align on both the columns and the index (row labels)

# Arithmetic operations with scalars operate element-wise


# Transpose

df[:5].T

# Most numpy functions can be called on pandas

