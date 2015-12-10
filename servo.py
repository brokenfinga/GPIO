import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

l = GPIO.PWM(13,500)
r = GPIO.PWM(15,500)

l.start(75)
r.start(75)

try:

	while True:
		l.ChangeDutyCycle(50)
		r.ChangeDutyCycle(50)
		time.sleep(1)

		l.ChangeDutyCycle(75)
		r.ChangeDutyCycle(75)
		time.sleep(1)

		l.ChangeDutyCycle(50)
		r.ChangeDutyCycle(50)
		time.sleep(1)


except KeyboardInterrupt:
	l.stop()
	r.stop()
	GPIO.cleanup()

