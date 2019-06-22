'''
arbitrator takes care of all the behaviors
'''
class Arbitrator(object):
    '''
    Manages the behaviors behavior will be higher priority the earlier in the list it is.
    '''
    def __init__(self, listofbehaviors, robitclass):
        self.behaviors = listofbehaviors
        self.robit = robitclass
        self.__currentbehavior = None
        self.__continue = True

    @property
    def behaviors(self):
        return self.__behaviors

    @behaviors.setter
    def behaviors(self, listofbehaviors):
        self.__behaviors = listofbehaviors

    @property
    def robit(self):
        return self.__robit

    @robit.setter
    def robit(self, robitclass):
        self.__robit = robitclass

    def start(self):
        '''
        Start the behaviorclass and keep it running until there is no behavior that is matched
        '''
        while(self.__continue):
            print(str(self.robit))
            nextbehavior = None
            for behavior in self.__behaviors:
                if behavior.takecontrol(self.robit):
                    nextbehavior = behavior
                    break
            if nextbehavior:
                if self.__currentbehavior:
                    self.__currentbehavior.end(self.robit)
                self.__currentbehavior = nextbehavior
                self.__currentbehavior.action(self.robit)
                self.__continue = True
            else:
                self.__continue = False
        print('Got me a Flag and it is so TASTY')
