# Paper only
from classes.agent import Agent
from classes.utils import *

class Agent3(Agent):
    def play(self, history: History) -> Hand:
        if len(history) % 2 == 0:
            return Hand.P
        return Hand.R