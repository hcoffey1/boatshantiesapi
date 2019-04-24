import sys
sys.path.append('../')
import pins
import RPi.GPIO as GPIO
from enum import Enum

class LED(Enum):
    '''
    Used to indicate which LED for usage
    '''
    FRONT = 0
    BACK = 1
    LEFT = 2
    RIGHT = 3

class STATE(Enum):
    '''
    Pass to functions to turn LED on/off
    '''
    ON = GPIO.HIGH
    OFF = GPIO.LOW

def led_init():
    '''
    Initialize's led pins for usage. 
    '''
    GPIO.setup(pins.LED_FRONT, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pins.LED_BACK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pins.LED_LEFT, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pins.LED_RIGHT, GPIO.OUT, initial=GPIO.LOW)

def led_toggle(led, state):
    '''
    Sets led to given state, i.e.
    led_toggle(LED.FRONT, STATE.ON) #Sets front led to on
    '''
    if led == LED.FRONT:
        GPIO.output(pins.LED_FRONT, value)
    elif led == LED.BACK:
        GPIO.output(pins.LED_BACK, value)
    elif led == LED.LEFT:
        GPIO.output(pins.LED_LEFT, value)
    elif led == LED.RIGHT:
        GPIO.output(pins.LED_RIGHT, value)
