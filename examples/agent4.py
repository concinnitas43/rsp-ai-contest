# Paper only
from classes.agent import Agent
from classes.utils import *

class Agent4(Agent):
    def play(self, history: History) -> Hand:
        return Hand.P