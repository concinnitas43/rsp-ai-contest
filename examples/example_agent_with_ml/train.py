import tensorflow as tf
import numpy as np
from ...classes.utils import *

import random

# Generate a long list of historical tuples
history_length = 1000  # Adjust the length as needed
history = [(random.choice(list(Hand)), random.choice(list(Hand))) for _ in range(history_length)]


# Mapping moves to numerical values
moves_map = {Hand.R: 0, Hand.P: 1, Hand.S: 2}

# Prepare data for training
X = np.array([[moves_map[player], moves_map[opponent]] for player, opponent in history])
y = np.array([moves_map[opponent] for _, opponent in history])

# Convert y to one-hot encoding
y_one_hot = tf.keras.utils.to_categorical(y, num_classes=3)

# Define a simple neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y_one_hot, epochs=50)

# Save the model to a file
model.save('rps_model_nn.h5')
