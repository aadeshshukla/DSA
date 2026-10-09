import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# XOR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])

# Build neural network
model = Sequential([
    Dense(8, input_shape=(2,), activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Evaluate predictions
predictions = model.predict(X, verbose=0)

for i in range(len(X)):
    print(X[i], "->", round(float(predictions[i][0])))
