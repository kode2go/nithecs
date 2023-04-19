# -*- coding: utf-8 -*-
"""

@author: BBarsch

Suppose we have two datasets: orders and customers. The orders dataset contains information about orders placed by customers, including the customer_id for each order. The customers dataset contains information about each customer, including the customer_id.

Our goal is to extract features from both datasets and combine them into a single DataFrame based on the customer_id. We can do this using the apply() function to create a new column in the orders dataset that contains the relevant customer information.

"""

import pandas as pd


# Load the orders and customers datasets
orders = pd.read_csv('orders.csv')
customers = pd.read_csv('customers.csv')

# Option 1

# Define a function to extract the customer name from the customers dataset
def get_customer_name(customer_id):
    customer = customers[customers['customer_id'] == customer_id]
    return customer['name'].values[0]

# Apply the function to the orders dataset to create a new column with the customer name
orders['customer_name'] = orders['customer_id'].apply(get_customer_name)

# View the updated orders dataset
print(orders.head())

# Option 2

# Merge the datasets based on the customer_id column
merged_data = pd.merge(orders, customers, on='customer_id')

# Extract the customer name from the merged dataset
orders['customer_name'] = merged_data['name']

# View the updated orders dataset
print(orders.head())
