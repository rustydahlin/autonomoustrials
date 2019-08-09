'''
Test file for the tcs34725 sensor
'''
import time
from sensormanager.sensormanager import ColorSensor

def main():
    '''
    Looping test for the sensor
    '''
    colorsensor = ColorSensor(0, 'colorsensor1')
    for i in range(0, 10):
        colorsensor.pollsensor()
        print(colorsensor.getdatadict())
        time.sleep(2)


if __name__ == "__main__":
    main()