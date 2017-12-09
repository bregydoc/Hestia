import random as r
import base_sensor as base

TEST = 0
ONE_WIRE = 1
I2C = 2

class TemperatureSensor:
    """docstring for TemperatureSensor."""
    def __init__(self, typeSensor = TEST):
        if typeSensor == TEST:
            self.connectPin = None
            self.lastValue = 0.0
            self.currentValue = 0.0
        elif typeSensor == ONE_WIRE:
            # I need add connect pin and differente protocols for adquire data
            pass

    def readSensor(self):
        if typeSensor == TEST:
            return r.randint(10, 20)
        elif typeSensor == ONE_WIRE:
            # ...
            return None

    def getCurrentValue(self):
        self.lastValue = self.currentValue
        self.currentValue = self.readSensor()
        return self.currentValue
