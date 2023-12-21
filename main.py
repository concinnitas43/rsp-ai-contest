from classes.game import *
from examples.agent1 import Agent1
from examples.agent2 import Agent2
from examples.agent3 import Agent3
from examples.agent4 import Agent4
from examples.agent5 import Agent5
from examples.agent6 import Agent6

g = Game(Agent6(), Agent5())

g.run(100)

print(g.result)