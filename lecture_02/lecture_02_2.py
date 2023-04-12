# -*- coding: utf-8 -*-
"""
@author: BBarsch

"""

# https://pandas.pydata.org/docs/user_guide/merging.html

#---------------Combine files / Concatenate ------------------#
# NB REMEMBER TO EXTRACT THE data.zip folder and person.zip folder


file_path = '.\\data\\'

# glob is an alternative to using os.listdir
import os
import pandas as pd
file_list = os.listdir(file_path)
# file_list = os.listdir('.\\data')
print(file_list)

# # empty df
df = pd.DataFrame()

# note how file is the iterator
for file in file_list:
    # skip "person_joined.csv" file
    if file == "person_joined.csv":
        continue
    # df_temp = pd.read_csv(file)
    print(file_path+file)
    df_temp = pd.read_csv(file_path+file)
    # df = df.concat(df_temp,ignore_index=True)
    df = pd.concat([df, df_temp])
    
## ?? If you have a list of files and you only want to select specific ones?
    
print(df)

# # reset the index and drop the old index column
df = df.set_index('id')

# print(df)

# export to csv file in data folder
df.to_csv(file_path+"person_joined.csv")

# #---------------Merge files------------------#

file_path2 = '.\\persons\\'

df1 = pd.read_csv(file_path2+'person_education.csv')
df2 = pd.read_csv(file_path2+'person_work.csv')

# # inner join
df_merge = pd.merge(df1,df2,on='id')

df_merge = df_merge.set_index('id')

df_merge.to_csv(file_path2+'person_merged.csv')

df_merge_filtered = df_merge[['University','Company Name']]



"""
An inner join returns only the rows where there is a match in 
both dataframes on the specified "on" column (in this case, the "id" 
                                              column). 
If there is no match, the row is excluded from the result.

merged_df = pd.merge(df1, df2, on='id', how='outer')

Inner join: Returns only the rows where there is a match 
in both dataframes on the specified "on" column.

Outer join: Returns all the rows from both dataframes. 
If there is no match for a row in either dataframe, 
the missing values will be filled with NaNs.

Left and Right Joins are possible too

"""

# df_big = pd.read_csv('big_data_01.csv')

# df_big = pd.read_csv('big_data_mil.csv')

# df_big1 = pd.read_csv('big_data_mil.csv')

# df_big2 = pd.read_csv('big_data_mil.csv')

# df_big3 = pd.read_csv('big_data_mil.csv')

# df_big4 = pd.read_csv('big_data_mil.csv')

# df_big5 = pd.read_csv('big_data_mil.csv')

# df_big6 = pd.read_csv('big_data_mil.csv')

# df_big7 = pd.read_csv('big_data_mil.csv')


"""
The number of rows of data that can be read into pandas on a 16GB RAM laptop depends on various factors such as the size of each row, the number of columns, the data type of the columns, and the available memory usage during the read operation.

A 16GB RAM laptop can typically handle reading in datasets of several million rows with moderate memory usage optimizations, assuming that there are no other memory-intensive processes running on the machine. It is always a good practice to monitor the memory usage during the read operation and optimize the read process accordingly.

To optimize memory usage during data read operations in pandas, you can use techniques such as:

Use the dtype parameter in the read_csv() or read_parquet() functions to specify the data type of each column explicitly.

Use the usecols parameter in the read_csv() function to read only a subset of columns from the dataset.

Use the chunksize parameter in the read_csv() or read_parquet() functions to read in the dataset in chunks and process each chunk separately.

Use the low_memory parameter in the read_csv() function to minimize the memory usage when the CSV file has mixed data types.

Optimize the data storage format by using a compressed format such as gzip or bzip2 for CSV files or using Parquet or Arrow format for columnar data.


"""

## Profile Reporting
# from ydata_profiling import ProfileReport
# profile = ProfileReport(df, title="Profiling Report")
# profile.to_file("your_report.html")

# import subprocess
# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))

# # html_file = 'C:\\Users\\BBarsch.CSIR\\.spyder-py3\\your_report.html'
# html_file = 'your_report.html'
# # Combine the script directory with the relative path to the HTML file
# html_path = os.path.join(script_dir, html_file)

# # html_file = 'your_report.html'
# firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# subprocess.run([firefox_path, html_path])



