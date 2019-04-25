import sys
sys.path.append('../')
import pins
import RPi.GPIO as GPIO
from enum import Enum

#PWM Value for LED's
BRIGHTNESS = 30

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
    #ON = GPIO.HIGH
    #OFF = GPIO.LOW
    ON = BRIGHTNESS
    OFF = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins.LED_FRONT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pins.LED_BACK, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pins.LED_LEFT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pins.LED_RIGHT, GPIO.OUT, initial=GPIO.LOW)

LF_PWM = GPIO.PWM(LED.FRONT.value, 100)
LB_PWM = GPIO.PWM(LED.BACK.value, 100)
LL_PWM = GPIO.PWM(LED.LEFT.value, 100)
LR_PWM = GPIO.PWM(LED.RIGHT.value, 100)

LF_PWM.start(0)
LB_PWM.start(0)
LL_PWM.start(0)
LR_PWM.start(0)

def led_toggle(led, state):
    '''
    Sets led to given state, i.e.
    led_toggle(LED.FRONT, STATE.ON) #Sets front led to on
    '''
    if led == LED.FRONT:
        LF_PWM.ChangeDutyCycle(state.value)
    elif led == LED.BACK:
        LB_PWM.ChangeDutyCycle(state.value)
    elif led == LED.LEFT:
        LL_PWM.ChangeDutyCycle(state.value)
    elif led == LED.RIGHT:
        LR_PWM.ChangeDutyCycle(state.value)

    #p = GPIO.PWM(led.value, 100)
    #p.start(0)
    #p.ChangeDutyCycle(BRIGHTNESS)
    #GPIO.output(led.value, state.value)
