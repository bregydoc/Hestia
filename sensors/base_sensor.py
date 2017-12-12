import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


class GenericSensor:
    def __init__(self, pin):
        self.pin = pin
        self.internalState = 0
        GPIO.setup(self.pin, GPIO.IN)

    def getState(self):
        self.internalState = GPIO.input(self.pin)
        return self.internalState

    def closeChannel(self):
        GPIO.cleanup()

    def getInternalState(self):
        return self.internalState
