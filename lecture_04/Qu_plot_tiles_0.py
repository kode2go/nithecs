# -*- coding: utf-8 -*-
"""

@author: BBarsch
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
# Create a pairplot using Seaborn


# df = pd.read_csv('data.txt', delimiter='\t')
df = pd.read_csv("data.txt", header=None, delim_whitespace=True,names=['column1', 'column2', 'column3', 'column4'])



fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

'''This will create a 2x2 grid of plots, with each plot comparing two columns of data from the DataFrame. You can customize the plot titles, axis labels, and formatting as needed.

Note that you'll need to replace filename.txt with the name of your text file, and column1, column2, column3, and column4 with the names of the columns containing the quantities you want to compare.'''

ax = axes.ravel()

ax[0].plot(df['column1'], df['column2'], 'o')
ax[0].set_title('column 1 vs  column 2')

ax[1].plot(df['column1'], df['column3'], 'o')
ax[1].set_title('column 1 vs  column 3')

ax[2].plot(df['column1'], df['column4'], 'o')
ax[2].set_title('column 1 vs  column 4')

ax[3].plot(df['column2'], df['column3'], 'o')
ax[3].set_title('column 2 vs  column 3')

plt.tight_layout()

sns.pairplot(df)

plt.show()



# Show the plot
plt.show()