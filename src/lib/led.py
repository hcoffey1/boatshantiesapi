import sys
sys.path.append('../')
import pins
import RPi.GPIO as GPIO
from enum import Enum

class DIRECTION(Enum):
    '''
    Used to indicate which LED for usage
    '''
    FRONT = 0
    BACK = 1
    LEFT = 2
    RIGHT = 3

class STATUS(Enum):
    '''
    Pass to functions to turn LED on/off
    '''
    ON = GPIO.HIGH
    OFF = GPIO.LOW

def led_init():
    '''
    Initialize's led pins for usage. 
    '''
    pass

def led_front(value):
    '''
    Write's value to front led pin
    STATUS.ON   - Turns on the LED
    STATUS.OFF  - Turns off the LED
    '''
    pass

def led_back(x):
    '''
    Write's value to rear led pin
    STATUS.ON   - Turns on the LED
    STATUS.OFF  - Turns off the LED
    '''
    pass

def led_left(x):
    '''
    Write's value to left led pin
    STATUS.ON   - Turns on the LED
    STATUS.OFF  - Turns off the LED
    '''
    pass

def led_right(x):
    '''
    Write's value to right led pin
    STATUS.ON   - Turns on the LED
    STATUS.OFF  - Turns off the LED
    '''
    pass
