import sys
import api
sys.path.append("globot/globot")
from Globot import Globot
from Rule import Rule
from SignalValue import SignalValue
from SignalSet import SignalSet
from Action import Action

def get_signal_set():
    front = SignalValue(total=api.get_front_sensor())
    left = SignalValue(api.get_left_sensor())
    right = SignalValue(api.get_right_sensor())
    back = SignalValue(api.get_back_sensor())
    return SignalSet(forward=front, right=right, left=left, back=back)

def perform_action(action:Action):
    api.turn(action.rotation)
    api.drive(action.drive)
    api.sleep(action.sleep)
    api.change_signal(action.new_signal.total())

if __name__ == "__main__":
    path_to_instruction_set = sys.argv[1]
    globot = Globot.build_from_file(path_to_instruction_set)
    while True:
        action = globot.get_action(signal_set=get_signal_set())
        perform_action(action)
        print(action)

