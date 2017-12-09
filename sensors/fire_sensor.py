import time

TEST = 0
PRODUCTION = 1


class FireSensor:
    """docstring for FireSensor."""
    def __init__(self, pin=None):
        self.currentState = 0
        if pin == None:
            self.type = TEST
            self.pin = None
        elif pin == PRODUCTION:
            self.type = PRODUCTION
            self.pin = None

    def getState(self):
        if self.type == TEST:
            localtime = time.localtime(time.time())
            if localtime.tm_sec % 2 == 0:
                return 0
            else:
                return 1
        elif self.type == PRODUCTION:
            pass

    def getCurrentValue(self):
        return self.getState()
