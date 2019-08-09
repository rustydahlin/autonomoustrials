'''
Just a simple main starter page to run everything else
'''
import robit.robit
import ai.behavioral.arbitrator
from ai.behavioral.examples import moveforward, movebackward


def behavior():
    behaviorlist = (movebackward.MoveBackward(), moveforward.MoveForward())
    therobit = robit.robit.Robit(False, 100)
    arbit = ai.behavioral.arbitrator.Arbitrator(listofbehaviors=behaviorlist, robitclass=therobit)
    arbit.start()

if __name__ == "__main__":
    behavior()
