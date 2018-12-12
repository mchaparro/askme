#!/usr/bin/python

from flask import request
from flask_api import FlaskAPI
import RPi.GPIO as GPIO
from flask_cors import CORS
import time
#green 24
LEDS = {"green": 16, "red": 18}
GPIO.setmode(GPIO.BCM)
#GPIO.setup(LEDS["green"], GPIO.OUT)
#GPIO.setup(LEDS["red"], GPIO.OUT)


GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT) #led

GPIO.setup(9,GPIO.OUT) #buzzer

GPIO.setup(3,GPIO.OUT)  #a
GPIO.setup(2,GPIO.OUT)  #b
GPIO.setup(14,GPIO.OUT) #c
GPIO.setup(15,GPIO.OUT) #d
GPIO.setup(23,GPIO.OUT) #e
GPIO.setup(4,GPIO.OUT)  #f
GPIO.setup(27,GPIO.OUT) #g
segments = (3,2,14,15,23,4,27)

zero = (1,1,1,1,1,1,0)
one = (0,1,1,0,0,0,0)
two = (1,1,0,1,1,0,1)
three = (1,1,1,1,0,0,1)
four = (0,1,1,0,0,1,1)
five = (1,0,1,1,0,1,1)
six = (1,0,1,1,1,1,1)
seven = (1,1,1,0,0,0,0)
eight = (1,1,1,1,1,1,1)
nine = (1,1,1,0,0,1,1)


app = FlaskAPI(__name__)
CORS(app)
@app.route('/', methods=["GET"])
def api_root():
	try:
		display = int(request.args.get("display"))
	except:
		display = 0
	if display > 9:
		display = 9
	if display == 0:
		GPIO.output(segments, zero)
	elif display == 1:
		GPIO.output(segments, one)
	elif display == 2:
		GPIO.output(segments, two)
	elif display == 3:
		GPIO.output(segments, three)
	elif display == 4:
		GPIO.output(segments, four)
	elif display == 5:
		GPIO.output(segments, five)
	elif display == 6:
		GPIO.output(segments, six)
	elif display == 7:
		GPIO.output(segments, seven)
	elif display == 8:
		GPIO.output(segments, eight)
	elif display == 9:
		GPIO.output(segments, nine)
	else:
		GPIO.output(segments, zero)

	#buzzer!
	for i in range(2):
		for i in range(20):
			GPIO.output(9, 1)
			GPIO.output(24, 1)
			time.sleep(.001)
			GPIO.output(9, 0)
			GPIO.output(24, 0)
			time.sleep(.001)
		time.sleep(.15)
	return "current questions: "+str(display)



@app.route('/off', methods=["GET"])
def lef_off():
	GPIO.output(24, 0)
	return "led off"

@app.route('/on', methods=["GET"])
def led_onn():
	GPIO.output(24, 1)
	return "led on"

#@app.route('/led/<color>/', methods=["GET", "POST"])
#def api_leds_control(color):
# if request.method == "POST":
#        if color in LEDS:
#            GPIO.output(LEDS[color], int(request.data.get("state")))
#    return {color: GPIO.input(LEDS[color])}

if __name__ == "__main__":
	app.run()
