from classes.game import *
from examples.agent1 import Agent1
from examples.agent2 import Agent2

g = Game(Agent1(), Agent2())

g.run(100)

print(g.result)