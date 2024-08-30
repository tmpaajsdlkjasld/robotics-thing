from gpiozero import Servo
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

while True
	pass
