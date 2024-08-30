from gpiozero import Servo
from picamera2 import Picamera2
#from time import sleep

def left():
	left_motor.max()
	right_motor.max()

def forwards():
	left_motor.min()
	right_motor.max()

def right():
	left_motor.min()
	right_motor.min()

def backwards():
	left_motor.max()
	right_motor.min()

left_motor = Servo(25)
right_motor = Servo(4)

left_motor.value = None
right_motor.value = None

picam2 = Picamera2()
picam2.start()

while True
	array = picam2.capture_array()
	r = 0
	g = 0
	b = 0
	for x in range(480):
		for y in range(640):
			r += array[x][y][0]
			g += array[x][y][1]
			b += array[x][y][2]
	if r > 307200*20 and g > 307200:
		right()
	elif r > 307200*20:
		backwards()
	elif g > 307200*20:
		forwards()
	elif b > 307200*20:
		left()
