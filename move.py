import robitConfig
import RPi.GPIO as GPIO
import time

class Motor(object):
    def __init__(self, pin1, pin2, pwm_pin):
        print(
            "Initialize motor: pin1={0}, pin2={1}, pwm_pin={2}", pin1, pin2, pwm_pin)
        self.__pin1__ = pin1
        self.__pin2__ = pin2
        self.__pwm_pin__ = pwm_pin
        GPIO.setup(pwm_pin, GPIO.OUT)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.output(pwm_pin, GPIO.LOW)
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        try:
            self.__pwm__ = GPIO.PWM(pwm_pin, 1000)
        except:
            pass

    def forward(self, speed=100):
        print("{0}/{1}/{2} - Forward speed={3}", self.__pin1__,
              self.__pin2__, self.__pwm_pin__, speed)
        GPIO.output(self.__pin1__, GPIO.HIGH)
        GPIO.output(self.__pin2__, GPIO.LOW)
        self.__pwm__.start(100)
        self.__pwm__.ChangeDutyCycle(speed)

    def backward(self, speed=100):
        print("{0}/{1}/{2} - Backward speed={3}", self.__pin1__,
              self.__pin2__, self.__pwm_pin__, speed)
        GPIO.output(self.__pin1__, GPIO.LOW)
        GPIO.output(self.__pin2__, GPIO.HIGH)
        self.__pwm__.start(0)
        self.__pwm__.ChangeDutyCycle(speed)

    def stop(self):
        print("{0}/{1}/{2} - Stop", self.__pin1__,
              self.__pin2__, self.__pwm_pin__)
        GPIO.output(self.__pin1__, GPIO.LOW)
        GPIO.output(self.__pin2__, GPIO.LOW)
        GPIO.output(self.__pwm_pin__, GPIO.LOW)


GPIO.setmode(GPIO.BOARD)
right_motor = Motor(robitConfig.values.getint("motor.right.gpio.pin1"), 
                    robitConfig.values.getint("motor.right.gpio.pin2"), 
                    robitConfig.values.getint("motor.right.gpio.pwm.pin"))

left_motor = Motor(robitConfig.values.getint("motor.left.gpio.pin1"), 
                    robitConfig.values.getint("motor.left.gpio.pin2"), 
                    robitConfig.values.getint("motor.left.gpio.pwm.pin"))

def forward(speed=100):
    right_motor.forward(speed)
    left_motor.forward(speed)

def backward(speed=100):
    right_motor.backward(speed)
    left_motor.backward(speed)

def stop():
    right_motor.stop()
    left_motor.stop()

# negative values pivot left, positive values pivot right. 
# not necessarily accurate to the degree, more of a ballpark attempt...
def pivot(degrees):
    stop()
    if(degrees > 0):
        right_motor.backward(85)
        left_motor.forward(85)
    else:
        right_motor.forward(85)
        left_motor.backward(85)
    time.sleep(robitConfig.values.getfloat("motor.pivot.factor")*abs(degrees)) 
    stop()

if __name__ == '__main__':
    pivot(-90)
    # pivot(90)
    # forward()
    # time.sleep(.3)
    # pivot(90)
    # forward()
    # time.sleep(.3)
    # pivot(90)
    # forward()
    # time.sleep(.3)
    # pivot(90)
    # forward()
    # time.sleep(.3)
    # stop()

    # right_motor.backward()
    # left_motor.backward()
    # time.sleep(3)
    # right_motor.stop()
    # left_motor.stop()
    GPIO.cleanup()

