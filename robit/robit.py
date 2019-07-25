'''
Robit class for keeping track of everything
'''
import random
from robit.drivetrain import BaseDrivetrain

motors = BaseDrivetrain()

class Robit(object):
    def __init__(self, hitsomething, distance, ultrasonic_dist):
        self.hitsomething = hitsomething
        self.distance = distance
        self.ultrasonic_dist = ultrasonic_dist

    @property
    def hitsomething(self):
        return self.__hitsomething

    @hitsomething.setter
    def hitsomething(self, boolvalue):
        self.__hitsomething = boolvalue

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distancevalue):
        self.__distance = distancevalue
    
    @property
    def ultrasonic_dist(self):
        return self.__ultrasonic_dist

    @ultrasonic_dist.setter
    def ultrasonic_dist(self, distancevalue):
        self.__ultrasonic_dist = distancevalue

    def moveforward(self):
        motors.motor_left(True, 1, 100)
        motors.motor_right(True, 1, 100)
        self.distance = self.distance - 3
        self.hitsomething = 25 > random.randint(0,100) #random chance of hitting something when moving forward change later

    def movebackward(self):
        motors.motor_left(True, 0, 100)
        motors.motor_right(True, 0, 100)
        self.distance = self.distance + 1
        self.hitsomething = False

    def spin(self):
        motors.motor_left(True, 1, 100)
        motors.motor_right(True, 0, 100)
    
    def stop(self):
        motors.motor_left(False, 1, 100)
        motors.motor_right(False, 1, 100)

    def __str__(self):
        return str({'HitSomething':self.hitsomething, 'Distance':self.distance})
