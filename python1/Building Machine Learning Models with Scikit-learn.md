## [[Building Machine Learning Models with Scikit-learn]]

### Introduction
Scikit-learn is a comprehensive Python library for machine learning. It provides a wide range of supervised and unsupervised learning algorithms, making it easy to build and evaluate machine learning models.

### How to Use Scikit-learn

#### Importing the Library and Loading Data
```python
from sklearn import datasets
iris = datasets.load_iris()
```

#### Creating a Model
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
```

#### Training the Model
```python
model.fit(iris.data, iris.target)
```

#### Making Predictions
```python
predictions = model.predict(iris.data)
```

#### Evaluating the Model
```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(iris.target, predictions)
```

### Other Python Concepts Related to Scikit-learn

- [[Variables and Data Types]]: Scikit-learn uses NumPy arrays for storing and manipulating data.
- [[Functions]]: Scikit-learn provides various functions for building, training, and evaluating models.
- [[Modules and Packages]]: Scikit-learn is organized into modules, making it easy to import specific functionality.
- [[Libraries like NumPy]]: Scikit-learn relies on NumPy for numerical operations.
- [[Libraries like Pandas]]: Pandas can be used for data pre-processing before using Scikit-learn.
# [[Python 1 Home]]