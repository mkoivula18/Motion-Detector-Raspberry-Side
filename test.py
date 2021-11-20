from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time

pir = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)



try:
	time.sleep(2)
	while True:
		if GPIO.input(pir) == 1:
			print("MOTION DETECTED")
		else:
			print("NO MOTION")
except KeyboardInterrupt:
	GPIO.cleanup()
