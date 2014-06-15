import serial
import time


class LedArduino():

    def __init__(self, com):
        ser = serial.Serial(com)
        ser.baudrate = 9600 #115200
        ser.timeout = 5
        ser.flushInput()
        time.sleep(2)
        self.ser = ser
        
    def writeColor(self, r, g, b, led_id = 0):
        self.ser.writelines("%d,%d,%d,%d\n" %(led_id, r, g, b))
        time.sleep(0.05)

    def writeColorRGB(self, rgb_color, led_id = 0):
        (r,g,b) = self._parse_color(rgb_color)
        self.writeColor(r, g, b, led_id)

    def _parse_color(self, color_hex):
        return (int(color_hex[1:3],16),int(color_hex[3:5],16),int(color_hex[5:7],16))

def testLed():
    COM = "/dev/tty.usbmodem1421"
    leds = LedArduino(COM)
    leds.writeColor(100,100,100, 0)
    leds.writeColor(100,10,10, 1)

if __name__ == '__main__':
	testLed()


