import sys
sys.path.append('../') 
import pins
import RPi.GPIO as GPIO
from enum import enum
from time import sleep

class SERVO(Enum):
    '''
    Used to specify Servo
    '''
    LEFT = pins.SERVO_1
    RIGHT = pins.SERVO_2

def servo_init():
    '''
    Initialize's servo pins for usage.
    '''
    GPIO.setup(pins.SERVO_1, GPIO.OUT)
    GPIO.setup(pins.SERVO_2, GPIO.OUT)

def servo_toggle(servo, state):
    p = GPIO.PWM(pins.SERVO_1, 100)
    p.start(0)
    p.ChangeDutyCycle(1)
    sleep(1)
