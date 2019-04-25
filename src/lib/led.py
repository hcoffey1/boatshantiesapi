import sys
sys.path.append('../')
import pins
import RPi.GPIO as GPIO
from enum import Enum

#PWM Value for LED's
#BRIGHTNESS = 30

class LED(Enum):
    '''
    Used to indicate which LED for usage
    '''
    FRONT = pins.LED_FRONT
    BACK = pins.LED_BACK
    LEFT = pins.LED_LEFT
    RIGHT = pins.LED_RIGHT 

class STATE(Enum):
    '''
    Pass to functions to turn LED on/off
    '''
    ON = GPIO.HIGH
    OFF = GPIO.LOW

GPIO.setup(pins.LED_FRONT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pins.LED_BACK, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pins.LED_LEFT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pins.LED_RIGHT, GPIO.OUT, initial=GPIO.LOW)

#def led_init():
#    '''
#    Initialize's led pins for usage. 
#    '''
#    GPIO.setup(pins.LED_FRONT, GPIO.OUT, initial=GPIO.LOW)
#    GPIO.setup(pins.LED_BACK, GPIO.OUT, initial=GPIO.LOW)
    #GPIO.setup(pins.LED_LEFT, GPIO.OUT, initial=GPIO.LOW)
    #GPIO.setup(pins.LED_RIGHT, GPIO.OUT, initial=GPIO.LOW)

def led_toggle(led, state):
    '''
    Sets led to given state, i.e.
    led_toggle(LED.FRONT, STATE.ON) #Sets front led to on
    '''
    #p = GPIO.PWM(led.value, 100)
    #p.start(0)
    #p.ChangeDutyCycle(BRIGHTNESS)
    GPIO.output(led.value, state.value)
