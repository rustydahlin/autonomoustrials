'''
Just a simple main starter page to run everything else
'''
import robit.robit
import ai.behavioral.arbitrator
from ai.behavioral.examples import moveforward, movebackward
import ai.fsm.fsmrobit
import ai.fsm.examples.states


def behavior():
    behaviorlist = (movebackward.MoveBackward(), moveforward.MoveForward())
    therobit = robit.robit.Robit(False, 100)
    arbit = ai.behavioral.arbitrator.Arbitrator(listofbehaviors=behaviorlist, robitclass=therobit)
    arbit.start()

def fsm():
    therobit = robit.robit.Robit(False, 100)
    fsmsystem = ai.fsm.fsmrobit.FSMRobit(therobit, ai.fsm.examples.states.MoveForward())
    while fsmsystem.hasstate():
        fsmsystem.update()

if __name__ == "__main__":
    #behavior()
    fsm()
