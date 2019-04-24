import sys
sys.path.append('../src')

import wiringpi
import pins
import RPi.GPIO as GPIO
from time import sleep

def detected(channel):
    print("Found light!")

if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pins.LED, GPIO.OUT, initial=GPIO.LOW)
    #GPIO.setup(pins.SERVO_1, GPIO.OUT, initial=GPIO.LOW)
    
    #GPIO.setup(pins.PHOTOTRAN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(pins.PHOTOTRAN, GPIO.IN)
    
    GPIO.add_event_detect(pins.PHOTOTRAN, GPIO.RISING, callback=detected, bouncetime=300)

    wiringpi.wiringPiSetupGpio()

    wiringpi.pinMode(12, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)
    
    delay_period = 0.01

    while True:
        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')
        GPIO.output(pins.LED, GPIO.HIGH)
        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')
        #GPIO.output(pins.SERVO_1, GPIO.HIGH)
        sleep(1)
        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')

        GPIO.output(pins.LED, GPIO.LOW)
        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')
        #GPIO.output(pins.SERVO_1, GPIO.LOW)

        sleep(1)
