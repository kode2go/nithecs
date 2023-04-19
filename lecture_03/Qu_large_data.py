# -*- coding: utf-8 -*-
"""


@author: BBarsch


    - Using large data set ( size > 2 GB). How to be mindful of optimised code / how to avoid redundant code. What are computationally intensive/costly functions to be aware of?:
        
        

        
- When working with large datasets (size > 2 GB) in Pandas, it is important to be mindful of the performance of your code and to avoid redundant operations. Here are some tips to help optimize your code:

- Use the dtype parameter: When reading in a large dataset, consider specifying the data types of the columns using the dtype parameter. This can reduce memory usage and speed up data processing.

- Use chunking: Instead of reading in the entire dataset at once, consider reading the data in chunks using the chunksize parameter of the read_csv or read_table functions. This can help reduce memory usage and improve performance.

- Use vectorized operations: Pandas has built-in functions for many common operations, such as arithmetic operations, string operations, and date/time operations. These functions are optimized for performance and can be much faster than looping over rows of data.

- Use the apply method sparingly: The apply method can be useful for applying a function to each row or column of a dataset. However, it can be computationally expensive and should be used sparingly.

- Use indexing: If you need to perform frequent lookups or filtering operations on the dataset, consider using indexing to speed up these operations. Indexing can help reduce the amount of data that needs to be processed, improving performance.

- Use groupby and agg instead of apply: If you need to perform a calculation on a grouped dataset, consider using the groupby and agg functions instead of apply. These functions are optimized for performance and can be much faster than using apply.

- Avoid redundant calculations: If you need to perform a calculation multiple times, consider storing the result in a variable rather than recalculating it each time. This can help reduce computation time and improve performance.

- Be mindful of computationally intensive functions: Certain functions can be computationally intensive and can slow down your code significantly when working with large datasets. For example, sorting and grouping operations can be costly. Be aware of these functions and use them judiciously.

- Use parallel processing: If your machine has multiple cores, consider using parallel processing to speed up computation. This involves breaking up the dataset into smaller chunks and processing each chunk on a separate core. This can significantly reduce computation time for computationally intensive tasks.

- By following these tips, you can optimize your code and improve performance when working with large datasets in Pandas. 


__________________________________________________


The definition of "large data" or "big data" can vary depending on the context and the specific industry or field. In general, large data refers to data sets that are too large and complex to be processed and analyzed using traditional data processing tools and techniques.

The size of a large data set can range from a few terabytes to many petabytes or even exabytes. Large data sets often contain both structured and unstructured data, such as text, images, video, and sensor data. The volume, variety, and velocity of large data sets can pose significant challenges for data processing, storage, and analysis.

In addition to the size of the data set, other factors that contribute to the complexity of large data include the need for real-time processing, the need to process data from multiple sources, and the need to analyze data in near-real-time to make decisions.

Some examples of industries that deal with large data include finance, healthcare, e-commerce, social media, and scientific research. In these industries, large data sets are often used to gain insights into customer behavior, identify trends and patterns, and develop predictive models to inform business decisions.

In summary, large data refers to data sets that are too large and complex to be processed and analyzed using traditional data processing tools and techniques. The size of a large data set can range from a few terabytes to many petabytes or even exabytes, and the complexity of the data can pose significant challenges for processing, storage, and analysis.

Pandas can be used for processing and analyzing large data sets. However, pandas performance may be slower on large data sets due to its memory constraints. Pandas is a popular open-source library for data manipulation and analysis in Python, and it is designed to work with data sets that can fit into memory.

To overcome the memory constraints of pandas and work with larger data sets, several approaches can be used, such as:

Chunking: By breaking the data set into smaller chunks, you can process and analyze them one at a time, rather than loading the entire data set into memory at once. The pandas read_csv() function allows you to read in data in chunks.

Sampling: If you don't need to work with the entire data set, you can take a representative sample to perform your analysis.

Distributed computing: You can also use distributed computing frameworks, such as Apache Spark, to process and analyze large data sets. Pandas can be integrated with Spark to leverage the distributed computing capabilities of Spark.

Overall, pandas is a powerful tool for data manipulation and analysis, but it may not be the best choice for extremely large data sets. When working with large data sets, it's important to consider alternative approaches such as chunking, sampling, or distributed computing.


__________________________________________________


https://pandas.pydata.org/docs/user_guide/scale.html

https://pandas.pydata.org/docs/user_guide/basics.html#accelerated-operations



Pandas Parquet refers to the support for reading and writing Parquet files in the Pandas library. Parquet is a columnar storage file format that is commonly used in big data processing frameworks such as Apache Spark and Apache Hadoop. It is designed to be efficient for both reading and writing large datasets, particularly when dealing with complex data structures.

Pandas provides support for reading and writing Parquet files using the read_parquet() and to_parquet() functions. These functions allow Pandas users to work with Parquet files directly from within the Pandas data analysis workflow, without the need for additional tools or libraries.

When reading a Parquet file with Pandas, the data is loaded into a Pandas DataFrame object, which provides a familiar interface for manipulating and analyzing the data. Similarly, when writing data to a Parquet file with Pandas, the data is first converted to a Parquet file format and then written to disk.

Overall, Pandas Parquet support provides a convenient and efficient way for Pandas users to work with Parquet files, which are commonly used in big data processing workflows.

"""

