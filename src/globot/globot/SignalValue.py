from random import random

class SignalValue:
    def __init__(self, total:float=None, r:float=None, g:float=None, b:float=None):
        if total is not None:
            self.r = float(total)
            self.g = float(total)
            self.b = float(total)
        else:
            self.r = float(r) if r else 0.0
            self.g = float(r) if r else 0.0
            self.b = float(r) if r else 0.0

    @staticmethod
    def build_from_json(json_data):
        if type(json_data) in (int, float):
            return SignalValue(total=float(json_data))
        else:
            return SignalValue(r=float(json_data[0]), g=float(json_data[1]), b=float(json_data[2]))

    def random_low():
        # Returns a SignalValue with values of RGB all randomly selected in the range [0, 0.1)
        return SignalValue(r=(random() / 10), g=(random() / 10), b=(random() / 10))

    @staticmethod
    def distance(a, b):
        return ((a.r - b.r) ** 2 + (a.g - b.g) ** 2 + (a.b - b.b) ** 2) ** 0.5

    def __add__(self, other):
        new_signal_value = SignalValue()
        new_signal_value.alter(self.r, self.g, self.b)
        new_signal_value.alter(other.r, other.g, other.b)
        return new_signal_value

    def __sub__(self, other):
        new_signal_value = SignalValue()
        new_signal_value.alter(self.r, self.g, self.b)
        new_signal_value.alter(-other.r, -other.g, -other.b)
        return new_signal_value

    def __str__(self):
        return "({:0.2}, {:0.2}, {:0.2})".format(float(self.r), float(self.g), float(self.b))
    
    def alter(self, r_delta=0, g_delta=0, b_delta=0):
        self.r += r_delta
        if self.r > 2:
            self.r = 2
        if self.r < 0:
            self.r = 0
        self.g += g_delta
        if self.g > 2:
            self.g = 2
        if self.g < 0:
            self.g = 0
        self.b += b_delta
        if self.b > 2:
            self.b = 2
        if self.b < 0:
            self.b = 0 

    def total(self):
        return (self.r + self.g + self.b) / 3
