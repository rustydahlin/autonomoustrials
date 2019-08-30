'''
Class for tank movement
'''
import robit.movement.bases
import robit.motor.bases

class TankMovement(robit.movement.bases.MovementBase):
    '''
    Base class for all motor controllers mostly used as interface
    '''
    def __init__(self, leftmotor, rightmotor, reverse=False, travelspeed=100, rotatespeed=100, acceleration=100):
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.reverse = reverse
        super().__init__(travelspeed, rotatespeed, acceleration)

    @property
    def reverse(self):
        '''
        get the reverse
        '''
        return self.__reverse

    @reverse.setter
    def reverse(self, reverse):
        '''
        set the reverse must be an bool true will reverse he motors for positive vs negative travel and rotation
        '''
        if isinstance(reverse, bool):
            self.__reverse = reverse
        else:
            raise Exception("reverse must be of type bool")

    @property
    def leftmotor(self):
        '''
        get the leftmotor
        '''
        return self.__leftmotor

    @leftmotor.setter
    def leftmotor(self, leftmotor):
        '''
        set the leftmotor must be an motor
        '''
        if isinstance(leftmotor, robit.motor.bases.Motor):
            self.__leftmotor = leftmotor
        else:
            raise Exception("leftmotor must be of type motor")

    @property
    def rightmotor(self):
        '''
        get the rightmotor
        '''
        return self.__rightmotor

    @rightmotor.setter
    def rightmotor(self, rightmotor):
        '''
        set the rightmotor must be an motor
        '''
        if isinstance(rightmotor, robit.motor.bases.Motor):
            self.__rightmotor = rightmotor
        else:
            raise Exception("rightmotor must be of type motor")

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
        if distance:
            raise NotImplementedError("Sorry have not implemented the Distance yet")
        if self.reverse:
            direction = direction * -1
        if direction > 0:
            self.leftmotor.clockwise(self.travelspeed)
            self.rightmotor.clockwise(self.travelspeed)
        else:
            self.leftmotor.counterclockwise(self.travelspeed)
            self.rightmotor.counterclockwise(self.travelspeed)

    def rotate(self, direction, degrees=None):
        '''
        rotate the motors in opposite directions to rotate robot in a direction and if degrees is set stop after that many degrees
        direction - USE the GLOBAL Constants positive is right negative is left if connected correctly
        degrees - integer for how many degrees to rotate if none continuous rotation
        '''
        if degrees:
            raise NotImplementedError("Sorry have not implemented the Degrees yet")
        if self.reverse:
            direction = direction * -1
        if direction > 0:
            self.leftmotor.clockwise(self.rotatespeed)
            self.rightmotor.counterclockwise(self.rotatespeed)
        else:
            self.leftmotor.counterclockwise(self.rotatespeed)
            self.rightmotor.clockwise(self.rotatespeed)

    def stop(self):
        '''
        Should implement a normal stop with any necessary cleanup and run out of motors as needed.
        '''
        self.leftmotor.stop()
        self.rightmotor.stop()

    def emergency_stop(self):
        '''
        Should implement a method where the motors stop as fast as possible with the least amount of cleanup or travel.
        Should only be used in emergency situations.
        '''
        self.leftmotor.brakestop()
        self.rightmotor.brakestop()
