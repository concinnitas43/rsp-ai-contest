# Rock only
from classes.agent import Agent
from classes.utils import *

class Agent2(Agent):
    def play(self, history: History) -> Hand:
        return Hand.R