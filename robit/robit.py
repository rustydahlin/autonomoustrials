'''
Robit class for keeping track of everything
'''
import random

class Robit(object):
    def __init__(self, hitsomething, distance):
        self.hitsomething = hitsomething
        self.distance = distance

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

    def moveforward(self):
        self.distance = self.distance - 3
        self.hitsomething = 25 > random.randint(0,100) #random chance of hitting something when moving forward change later

    def movebackward(self):
        self.distance = self.distance + 1
        self.hitsomething = False

    def __str__(self):
        return str({'HitSomething':self.hitsomething, 'Distance':self.distance})
