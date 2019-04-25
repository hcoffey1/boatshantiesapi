import sys
sys.path.append('../')
import servo
from enum import Enum

class MOVE(Enum):
    FORWARD = 0
    BACK = 1
    LEFT = 2
    RIGHT = 3
    HALT = 4

def toggle_direction(state):
    if state == MOVE.FORWARD:
        servo.sero_toggle(servo.SERVO.LEFT, servo.STATE.CCW)
        servo.sero_toggle(servo.SERVO.RIGHT, servo.STATE.CW)
    elif state == MOVE.BACK:
        servo.sero_toggle(servo.SERVO.LEFT, servo.STATE.CW)
        servo.sero_toggle(servo.SERVO.RIGHT, servo.STATE.CCW)
    elif state == MOVE.LEFT:
        servo.sero_toggle(servo.SERVO.LEFT, servo.STATE.CCW)
        servo.sero_toggle(servo.SERVO.RIGHT, servo.STATE.HALT)
    elif state == MOVE.RIGHT:
        servo.sero_toggle(servo.SERVO.LEFT, servo.STATE.HALT)
        servo.sero_toggle(servo.SERVO.RIGHT, servo.STATE.CW)
    elif state == MOVE.HALT:
        servo.sero_toggle(servo.SERVO.LEFT, servo.STATE.HALT)
        servo.sero_toggle(servo.SERVO.RIGHT, servo.STATE.HALT)

