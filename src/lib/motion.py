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
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CCW)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CW)
    elif state == MOVE.BACK:
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CW)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CCW)
    elif state == MOVE.RIGHT:
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CCW)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.HALT)
    elif state == MOVE.LEFT:
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.HALT)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CCW)
    elif state == MOVE.HALT:
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.HALT)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.HALT)

