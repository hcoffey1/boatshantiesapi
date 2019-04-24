import numpy as np

from Globot import Globot
from SignalValue import SignalValue
from SignalSet import SignalSet
from enum import Enum

DEGRADATION_FACTOR = 1.2

class Orientation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
    @staticmethod
    def orientation_as_delta(orientation):
        delta_dict = {
                0: (0, 1),
                1: (1, 0),
                2: (0, -1),
                3: (-1, 0)
                }
        return delta_dict[orientation.value]

class Direction(Enum):
    FORWARD = 0
    RIGHT = 1
    BACK = 2
    LEFT = 3

class SimulationEnvironment:
    def __init__(self, world_size:int=10, degradation=None):
        if degradation is not None:
            global DEGRADATION_FACTOR
            DEGRADATION_FACTOR = degradation
        # global event counter
        self.gec = 0 
        self.world = [[Tile(self, x, y) for y in range(world_size)] for x in range(world_size)]
        self.size = world_size
        self.globots = set()
        self.sleeping_globots = set()

    def get_gec(self):
        self.gec += 1
        return self.gec

    def add_globot(self, globot:Globot, x:int, y:int):
        if self.world[x][y].occupant is None:
            self.world[x][y].occupant = globot
            self.globots.add(globot)
            globot.signal = SignalValue.random_low()
            globot.x = x
            globot.y = y
            globot.dir = 0
            globot.sleep_timer = 0
        # Increase degradation factor a bit

    def step(self):
        # Check to see if any globots wake up this step:
        for globot in self.sleeping_globots:
            globot.sleep_timer -= 1
            if globot.sleep_timer == 0:
                self.sleeping_globots.remove(globot)
                self.globots.add(globot)

        for globot in self.globots:
            action = globot.get_action(self.get_globot_stimuli_set(globot))
            globot.signal = action.new_signal
            if action.rotation != 0:
                globot.dir = (globot.dir + action.rotation)
                while globot.dir < 0:
                    globot.dir += 360
                globot.dir = globot.dir % 360
            if action.drive != 0:
                self.drive_globot(globot, action.drive)
            if action.sleep != 0:
                self.globots.remove(globot)
                globot.sleep_timer = action.sleep
                self.sleeping_globots.add(globot)

        self.clear_signals()

        for globot in self.globots:
            self.propogate_signal(globot)

        for globot in self.sleeping_globots:
            self.propogate_signal(globot)

    def get_globot_orientation(self, globot:Globot):
        # Push direction into a positive space
        while globot.dir < 0:
            globot.dir += 360
        # Make sure direction isn't greater than 360
        if globot.dir > 360:
            globot.dir = globot.dir % 360
        if globot.dir >= 45 and globot.dir < 135:
            return Orientation.UP
        elif globot.dir >= 135 and globot.dir < 225:
            return Orientation.LEFT
        elif globot.dir >= 225 and globot.dir < 315:
            return Orientation.DOWN
        elif (globot.dir >= 315 and globot.dir < 360) or (globot.dir >= 0 and globot.dir < 45):
            return Orientation.RIGHT

    def get_globot_stimuli_set(self, globot:Globot):
        return SignalSet(
                forward=self.get_globot_stimuli(globot, Direction.FORWARD),
                right=self.get_globot_stimuli(globot, Direction.RIGHT),
                back=self.get_globot_stimuli(globot, Direction.BACK),
                left=self.get_globot_stimuli(globot, Direction.LEFT))

    def get_globot_stimuli(self, globot:Globot, direction:Direction):
        orientation = self.get_globot_orientation(globot)
        resulting_orientation = Orientation((direction.value + orientation.value) % 4)
        return self.get_globot_stimuli_by_orientation(globot=globot, orientation=resulting_orientation)

    def get_globot_stimuli_by_orientation(self, globot:Globot, orientation:Orientation):
        xd, yd = Orientation.orientation_as_delta(orientation)
        new_x = globot.x + xd
        new_y = globot.y + yd
        if new_x >= 0 and new_x < self.size and new_y >= 0 and new_y < self.size:
            return self.world[new_x][new_y].signal_value - globot.signal
        else:
            return SignalValue()

    def drive_globot(self, globot:Globot, distance:int):
        orientation = self.get_globot_orientation(globot)
        xd, yd = Orientation.orientation_as_delta(orientation)
        new_x = globot.x + xd
        new_y = globot.y + yd
        if new_x >= 0 and new_x < self.size and new_y >= 0 and new_y < self.size:
            if self.world[new_x][new_y].occupant == None:
                self.world[globot.x][globot.y].occupant = None
                globot.x = new_x
                globot.y = new_y
                self.world[new_x][new_y].occupant = globot

    def clear_signals(self):
        for x in range(self.size):
            for y in range(self.size):
                self.world[x][y].signal_value = SignalValue()

    def propogate_signal(self, globot:Globot):
        for x in range(self.size):
            for y in range(self.size):
                if globot.x == x and globot.y == y:
                    self.world[x][y].signal_value += globot.signal
                else:
                    self.world[x][y].signal_value += degrade(globot.signal, (((globot.x - x) ** 2 + (globot.y - y) ** 2) ** 0.2))

    def print_board(self):
        repr = ""
        for y in range(self.size - 1, -1, -1):
            for x in range(self.size):
                tile = self.world[x][y]
                if tile.occupant is None:
                    repr += "{:.2f}".format(tile.signal_value.total())
                else:
                    repr += " {}  ".format(self.get_globot_sprite(tile.occupant))
                repr += "    "
            repr += "\n\n"
        print(repr)

    def get_globot_sprite(self, globot:Globot):
        if globot.bottype == "beacon":
            return "*"
        orientation = self.get_globot_orientation(globot)
        return {
                Orientation.UP: "^",
                Orientation.LEFT: "<",
                Orientation.DOWN: "v",
                Orientation.RIGHT: ">"
                }[orientation]

    def get_heatmap(self):
        heatmap = np.zeros((self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                heatmap[x][y] = self.world[x][y].signal_value.total()
        return np.flip(heatmap, axis=0)


def degrade(signal:SignalValue, distance:float):
    distance *= DEGRADATION_FACTOR
    return SignalValue(signal.r / (distance ** 2), signal.g / (distance ** 2), signal.b / (distance ** 2))


class Tile:
    def __init__(self, environment, x:int, y:int):
        self.env = environment
        self.x = x
        self.y = y
        self.signal_value = SignalValue()
        self.occupant = None
        # Event Counter
        self.ec = -1

