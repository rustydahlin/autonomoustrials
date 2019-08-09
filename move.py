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


if __name__ == '__main__':
    right_motor.forward()
    left_motor.forward()
    time.sleep(3)
    right_motor.stop()
    left_motor.stop()
    GPIO.cleanup()

