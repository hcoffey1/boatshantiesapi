import sys
sys.path.append('../') 
import pins
import RPi.GPIO as GPIO
from enum import Enum
from time import sleep

GPIO.setup(pins.SERVO_1, GPIO.OUT)
GPIO.setup(pins.SERVO_2, GPIO.OUT)

class SERVO(Enum):
    '''
    Used to specify Servo
    '''
    LEFT = pins.SERVO_1
    RIGHT = pins.SERVO_2

class STATE(Enum):
    CW = 1
    CCW = 20

#def servo_init():
#    '''
#    Initialize's servo pins for usage.
#    '''
#    GPIO.setup(pins.SERVO_1, GPIO.OUT)
#    GPIO.setup(pins.SERVO_2, GPIO.OUT)

def servo_toggle(servo, state, length):
    p = GPIO.PWM(servo.value, 100)
    p.start(0)
    p.ChangeDutyCycle(state.value)
    sleep(length)
