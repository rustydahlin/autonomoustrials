'''
L298 motot classes.
'''
import RPi.GPIO as GPIO

import robit.motor.bases
import robit.constants

class L298Motor(robit.motor.bases.Motor):
    '''
    Class for interfacing with motors on an l298 based controller
    '''
    def __init__(self, clockwisepin, counterclockwisepin, enablepin, basehz=1000):
        self.clockwisepin = clockwisepin
        self.counterclockwisepin = counterclockwisepin
        self.enablepin = enablepin
        self.basehz = basehz
        GPIO.setup(enablepin, GPIO.OUT)
        GPIO.setup(clockwisepin, GPIO.OUT)
        GPIO.setup(counterclockwisepin, GPIO.OUT)
        GPIO.output(enablepin, GPIO.LOW)
        GPIO.output(clockwisepin, GPIO.LOW)
        GPIO.output(counterclockwisepin, GPIO.LOW)
        try:
            self.pwm = GPIO.PWM(enablepin, self.basehz)
            self.pwm.start(100)
        except:
            pass

    @property
    def clockwisepin(self):
        '''
        get the clockwisepin
        '''
        return self.__clockwisepin

    @clockwisepin.setter
    def clockwisepin(self, clockwisepin):
        '''
        set the clockwisepin must be an integer and in the list of GPIO pins and available
        '''
        if isinstance(clockwisepin, int) and clockwisepin in robit.constants.GPIO_BOARD_PINS:
            self.__clockwisepin = clockwisepin
        else:
            raise Exception("clockwisepin must be an integer and in the list of GPIO pins and available")

    @property
    def counterclockwisepin(self):
        '''
        get the counterclockwisepin
        '''
        return self.__counterclockwisepin

    @counterclockwisepin.setter
    def counterclockwisepin(self, counterclockwisepin):
        '''
        set the counterclockwisepin must be an integer and in the list of GPIO pins and available
        '''
        if isinstance(counterclockwisepin, int) and counterclockwisepin in robit.constants.GPIO_BOARD_PINS:
            self.__counterclockwisepin = counterclockwisepin
        else:
            raise Exception("counterclockwisepin must be an integer and in the list of GPIO pins and available")

    @property
    def basehz(self):
        '''
        get the basehz
        '''
        return self.__basehz

    @basehz.setter
    def basehz(self, basehz):
        '''
        set the basehz must be an integer and positive
        '''
        if isinstance(basehz, int) and basehz > 0:
            self.__basehz = basehz
        else:
            raise Exception("basehz must be an integer and positive")

    def clockwise(self, speed=100):
        '''
        rotate the motor clockwise
        '''
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.counterclockwisepin, GPIO.LOW)
        GPIO.output(self.clockwisepin, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)


    def counterclockwise(self, speed=100):
        '''
        rotate the motor counterclockwise
        '''
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.clockwisepin, GPIO.LOW)
        GPIO.output(self.counterclockwisepin, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        '''
        Rolling stop
        '''
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.counterclockwisepin, GPIO.LOW)
        GPIO.output(self.clockwisepin, GPIO.LOW)

    def brakestop(self):
        '''
        hard stop the motor with resistave induction
        '''
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.counterclockwisepin, GPIO.LOW)
        GPIO.output(self.clockwisepin, GPIO.LOW)
        self.pwm.ChangeDutyCycle(100)
