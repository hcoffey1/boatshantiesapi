from SimulationEnvironment import SimulationEnvironment
from Globot import Globot
import matplotlib.pyplot as plt
import numpy as np


env = SimulationEnvironment(world_size=30)
globot = Globot.build_from_file("rulesets/spacer.json")
env.add_globot(globot, 1, 1)
globot = Globot.build_from_file("rulesets/spacer.json")
env.add_globot(globot, 29, 29)
globot = Globot.build_from_file("rulesets/seeker.json")
env.add_globot(globot, 29, 1)
globot = Globot.build_from_file("rulesets/beacon.json")
env.add_globot(globot, 15, 15)
globot = Globot.build_from_file("rulesets/beacon.json")
env.add_globot(globot, 11, 15)
globot = Globot.build_from_file("rulesets/beacon.json")
env.add_globot(globot, 11, 11)
globot = Globot.build_from_file("rulesets/beacon.json")
env.add_globot(globot, 10, 11)
env.print_board()
env.step()

plt.imshow(env.get_heatmap(), interpolation='nearest')
plt.show()

env.print_board()
env.step()
env.step()
env.step()
env.step()
env.step()
env.step()
env.print_board()
env.step()
env.step()
env.step()
env.step()
env.step()
env.step()
env.step()
env.step()
env.step()
env.step()
env.print_board()

plt.imshow(env.get_heatmap(), interpolation='nearest')
plt.show()
