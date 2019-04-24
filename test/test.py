import sys
sys.path.append('../src')

#import wiringpi
import pins
import RPi.GPIO as GPIO
from time import sleep

#pwm of 1 and 19 are opposites for servo direction, 0-19 values
#seem important, anything above that appears to not change
#10-15 is when servo begins to slow and then change direction

def detected(channel):
    if GPIO.input(channel):
        delay_period = 1 
        print("Found light!")
        p1.ChangeDutyCycle(8)
        p2.ChangeDutyCycle(19)
        sleep(1)
        #for x in range(100):
        #    print("DUTY: " + str(x))
        #    p.ChangeDutyCycle(x)
        #    sleep(delay_period)
    else:
        print("LOST light!")
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)



if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins.LED, GPIO.OUT, initial=GPIO.LOW)
    #GPIO.setup(pins.SERVO_1, GPIO.OUT, initial=GPIO.LOW)
    
    #GPIO.setup(pins.PHOTOTRAN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(pins.PHOTOTRAN, GPIO.IN)
    
    GPIO.add_event_detect(pins.PHOTOTRAN, GPIO.BOTH, callback=detected, bouncetime=300)
    #GPIO.add_event_detect(pins.PHOTOTRAN, !GPIO.RISING, callback=fall, bouncetime=300)

    GPIO.setup(pins.SERVO_1, GPIO.OUT)
    p1 = GPIO.PWM(pins.SERVO_1, 100)
    p1.start(0)

    GPIO.setup(pins.SERVO_2, GPIO.OUT)
    p2 = GPIO.PWM(pins.SERVO_2, 100)
    p2.start(0)
    #wiringpi.wiringPiSetupGpio()

#    wiringpi.pinMode(pins.SERVO_1, wiringpi.GPIO.PWM_OUTPUT)
#    wiringpi.pinMode(pins.SERVO_2, wiringpi.GPIO.PWM_OUTPUT)
#    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

#    wiringpi.pwmSetClock(192)
#    wiringpi.pwmSetRange(2000)
    
    delay_period = 1 

    while True:
        
        #for pulse in range(50, 250, 1):
        #    wiringpi.pwmWrite(pins.SERVO_1,pulse)
        #    sleep(delay_period)
        #p.ChangeDutyCycle(75) 
     #   for x in range(100):
     #       print("DUTY: " + str(x))
     #       p.ChangeDutyCycle(x)
     #       sleep(delay_period)

        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')

#        wiringpi.pwmWrite(pins.SERVO_1,1)
#        wiringpi.pwmWrite(pins.SERVO_2,1)
        GPIO.output(pins.LED, GPIO.HIGH)

        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')

        sleep(1)

     #   p.ChangeDutyCycle(0)
        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')

#        wiringpi.pwmWrite(pins.SERVO_1,0)
#        wiringpi.pwmWrite(pins.SERVO_2,0)
        GPIO.output(pins.LED, GPIO.LOW)
        if GPIO.input(pins.PHOTOTRAN):
            print('Input is HIGH')
        else:
            print('Input is LOW')
        #GPIO.output(pins.SERVO_1, GPIO.LOW)

        sleep(1)
