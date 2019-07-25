'''
Move the robit forward
'''
from ai.fsm.statebase import BaseState
import robit.awr.ultrasonic as ultrasonic
import time

class MoveForward(BaseState):

    '''
    Class for the state base so that they can be properly utilized
    '''
    def enter(self, fsmrobit):
        '''
        Override called on entering the state
        '''
        #we can do prechecks here to make sure what state the robit is in but for this example we will do nothing
        pass

    def execute(self, fsmrobit):
        '''
        Override called on executing the state
        '''
        print('Gonna get me a flag nom nom nom')
        if fsmrobit.robit.hitsomething:
            fsmrobit.changestate(MoveBackward())
            return
        elif fsmrobit.robit.distance > 0:
            fsmrobit.robit.moveforward()
            return
        if fsmrobit.robit.distance <= 0:
            print('Got me a Flag and it is so TASTY')
            fsmrobit.changestate(None)


    def exit(self, fsmrobit):
        '''
        Override called when exiting the state
        '''
        #we can do some cleanup of the data while we are here but for the example lets do nothing
        pass

class MoveBackward(BaseState):

    '''
    Class for the state base so that they can be properly utilized
    '''
    def enter(self, fsmrobit):
        '''
        Override called on entering the state
        '''
        #we can do prechecks here to make sure what state the robit is in but for this example we will do nothing
        pass

    def execute(self, fsmrobit):
        '''
        Override called on executing the state
        '''
        print('Oh noes I hit something better move backward')
        fsmrobit.robit.movebackward()
        fsmrobit.changestate(MoveForward())

    def exit(self, fsmrobit):
        '''
        Override called when exiting the state
        '''
        #we can do some cleanup of the data while we are here but for the example lets do nothing
        pass

class AWR_Drive_Till_Yer_Close(BaseState):

    '''
    Class for the state base so that they can be properly utilized
    '''
    def enter(self, fsmrobit):
        '''
        Override called on entering the state
        '''
        #we can do prechecks here to make sure what state the robit is in but for this example we will do nothing
        pass

    def execute(self, fsmrobit):
        '''
        Override called on executing the state
        '''
        fsmrobit.robit.ultrasonic_dist = ultrasonic.checkdist()
        print("Ultrasonic Distance = {0}", fsmrobit.robit.ultrasonic_dist)
        if fsmrobit.robit.ultrasonic_dist < 0.12:
            print("WHAO WHATCH OUT FOR THAT THING THERE!")
            fsmrobit.changestate(AWR_Spin_In_A_Circle())
            return
        else:
            fsmrobit.robit.moveforward()
            return


    def exit(self, fsmrobit):
        '''
        Override called when exiting the state
        '''
        #we can do some cleanup of the data while we are here but for the example lets do nothing
        pass

class AWR_Spin_In_A_Circle(BaseState):

    '''
    Class for the state base so that they can be properly utilized
    '''
    def enter(self, fsmrobit):
        '''
        Override called on entering the state
        '''
        #we can do prechecks here0 to make sure what state the robit is in but for this example we will do nothing
        pass

    def execute(self, fsmrobit):
        '''
        Override called on executing the state
        '''
        print("Executing avoidance maneuver")
        fsmrobit.robit.spin()
        time.sleep(3)
        fsmrobit.robit.stop()
        fsmrobit.changestate(None)


    def exit(self, fsmrobit):
        '''
        Override called when exiting the state
        '''
        #we can do some cleanup of the data while we are here but for the example lets do nothing
        pass