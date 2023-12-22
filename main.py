from classes.game import *
from examples.dummies.agent1 import Agent1
from examples.dummies.agent2 import Agent2
from examples.dummies.agent3 import Agent3
from examples.dummies.agent4 import Agent4
from examples.dummies.agent5 import Agent5
from examples.dummies.agent6 import Agent6
from examples.example_agent_with_ml.main_agent import AgentML

g = Game(AgentML(), Agent4())

g.run(100)

print(g.result)