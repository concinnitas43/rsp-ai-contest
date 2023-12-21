from classes.game import *
from examples.dummies.agent1 import Agent1
from examples.dummies.agent2 import Agent2
from examples.dummies.agent3 import Agent3
from examples.dummies.agent4 import Agent4
from examples.dummies.agent5 import Agent5
from examples.dummies.agent6 import Agent6

## FROM YOUR OWN BOT
from examples.dummies.agent4 import Agent4

dummies = [Agent1(), Agent2(), Agent3(), Agent4(), Agent5(), Agent6()]

myBot = Agent4()

g.run(100)

print(g.result)