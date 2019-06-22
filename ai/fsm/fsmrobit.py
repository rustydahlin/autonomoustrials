'''
FSM robit management
'''
class FSMRobit(object):

    def __init__(self, robitclass, startingstate):
        self.__currentstate = startingstate
        self.robit = robitclass

    @property
    def robit(self):
        return self.__robit

    @robit.setter
    def robit(self, robitclass):
        self.__robit = robitclass

    def hasstate(self):
        return self.__currentstate

    def changestate(self, nextstate):
        print('changing state ' + str(self.robit))
        if nextstate and self.__currentstate:
            self.__currentstate.exit(self)

            self.__currentstate = nextstate

            self.__currentstate.enter(self)
        elif self.__currentstate:
            self.__currentstate.exit(self)
            self.__currentstate = None

    def update(self):
        print("continuing on" + str(self.robit))
        if self.__currentstate:
            self.__currentstate.execute(self)



