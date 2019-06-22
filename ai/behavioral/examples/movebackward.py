'''
backup if we hit something
'''
import ai.behavioral.behavioralbase
class MoveBackward(ai.behavioral.behavioralbase.BehavioralBase):
    def __init__(self):
        pass

    def takecontrol(self, robitclass):
        '''
        checks if this behavior thinks it should take control
        '''
        return robitclass.hitsomething


    def action(self, robitclass):
        '''
        do something
        '''
        print('Oh noes I hit something better move backward')
        robitclass.movebackward()

    def end(self, robitclass):
        '''
        stop and exit whatever you were doing
        '''
        pass
