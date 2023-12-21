# Paper only
from classes.agent import Agent
from classes.utils import *

class Agent4(Agent):
    def play(self, history: History) -> Hand:
        if len(history) >= 2:
            return history[-2]
        return Hand.R