# -*- coding: utf-8 -*-
"""
@author: BBarsch

There are several popular machine learning libraries that can be used with pandas to build and train models. Here are a few examples:

Scikit-learn: Scikit-learn is a popular open-source library for classical machine learning in Python. It provides various modules for classification, regression, clustering, and dimensionality reduction. Scikit-learn can be used with pandas to preprocess data and train machine learning models.

TensorFlow: TensorFlow is an open-source machine learning library developed by Google. It provides a powerful API for building and training deep learning models. TensorFlow can be used with pandas to preprocess data and train deep learning models.

Keras: Keras is a high-level neural networks API written in Python. It is built on top of TensorFlow and provides a simple and intuitive API for building and training deep learning models. Keras can be used with pandas to preprocess data and train deep learning models.

**Note: scikit-learn is generally considered the easiest to learn and use, followed by Keras and then TensorFlow and PyTorch. Tensorflow and PyTorch are fully customizable for custom models and perform low-level operations. However, this flexibility can make it more difficult to learn and use compared to libraries like scikit-learn.**

PyTorch: PyTorch is an open-source machine learning library developed by Facebook. It provides a powerful API for building and training deep learning models. PyTorch can be used with pandas to preprocess data and train deep learning models. It is known for its dynamic computation graph, which makes it easier to build and debug complex models. PyTorch is highly flexible and allows you to build custom models and perform low-level operations. 

XGBoost: XGBoost is a popular open-source library for gradient boosting in Python. It provides a fast and efficient implementation of the gradient boosting algorithm, which is a powerful technique for building and training machine learning models. XGBoost can be used with pandas to preprocess data and train gradient boosting models.
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

import pandas as pd

# Load the iris dataset
iris = load_iris()

# Convert the dataset to a pandas DataFrame
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris_df, iris.target, test_size=0.2)

# Train a decision tree classifier on the training data
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Evaluate the accuracy of the classifier on the testing data
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)