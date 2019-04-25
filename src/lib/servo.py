import sys
sys.path.append('../') 
import pins
import RPi.GPIO as GPIO
from enum import Enum
from time import sleep

class SERVO(Enum):
    '''
    Used to specify Servo
    '''
    LEFT = pins.SERVO_1
    RIGHT = pins.SERVO_2

class STATE(Enum):
    CW = 1
    CCW = 20
    HALT = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins.SERVO_1, GPIO.OUT)
GPIO.setup(pins.SERVO_2, GPIO.OUT)

S1_PWM = GPIO.PWM(SERVO.LEFT.value, 100)
S2_PWM = GPIO.PWM(SERVO.RIGHT.value, 100)

S1_PWM.start(0)
S2_PWM.start(0)

def servo_toggle(servo, state):
    if servo == SERVO.LEFT:
        S1_PWM.ChangeDutyCycle(state.value)
    elif servo == SERVO.RIGHT:
        S2_PWM.ChangeDutyCycle(state.value)
