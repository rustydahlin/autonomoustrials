'''
State Base class information
'''
class BaseState(object):
    '''
    Class for the state base so that they can be properly utilized
    '''
    def enter(self, robitclass):
        '''
        Override called on entering the state
        '''
        raise NotImplementedError("Enter method has not been implemented")

    def execute(self, robitclass):
        '''
        Override called on executing the state
        '''
        raise NotImplementedError("Execute method has not been implemented")

    def exit(self, robitclass):
        '''
        Override called when exiting the state
        '''
        raise NotImplementedError("Exit method has not been implemented")
