import datetime

class FireBridge:
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
