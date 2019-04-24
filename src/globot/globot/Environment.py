from abc import ABC, abstractmethod

from SignalValue import SignalValue

class Environment(ABC):
    def __init__(self):
        pass

    def turn(angle:int=0):
        pass

    def drive(distance:int=0):
        pass

    def change_signal(signal:SignalValue=None):
        pass

