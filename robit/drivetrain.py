'''
Base class for drive control. Override with robot specific implementations.
'''
class BaseDrivetrain(object):
    '''
    go - True/False
    direction - 1 = forward, 0 = backwards
    speed - 1-100 (100 = full speed)
    '''
    def motor_left(self, go, direction, speed):
        if go:
            print("direction: {0} speed: {1}".format(direction, speed))
        else:
            print("stop")

    '''
    go - True/False
    direction - 1 = forward, 0 = backwards
    speed - 1-100 (100 = full speed)
    '''
    def motor_right(self, go, direction, speed):
        if go:
            print("direction: {0} speed: {1}".format(direction, speed))
        else:
            print("stop")

