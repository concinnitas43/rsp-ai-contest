# always returns whatever the opponent played in the previous round
from classes.agent import Agent
from classes.utils import *

class Agent6(Agent):
    def play(self, history: History) -> Hand:
        return history[-1][1]