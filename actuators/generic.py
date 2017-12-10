
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class GenericActuator:
    def __init__(self, pin, default=0):
        self.pin = pin
        self.internalState = default
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def setState(self, s):
        self.internalState = s
        GPIO.output(self.pin, self.internalState)

    def toggleState(self):
        self.internalState ^= 1
        GPIO.output(self.pin, self.internalState)

    def closeActuator(self):
        GPIO.cleanup()

    def getInternalState(self):
        return self.internalState
