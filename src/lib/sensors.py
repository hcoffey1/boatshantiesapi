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

'''
returns the current values for the given pins
'''
def front_value():
    return GPIO.input(PHOTO.FRONT)

def back_value():
    return GPIO.input(PHOTO.BACK)

def left_value():
    return GPIO.input(PHOTO.LEFT)

def right_value():
    return GPIO.input(PHOTO.RIGHT)

def photo_init():
    '''
    Initialize's phototransistor pins for usage.
    '''
    GPIO.setup(pins.PHOTO_FRONT, GPIO.IN)
    GPIO.setup(pins.PHOTO_BACK, GPIO.IN)
    GPIO.setup(pins.PHOTO_LEFT, GPIO.IN)
    GPIO.setup(pins.PHOTO_RIGHT, GPIO.IN)
