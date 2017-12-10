import datetime

class FireBridgeSensor:
    """docstring for FireBridge."""
    def __init__(self, document, sensor):
        self.sensor = sensor
        self.document = document

    def pushData(self):
        d = {
            u'value': self.sensor.getCurrentValue(),
            u'update_at': datetime.datetime.today()
        }
        self.document.set(d)
        return d

    def pullCloudData(self):
        data = self.document.get().to_dict()
        return data

    def pullLocalData(self):
        return {
            u'value': self.sensor.getCurrentValue(),
            u'update_at': datetime.datetime.today()
        }

class FireBridgeActuator:
    """docstring for FireBridge."""
    def __init__(self, document, actuator):
        self.actuator = actuator
        self.document = document

    def pullCloudData(self):
        try:
            data = self.document.get().to_dict()
        except google.cloud.exceptions.NotFound:
            self.document.set({
                u'value': self.actuator.getInternalState(),
                u'update_at': datetime.datetime.today()
            })
        return data

    def propagateData(self):
        data = self.pullCloudData()
        output = data['value']
        self.actuator.setState(output)

    def pullLocalData(self):
        return {
            u'value': self.actuator.getInternalState(),
            u'update_at': datetime.datetime.today()
        }
