# always returns whatever the opponent played in the previous round
from classes.agent import Agent
from classes.utils import *

import random

class Agent6(Agent):
    def play(self, history: History) -> Hand:
        try: 
            return history[-1][1]
        except IndexError:
            return random.choice(list(Hand))