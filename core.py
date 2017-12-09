import time

class DomoticCore:
    def __init__(self, sensors):
        self.sensors = sensors # Bridges

    def mainLoop(self, frequency=1):
        delay = int(1/frequency)
        while True:
            for s in self.sensors:
                print s.pushData()
            time.sleep(delay)
