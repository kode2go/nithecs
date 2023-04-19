# -*- coding: utf-8 -*-
"""

@author: BBarsch

Question:
    
    How does one combine two sets of data that is in date time format. The one starting sooner and the second ending later with some overlap in dates. How does one combine this without creating duplicates? or will you have to combine and deal with duplicates thereafter? The datasets are rather large so avoiding duplicates from the start would be preferable...
    
    
Answer:
    
    
To combine two sets of data in pandas that are in datetime format and have some overlap in dates without creating duplicates, you can use the merge function. Here's how:

Ensure that the two datasets have a common column that can be used for merging. In this case, it would be the datetime column.

Load the two datasets into separate pandas dataframes, with the datetime column as the index.

Use the merge function to combine the two dataframes. Set the how parameter to "outer" to ensure that all rows from both dataframes are included, and set the suffixes parameter to unique suffixes to avoid column name conflicts.

To remove duplicates, you can use the drop_duplicates function. You can specify the subset of columns that should be checked

"""

import pandas as pd

# Load the first dataset into a pandas dataframe
df1 = pd.read_csv('dataset1.csv', parse_dates=['datetime'])

# Load the second dataset into a pandas dataframe
df2 = pd.read_csv('dataset2.csv', parse_dates=['datetime'])

# Merge the two dataframes on the datetime index, with an outer join to include all rows
merged_df = pd.merge(df1, df2, how='outer', suffixes=('_1', '_2'))

# drop duplicates based only on the datetime, value_1, and value_2 columns, you can modify the drop_duplicates method to only include those columns:

# Step 1
mask = merged_df['value_1'] != merged_df['value_2']

# Step 2
merged_df_filtered = merged_df[mask]

# Step 3
merged_df_dropped_dup = merged_df_filtered.drop_duplicates(subset=['datetime', 'value_1', 'value_2'], keep=False)
    
    
# merged_df_dropped_dup = merged_df[merged_df['value_1'] != merged_df['value_2']].drop_duplicates(subset=['datetime', 'value_1', 'value_2'], keep=False)



