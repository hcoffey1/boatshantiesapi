from Globot import Globot
from SignalSet import SignalSet

def test_single_stimuli():
    ruleset = Globot.build_from_file(filename="rulesets/turnTowardsLight.json")
    left_signalset = SignalSet.build_from_json({'forward':0, 'right':0, 'left':1, 'back':0})
    action = ruleset.get_action(left_signalset)
    assert(action.rotation == 15)

def test_noisy_single_stimuli():
    ruleset = Globot.build_from_file(filename="rulesets/turnTowardsLight.json")
    back_noisy_signalset = SignalSet.build_from_json({'forward':0.2, 'right':0.1, 'left':0, 'back':0.8})
    action = ruleset.get_action(back_noisy_signalset)
    print(action)
    assert(action.rotation == 30)
    
if __name__ == "__main__":
    test_single_stimuli()
