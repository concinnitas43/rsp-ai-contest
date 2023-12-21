# Paper only
from classes.agent import Agent
from classes.utils import *

class Agent1(Agent):
    def play(self, history: History) -> Hand:
        return Hand.P