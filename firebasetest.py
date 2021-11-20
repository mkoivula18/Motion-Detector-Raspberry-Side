#IN CASE GRPC NOT WORKING
# export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0

from firebase_admin import db, credentials, firestore
import firebase_admin
import RPi.GPIO as GPIO
import time

pir = 4
movementCounter = 0
movementDetected = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)


cred = credentials.Certificate('ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

"""
doc_ref = db.collection('MotionDetector').add({
    'Detections': 0, 
    'Sensor': 'PIR'
})
"""

print("Starting Motiontracker...")
try:
    while True:
        time.sleep(2)

        if GPIO.input(pir) == 1 and movementDetected == False:
            print("MOTION DETECTED")
            movementDetected = True
            movementCounter += 1
            db.collection('MotionDetector').document('ZERokZzMZJQAQTIAjGNz').update({
                'Detections': movementCounter, 
                'Sensor': 'PIR'
            })

        if GPIO.input(pir) == 0 and movementDetected == True:
            print("NO MOTION")
            movementDetected = False
except KeyboardInterrupt:
    GPIO.cleanup()

