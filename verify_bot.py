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

my_bot = Agent5() ### FIX THIS LINE WITH YOUR OWN BOT


results = []
for i in range(6):
    g = Game(my_bot, dummies[i])
    g.run(100)
    results.append(g.result)
    print(F"GAME {i+1} RESULTS : {'FAIL' if g.result <= 75 else 'SUCCESS'} \t\t\t {g.result}")


print(results)