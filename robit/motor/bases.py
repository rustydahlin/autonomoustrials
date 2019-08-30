'''
Base class for motors.
'''
class Motor(object):
    '''
    Motor Interface class
    '''
    def clockwise(self, speed=100):
        raise NotImplementedError('clockwise method has not been implemented yet')

    def counterclockwise(self, speed=100):
        raise NotImplementedError('counterclockwise method has not been implemented yet')

    def brakestop(self):
        raise NotImplementedError('brakestop method has not been implemented yet')

    def stop(self):
        raise NotImplementedError('stop method has not been implemented yet')