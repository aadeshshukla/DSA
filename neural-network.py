
import numpy as np

# XOR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Reproducible random initialization
np.random.seed(42)

# Network architecture: 2 input -> 4 hidden -> 1 output
input_neurons = 2
hidden_neurons = 4
output_neurons = 1

# Initialize weights and biases
W1 = np.random.randn(input_neurons, hidden_neurons)
b1 = np.zeros((1, hidden_neurons))

W2 = np.random.randn(hidden_neurons, output_neurons)
b2 = np.zeros((1, output_neurons))

# Activation functions
def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(a):
    return a * (1 - a)

# Training configuration
learning_rate = 0.5
epochs = 20000

# Training loop
for epoch in range(epochs):

    # Forward propagation
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    # Calculate binary cross-entropy loss
    eps = 1e-8
    loss = -np.mean(
        y * np.log(a2 + eps) +
        (1 - y) * np.log(1 - a2 + eps)
    )

    # Backpropagation
    dz2 = (a2 - y) / len(X)
    dW2 = np.dot(a1.T, dz2)
    db2 = np.sum(dz2, axis=0, keepdims=True)

    dz1 = np.dot(dz2, W2.T) * sigmoid_derivative(a1)
    dW1 = np.dot(X.T, dz1)
    db1 = np.sum(dz1, axis=0, keepdims=True)

    # Update parameters using gradient descent
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    if (epoch + 1) % 5000 == 0:
        print(f"Epoch {epoch + 1}, Loss: {loss:.6f}")

# Test the trained network
print("\nPredictions:")
predictions = sigmoid(
    sigmoid(np.dot(X, W1) + b1) @ W2 + b2
)

for inputs, prediction in zip(X, predictions):
    print(f"{inputs} -> {prediction[0]:.4f} "
          f"(class: {int(prediction[0] >= 0.5)})")
