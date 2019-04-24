from Ruleset import Ruleset
from SingalValue import SingalValue
from Environment import Environment

class Globot():
    def __init__(self, ruleset: Ruleset, environment:Environment):
        self.ruleset = ruleset
        self.environment = environment
        self.sleep_timer = 0

    def step(self, stimuli: SignalSet):
        if self.sleep_timer > 0:
            self.sleep_timer -= 1
            return
        else:
            action = self.ruleset.get_action(stimuli)
            if action.sleep > 0:
                self.sleep_timer = action.sleep
            self.environment.turn(angle=action.rotation)
            self.environment.drive(distance=action.drive)
            self.environment.change_signal(signal_value=action.new_signal_value)
        return
