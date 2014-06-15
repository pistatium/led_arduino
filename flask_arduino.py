from flask import Flask
from flask import render_template, url_for, redirect, request
from led_arduino import LedArduino

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('hello.html')

@app.route("/set_color",methods=['POST'])
def set_color():
	COM = "/dev/tty.usbmodem1421"
	leds = LedArduino(COM);
	c1 = request.values['color1']
	c2 = request.values['color2']
	leds.writeColorRGB(c1, 0)
	leds.writeColorRGB(c2, 1)
	return "success"


if __name__ == "__main__":
    app.debug = True
    app.run()