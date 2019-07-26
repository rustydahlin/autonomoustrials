'''
SensorManager keeps all the sensor data updated without overpolling any 1 sensor
'''

import board
import busio
import adafruit_tcs34725

I2C = busio.I2C(board.SCL, board.SDA)


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
        else:
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

    @property
    def sensoraddress(self):
        return self.__sensoraddress

    @sensoraddress.setter
    def sensoraddress(self, sensoraddress):
        self.__sensoraddress = sensoraddress

class ColorSensor(I2CSensor):
    '''
    TCS34725 color sensor class
    Documentation https://buildmedia.readthedocs.org/media/pdf/adafruit-circuitpython-tcs34725/latest/adafruit-circuitpython-tcs34725.pdf
    '''
    def __init__(self, sensoraddress, idval, integration_time=200, gain=60):
        self.__rgb = None
        self.__temperature = None
        self.__lux = None
        self.__sensor = adafruit_tcs34725.TCS34725(I2C)
        self.integration_time = integration_time
        self.gain = gain
        super().__init__(sensoraddress, idval)

    @property
    def integration_time(self):
        return self.__sensor.integration_time

    @integration_time.setter
    def integration_time(self, integration_time):
        self.__sensor.integration_time = integration_time

    @property
    def gain(self):
        return self.__sensor.gain

    @gain.setter
    def gain(self, gain):
        self.__sensor.gain = gain

    def pollsensor(self):
        self.__lux = self.__sensor.lux
        self.__temperature = self.__sensor.color_temperature
        self.__rgb = self.__sensor.color_rgb_bytes

    def getdatadict(self):
        return {'rgb':self.__rgb, 'lux':self.__lux, 'temperature':self.__temperature}


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
