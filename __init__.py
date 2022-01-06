from mycroft import MycroftSkill, intent_file_handler

import time
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class RgbLeds(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        #my_setting = self.settings.get('my_setting')

        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        strip.begin()

    @intent_file_handler('leds.rgb.intent')
    def handle_leds_rgb(self, message):
        self.speak_dialog('leds.rgb')

    def colorSolid(strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            #strip.show()
            #time.sleep(wait_ms/1000.0)

	strip.show

def create_skill():
    return RgbLeds()

