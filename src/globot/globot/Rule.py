from SignalValue import SignalValue
from SignalSet import SignalSet
from Action import Action

class Rule:
    def __init__(self, signal_set:SignalSet=None, action:Action=None):
        # Inputs
        self.signal_set = signal_set if signal_set else SignalSet()
        # Outputs
        self.action = action if action else Action()

    @staticmethod
    def build_from_json(json_data:dict):
       signal_set = SignalSet.build_from_json(json_data=json_data["signal_set"])
       action = Action.build_from_json(json_data=json_data["action"])
       return Rule(signal_set=signal_set, action=action)

    def __str__(self):
        return """
##################################################
f:{}            rotate: {}
r:{}    =>      drive:  {} 
b:{}            signal: {}
l:{}            sleep:  {}
##################################################
        """.format(
                self.signal_set.forward,
                self.action.rotation,
                self.signal_set.right,
                self.action.drive,
                self.signal_set.back,
                self.action.new_signal,
                self.signal_set.left,
                self.action.sleep
                )

