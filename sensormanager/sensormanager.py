'''
SensorManager keeps all the sensor data updated without overpolling any 1 sensor
'''
class Sensor(object):
    '''
    Base sensor class/interface
    '''
    def __init__(self, idval):
        self.idval = idval

    @property
    def idval(self):
        '''
        get the idval
        '''
        return self.__idval

    @idval.setter
    def idval(self, idval):
        '''
        set the idvalue
        '''
        if isinstance(idval, str):
            self.__idval = idval
        raise Exception("idval was of the incorrect type for sensor object")

    def pollsensor(self):
        raise NotImplementedError('pollsensor method has not been implemented yet')

    def getdatadict(self):
        raise NotImplementedError('getdatadict method has not been implemented yet')

class I2CSensor(Sensor):
    '''
    Base class for i2c sensors this still needs some implementation
    '''
    def __init__(self, sensoraddress, idval):
        self.sensoraddress = sensoraddress
        super().__init__(idval)


class SensorManager(object):
    '''
    Keeps a list of sensor objects and runs
    through them at a speed that will not kill the bus
    '''
    def __init__(self, sensorlist):
        self.sensorlist = sensorlist

    @property
    def sensorlist(self):
        '''
        get sensorlist
        '''
        return self.__sensordict.values()

    @sensorlist.setter
    def sensorlist(self, sensorlist):
        '''
        set the sensorlist
        '''
        if isinstance(sensorlist, list):
            self.__sensordict = dict()
            for sensor in sensorlist:
                if sensor.idval in self.__sensordict:
                    raise ValueError('Key "{0}" already exists in sensorlist'.format(sensor.idval))
                self.__sensordict[sensor.idval] = sensor
        raise Exception('Invalid sensor list')

    def singlelistrun(self):
        '''
        run a single loop through all the sensors and let them update themselves
        '''
        for sensor in self.sensorlist.values():
            sensor.pollsensor()
