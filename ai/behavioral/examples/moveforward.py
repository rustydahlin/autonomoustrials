'''
move forward if we can
'''
import ai.behavioral.behavioralbase
class MoveForward(ai.behavioral.behavioralbase.BehavioralBase):
    def __init__(self):
        pass

    def takecontrol(self, robitclass):
        '''
        checks if this behavior thinks it should take control
        '''
        return (not robitclass.hitsomething) and robitclass.distance > 0


    def action(self, robitclass):
        '''
        do something
        '''
        print('Gonna get me a flag nom nom nom')
        robitclass.moveforward()

    def end(self, robitclass):
        '''
        stop and exit whatever you were doing
        '''
        pass
