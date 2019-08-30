'''
Class for all the interfaces that will be needed for movemnt of the robit
'''

DIRECTION_POSITIVE = True
DIRECTION_NEGATIVE = False

class MovementBase(object):
    '''
    Base class for all motor controllers mostly used as interface
    '''
    def __init__(self, travelspeed=100, rotatespeed=100, acceleration=100):
        self.travelspeed = travelspeed
        self.rotatespeed = rotatespeed
        self.acceleration = acceleration

    @property
    def travelspeed(self):
        '''
        get the travelspeed
        '''
        return self.__travelspeed

    @travelspeed.setter
    def travelspeed(self, travelspeed):
        '''
        set the travelspeed must be an integer of 1 to 100 sets percentage of max speed bot can travel
        '''
        if isinstance(travelspeed, int) and travelspeed > 0 and travelspeed < 101:
            self.__travelspeed = travelspeed
        else:
            raise Exception("travel speed must be and integer and between 0 and 101 noninclusive")

    @property
    def rotatespeed(self):
        '''
        get the rotatespeed
        '''
        return self.__rotatespeed

    @rotatespeed.setter
    def rotatespeed(self, rotatespeed):
        '''
        set the rotatespeed must be an integer of 1 to 100 sets percentage of maximum rotate speed bot can rotate
        '''
        if isinstance(rotatespeed, int) and rotatespeed > 0 and rotatespeed < 101:
            self.__rotatespeed = rotatespeed
        else:
            raise Exception("rotate speed must be and integer and between 0 and 101 noninclusive")

    def travel(self, direction, distance=None):
        '''
        move the wheels in the same direction if distance is set move for that many units and stop
        direction - Use Global Constants positive would be forward negative would be backwards
        distance - integer for how many units to move in the direction
        '''
        raise NotImplementedError('travel method has not been implemented yet')

    def rotate(self, direction, degrees=None):
        '''
        rotate the motors in opposite directions to rotate robot in a direction and if degrees is set stop after that many degrees
        direction - USE the GLOBAL Constants positive is right negative is left if connected correctly
        degrees - integer for how many degrees to rotate if none continuous rotation
        '''
        raise NotImplementedError('rotate method has not been implemented yet')

    def stop(self):
        '''
        Should implement a normal stop with any necessary cleanup and run out of motors as needed.
        '''
        raise NotImplementedError('stop method has not been implemented yet')

    def emergency_stop(self):
        '''
        Should implement a method where the motors stop as fast as possible with the least amount of cleanup or travel.
        Should only be used in emergency situations.
        '''
        raise NotImplementedError('emergency_stop method has not been implemented yet')