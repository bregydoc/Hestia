import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import fire_bridge as fb
from sensors import temperature_sensor as temp

import core
# Use the application default credentials
cred = credentials.Certificate("domotic-fe8eb-firebase-adminsdk-wu31l-16589467b7.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

tempRef = db.collection(u'sensors').document(u'temp')
temperature = temp.TemperatureSensor(temp.TEST)
tfb = fb.FireBridge(tempRef, temperature)

domotic = core.DomoticCore([tfb])

domotic.mainLoop(1) # 1Hz
