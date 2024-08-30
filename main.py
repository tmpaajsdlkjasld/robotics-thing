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
	pixel = [0, 0, 0, 0]
	column = [[0]*4]*640
	for x in range(480):
		column += array[x]
	for y in range(640):
		pixel += column[y]
	r = pixel[0]
	g = pixel[1]
	b = pixel[2]
	if r > 1.2*b and g > 1.2*b:
		right()
	elif r > 1.2*g and r > 1.2*b:
		backwards()
	elif g > 1.2*r and g > 1.2*b:
		forwards()
	elif b > 1.1*r and b > 1.1g:
		left()
	else:
		right_motor.value = None
		left_motor.value = None
