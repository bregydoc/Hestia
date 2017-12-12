import json
import sensors

def getSensorsAndActuatorsFromJson(db, jsonPath):
    jo = open(jsonPath, 'r')
    rawData = jo.read()
    properties = json.loads(rawData)

    # sensors = []

    for s in properties['sensors']:
        doc = None
        sen = None
        if s['type'] == 'temperature':
            con = sensors.temperature_sensor.TEST
            if s['conexion'] == 'onewire':
                con = sensors.temperature_sensor.ONE_WIRE
            if s['conexion'] == 'i2c':
                con = sensors.temperature_sensor.I2C
            sen = sensors.temperature_sensor.TemperatureSensor(con)

        if s['type'] == 'movement':
            # con = sensors.movement_sensor.TEST
            sen =  sensors.movement_sensor.MovementSensor(pin=None)
            if 'GPIO' in s['conexion']:
                pingpio = int(s['conexion'].split('@')[1])
                # con = sensors.movement_sensor.PRODUCTION
                sen = sensors.movement_sensor.MovementSensor(pin=pingpio)

        if s['type'] == 'generic':
            pingpio = int(s['conexion'].split('@')[1])
            sen = sensors.base_sensor.GenericSensor(pin=pingpio)

        doc = db.collection(u'sensors').document(s['route'])

        senBridge = fb.FireBridgeSensor(doc, sen)
