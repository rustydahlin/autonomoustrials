'''
base classes for behavioral base
'''
class BehavioralBase(object):
    '''
    Behavioral base class
    '''

    def takecontrol(self, robitclass):
        '''
        checks if this behavior thinks it should take control
        '''
        raise NotImplementedError('takecontrol method has not been implemented yet')

    def action(self, robitclass):
        '''
        do something
        '''
        raise NotImplementedError('Action method has not been implemented yet')

    def end(self, robitclass):
        '''
        stop and exit whatever you were doing
        '''
        raise NotImplementedError('end has not be implemented yet')