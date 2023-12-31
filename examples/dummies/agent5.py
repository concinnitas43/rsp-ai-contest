# always returns whatever wins what the opponent played in the previous round
from classes.agent import Agent
from classes.utils import *

class Agent5(Agent):
    def play(self, history: History) -> Hand:
        try: 
            return succ(history[-1][1])
        except IndexError:
            return Hand.R