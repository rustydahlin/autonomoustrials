import time

import RPi.GPIO as GPIO

import robit.motor.l298motor as motor
import robit.movement.tankmovement as tanks
import robit.constants as consts

def runit(tank):
    print('Should turn right for a little bit')
    tank.rotate(consts.MOTOR_DIRECTION_POSITIVE)
    time.sleep(.3)
    print('should turn left for a little')
    tank.rotate(consts.MOTOR_DIRECTION_NEGATIVE)
    time.sleep(.3)
    print('How about a straight line forward')
    tank.travel(consts.MOTOR_DIRECTION_POSITIVE)
    time.sleep(.3)
    print('and how about a normal rolling stop')
    tank.stop()
    time.sleep(.3)
    print('How about a straight line backward')
    tank.travel(consts.MOTOR_DIRECTION_NEGATIVE)
    time.sleep(.3)
    print('and how about a Quick stop')
    tank.stop()
    time.sleep(.3)
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)

    leftmotor = motor.L298Motor(37, 40, 7)
    rightmotor = motor.L298Motor(13, 12, 11)
    tank = tanks.TankMovement(leftmotor, rightmotor, False)
    tank.travelspeed = 100
    tank.rotatespeed = 100
    runit(tank)
    tank.travelspeed = 75
    tank.rotatespeed = 75
    runit(tank)
    tank.travelspeed = 50
    tank.rotatespeed = 50
    runit(tank)
    tank.travelspeed = 25
    tank.rotatespeed = 25
    runit(tank)

    GPIO.cleanup()
