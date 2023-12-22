from classes.agent import Agent
from classes.utils import *

import tensorflow as tf
import numpy as np

# Function to load the model
def load_model(model_path):
    return tf.keras.models.load_model(model_path)

# Function to predict next move based on history
def predict_next_move(model, history):
    moves_map = {Hand.R: 0, Hand.P: 1, Hand.S: 2}

    # Convert history to numerical values
    X = np.array([[moves_map[player], moves_map[opponent]] for player, opponent in history])
        
    

    # Make predictions using the loaded model
    try:
        predictions = model.predict(X)
    except:
        predictions = model.predict([[0,0]])

    predicted_moves = [np.argmax(prediction) for prediction in predictions]

    # Map predicted moves back to RPS hands
    reverse_moves_map = {v: k for k, v in moves_map.items()}
    predicted_moves = [reverse_moves_map[move] for move in predicted_moves]

    return predicted_moves
    

class AgentML(Agent):
    def play(self, history: History) -> Hand:
        model_path = './examples/example_agent_with_ml/rps_model_nn.h5'
        loaded_model = load_model(model_path)

        predicted_moves = predict_next_move(loaded_model, history)
        return predicted_moves[-1]