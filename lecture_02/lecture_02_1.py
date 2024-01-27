# -*- coding: utf-8 -*-
"""
@author: BBarsch

Lecture 2 - 12 April @ 14:00

Agenda:
    1. Admin - Github Repo, Discussions, Form 2
        https://forms.office.com/r/ML2AjGd3eX
    2. Review of lecture 1
    3. Input/Output
    4. Data wrangling, aggregation, merging, joining 


"""

# 1. Admin - Github Repo, Discussions, Form 2, Setup Pandas

"""
How should you learn from these lectures???


Online Browser
https://trinket.io/embed/python3

Install Anaconda:
    
Windows:
https://www.youtube.com/watch?v=WUeBzT43JyY


Mac:
https://youtu.be/n83J8cBytus

Linux
https://youtu.be/dGm10q_y3xw


- Python Community - PyConZA

"""

# 2. Review of lecture 1

import pandas as pd

url = 'https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv'

df = pd.read_csv(url, header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# df = pd.read_csv('iris.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# file_path = 'c://users//username//folder//'

# df.to_csv(file_path+'dummy_data.csv')

# df.to_csv('./newfolder/dummy_data.csv')

df["sepal_length"]
type(df["sepal_length"])
type(df["sepal_length"].values)

# Chaining commands

df.query("sepal_length > 5").assign(sepal_ratio=df["sepal_width"] / df["sepal_length"]).head()
    

# more on assign
dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

dfa = dfa.assign(C=lambda x: x["A"] + x["B"], D=lambda x: x["A"] + x["C"])

# column names can be accessed like an attribute

df.sepal_length.values
type(df.sepal_length.values)

df[['sepal_length']]
type(df[['sepal_length']])

df["feature"] = df["sepal_length"] * df["sepal_width"]

df["flag"] = df["feature"] > 20

# 3. Input/Output

# https://pandas.pydata.org/docs/user_guide/io.html

# https://pandas.pydata.org/docs/reference/io.html

## csv

# see above...

## xlsx

df_xlsx = pd.read_excel('iris.xlsx')

## txt

df_txt = pd.read_csv('iris_txt.txt',delimiter='\t')

## sql

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="xx",
    user="xx",
    password="xx"
)

# Query the database for all data in a table
query = "SELECT * FROM project"
df_sql = pd.read_sql(query, conn)

# Display the resulting DataFrame
print(df_sql)

## HDF

df_hdf = pd.DataFrame([[1, 1.0, 'a']], columns=['x', 'y', 'z'])  
df_hdf.to_hdf('./store.h5', 'data')  
reread = pd.read_hdf('./store.h5')  

# 4. Data wrangling, aggregation, 

"""
This process typically involves several steps, such as removing duplicates, handling missing values, correcting data types, converting data formats, and merging or joining data sets.
"""

## Missing Data, Cleaning

df_med = pd.read_csv('med_data.csv')

df_med_cp = df_med


"""
Now you will notice the following:

The data set has an index column that is redundant
The data set contains some empty cells or NaNs (“Date” in row 22, and “Calories” in row 18 and 28, “Maxpulse” in row 1).
The data set contains wrong format (“Date” in row 26).
The data set contains wrong data (“Duration” in row 7 and 13).
The data set contains duplicates (row 11 and 12).
"""


# Now the index column is redundant and we do not need it. We can remove it with drop method in the following way:
df_med.drop(['Index'],inplace=True,axis=1)

"""
If you want to change the original DataFrame, use the inplace = True argument. The dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame. You will also need to reset the index with df.reset_index(drop=True) as if you remove a row, the row numbers will not be consecutive - df = df.reset_index(drop=True)
"""

# Replace Empty Values – Using fillna
## https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html

"""
Before removing rows completely because of a NaN, it is better to try to first modify to work with the data. So we can insert a new value instead. This way you do not have to delete entire rows just because of some empty cells as the other columns may have useful data. The fillna() method allows us to replace empty cells with a value. A common way to replace empty cells, is to calculate the mean (average), median (middle) or mode (most frequent) value of the column. Pandas uses the mean(), median() and mode() methods to calculate the respective values for a specified column:
"""

