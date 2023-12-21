from classes.utils import *
from classes.agent import Agent
import time

def print_bar(value, max_value):
    bar_length = 60
    scaled_value = int(value / max_value * bar_length)
    bar = '#' * scaled_value + '-' * (bar_length - scaled_value)
    print(f"[{bar}] {value}/{max_value}")

class Game:
    def __init__( self, agent1: Agent, agent2: Agent ):
        self.agent1 = agent1
        self.agent2 = agent2
        self.history = History()

        self.result = 0

    def play(self):
        hand1 = self.agent1.play(self.history)
        hand2 = self.agent2.play(flip(self.history))

        self.history.append( (hand1, hand2) )
        self.result += evaluate( (hand1, hand2) )

    def run(self, n: int, broadcast:bool = True, delay = 0.01):
        for t in range(n):
            self.play()
            if broadcast:
                print('\033c')
                print(f"Time : {t + 1}")
                print_bar( self.result + t + 1, 2 * n) # p1
                print_bar( -self.result + t + 1, 2 * n) # p2
            time.sleep(delay)

        
