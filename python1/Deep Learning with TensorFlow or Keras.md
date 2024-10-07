## [[Deep Learning with TensorFlow or Keras]]

### Overview
Deep learning is a subset of machine learning that deals with artificial neural networks. It is used to solve complex problems such as image recognition, natural language processing, and speech recognition. TensorFlow and Keras are two popular Python libraries for deep learning. TensorFlow is a low-level library that gives you more control over the training process, while Keras is a higher-level library that simplifies the process.

### Using TensorFlow
#### Creating and Training a Model
- TensorFlow uses a tensor (multidimensional data array) as the basic data structure.
- To create a model, you define the network architecture using the `tf.keras.Sequential` class.
- You can add layers to the model using methods like `add`, `dense`, and `conv2d`.
- To train the model, you use the `compile` method to specify the loss function, optimizer, and metrics to track.
- You then use the `fit` method to train the model on your data.

```python
# Import TensorFlow and create a model
import tensorflow as tf
model = tf.keras.Sequential()

# Add layers to the model
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
 loss='sparse_categorical_crossentropy',
 metrics=['accuracy'])

# Train the model
model.fit(data, labels, epochs=10)
```

#### Evaluation and Inference
- After training, you can evaluate the model's performance using the `evaluate` method.
- To make predictions, you use the `predict` method.

```python
# Evaluate the model
results = model.evaluate(test_data, test_labels)

# Make predictions
predictions = model.predict(new_data)
```

### Using Keras
#### Creating and Training a Model
- Keras simplifies the process of creating and training models by providing high-level APIs.
- You can use the `tf.keras.Sequential` class to create a model and add layers.
- You can also use pre-trained models from the Keras Applications library.
- To train a model, you use the `compile` and `fit` methods similar to TensorFlow.

```python
# Import Keras and create a model
import tensorflow.keras as keras
model = keras.Sequential()

# Add layers to the model
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
 loss='sparse_categorical_crossentropy',
 metrics=['accuracy'])

# Train the model
model.fit(data, labels, epochs=10)
```

#### Evaluation and Inference
- Evaluation and inference in Keras are similar to TensorFlow.
- You can use the `evaluate` and `predict` methods to assess the model's performance and make predictions.

```python
# Evaluate the model
results = model.evaluate(test_data, test_labels)

# Make predictions
predictions = model.predict(new_data)
```

### Related Python Concepts
- [[Libraries like NumPy]]: NumPy is used for numerical operations and multidimensional data manipulation in deep learning.
- [[Lists]]: [[Lists]] are used to represent sequences of data in deep learning models.
- [[Dictionaries]]: [[Dictionaries]] are used to store and retrieve data by keys in deep learning models.
- [[Functions]]: [[Functions]] are used to create custom layers and training methods in deep learning.
- [[Lambda [[Functions]]: Lambda functions are used to create anonymous functions that can be used as layers or training callbacks in deep learning.
# [[Python 1 Home]]