x = df_med["Calories"].mean()

df_med["Calories"].fillna(x, inplace = True) 


# Drop NANs and Wrong Date Format

"""
Cells with data of wrong format can make it difficult, or even impossible, to analyze data. To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format. In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the ‘Date’ column should be a string that represents a date. The best way to fix the date is to convert it a versatile date time format unique to Pandas using to_datetime():
"""

df_med['Date'] = pd.to_datetime(df_med['Date'])

df_med.dropna(inplace = True)

df_med = df_med.reset_index(drop=True)

# Incorrect values

"""
“Wrong data” does not have to be “empty cells” or “wrong format”, it can just be wrong, like if someone registered “199” instead of “1.99”. Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be. If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.

It doesn’t have to be wrong, but taking in consideration that this is the data set of someone’s workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

One way to fix wrong values is to replace them with something else.

In our example, it is most likely a typo, and the value should be “45” instead of “450”, and we could just insert “45” in row 7 with
"""

df_med.loc[7,'Duration'] = 45

"""
To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries. And remove the rows that contains wrong data above a certain threshold. Loop through all values in the “Duration” column.

If the value is higher than 120, remove the rows or if it is above 100 set to 100:
"""

for x in df_med.index:
    if df_med.loc[x, "Calories"] > 350:
        df_med.loc[x, "Calories"] = 350
        
        
# Remove duplicates

"""
Duplicate rows are rows that have been registered more than one time. By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
"""

df_med.drop_duplicates(inplace = True)

df_med = df_med.reset_index(drop=True)


# Filtering and grouping

# filter_sepal_length = df["sepal_length"] > 5
# df[filter_sepal_length]
# df.loc[filter_sepal_length,["sepal_width","species"]]

# Grouping and Aggregation

"""
By “group by” we are referring to a process involving one or more of the following steps:

    Splitting the data into groups based on some criteria.

    Applying a function to each group independently.

    Combining the results into a data structure.

"""

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html


"""
An aggregation is a GroupBy operation that reduces the dimension of the grouping object. The result of an aggregation is, or at least is treated as, a scalar value for each column in a group. 

max, mean, any, min, quantile, sum, std
"""

print("groupby agg")
print(df.groupby("class").mean())
print(df.groupby("class")[["sepal_length","sepal_width"]].mean())

"""
The aggregate() method can accept many different types of inputs. This section details using string aliases for various GroupBy methods; other inputs are detailed in the sections below.
"""

print(df.groupby("class").aggregate("sum"))

print(df.groupby("class").agg(["sum", "mean", "std"]))

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 32, 18, 47],
        'Height': [5.6, 6.1, 5.5, 6.2]}

df_data = pd.DataFrame(data)
df_data_2 = df_data

df_data = df_data.groupby('Height').agg({'Age': ['mean', 'max']})
print(df_data)

df_data_2 = df_data_2['Age'].apply(lambda x: x**2)
print(df_data_2)

"""
A transformation is a GroupBy operation whose result is indexed the same as the one being grouped. Common examples include cumsum() and diff().
"""



# Plotting:
# https://www.python-graph-gallery.com/25-histogram-with-several-variables-seaborn
# libraries & dataset

import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset("iris")

sns.histplot(data=df, x="sepal_length", color="skyblue", label="Sepal Length", kde=True)
sns.histplot(data=df, x="sepal_width", color="red", label="Sepal Width", kde=True)

plt.legend() 
plt.show()




## Profile Reporting
# from ydata_profiling import ProfileReport
# profile = ProfileReport(df_med, title="Profiling Report")
# profile.to_file("your_report.html")

# import subprocess
# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)

# # html_file = 'C:\\Users\\BBarsch.CSIR\\.spyder-py3\\your_report.html'
# html_file = 'your_report.html'
# # Combine the script directory with the relative path to the HTML file
# html_path = os.path.join(script_dir, html_file)

# # html_file = 'your_report.html'
# firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# subprocess.run([firefox_path, html_path])
