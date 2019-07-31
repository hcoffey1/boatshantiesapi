#!/usr/bin/env python3
import sys
sys.path.append('../')
import pins
import RPi.GPIO as GPIO
from enum import Enum

class PHOTO(Enum):
    '''
    Used to indicate which Phototransistors for usage
    '''
    FRONT = pins.PHOTO_FRONT
    BACK = pins.PHOTO_BACK
    LEFT = pins.PHOTO_LEFT
    RIGHT = pins.PHOTO_RIGHT

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins.PHOTO_FRONT, GPIO.IN)
GPIO.setup(pins.PHOTO_BACK, GPIO.IN)
GPIO.setup(pins.PHOTO_LEFT, GPIO.IN)
GPIO.setup(pins.PHOTO_RIGHT, GPIO.IN)

#Returns the current values for the given pins
def front_value():
    return GPIO.input(PHOTO.FRONT.value)

def back_value():
    return GPIO.input(PHOTO.BACK.value)

def left_value():
    return GPIO.input(PHOTO.LEFT.value)

def right_value():
    return GPIO.input(PHOTO.RIGHT.value)
