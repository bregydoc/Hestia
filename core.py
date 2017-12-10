import time

class DomoticCore:
    def __init__(self, sensors, actuators):
        self.sensors = sensors # Sensor Bridges
        self.actuators = actuators # Actuator Bridges

    def mainLoop(self, frequency=1):
        delay = int(1/frequency)
        while True:
            for a in self.actuators:
                a.propagateData()
            for s in self.sensors:
                print s.pushData()
            time.sleep(delay)
