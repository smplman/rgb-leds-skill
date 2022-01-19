from mycroft import MycroftSkill, intent_handler
from .color_dictionary import color_names
import socketio

# sio = socketio.Client()

# current_color = '#000000'

class RgbLeds(MycroftSkill):

    sio = socketio.Client()

    def __init__(self):
        MycroftSkill.__init__(self)
        self.current_color = '#000000'

    def initialize(self):
        self.sio_call_backs()
        self.sio.connect('http://localhost:8080')
        self.log.info('Initializing rgb-leds-skill')
        #my_setting = self.settings.get('my_setting')
        # self.register_entity_file('leds.rgb.intent')
        self.register_entity_file('color.entity')

        # Catch events
        self.add_event('recognizer_loop:record_begin', self._handle_listener_started)
        self.add_event('recognizer_loop:record_end', self._handle_listener_ended)

    # socketio callbacks
    def sio_call_backs(self):

        @self.sio.event
        def connect():
            print('socketio connection established')

        @self.sio.event
        def set_color(sid, hex):
            print('set_color ', hex)
            self.current_color = hex

    # Lghts on
    @intent_handler('leds.on.intent')
    def handle_leds_on(self, message):
        self.log.info('turning lights on')
        self.sio.emit('set_color', current_color)
        self.speak_dialog('leds.on')

    # Lights off
    @intent_handler('leds.off.intent')
    def handle_leds_off(self, message):
        self.log.info('turning lights off')
        self.sio.emit('set_color', '#000000')
        self.speak_dialog('leds.off')

    # Lights color
    @intent_handler('leds.colors.intent')
    def handle_leds_color(self, message):
        color = message.data.get('color').lower()
        self.log.info('trying to set LED color to ' + color)
        if color is not None:
            hex = color_names[color]
            self.log.info('hex value: ' + hex)
            self.current_color = hex
            self.sio.emit('set_color', hex)
            self.speak_dialog('leds.colors', {'color': color})
        else:
            print('color not found')
            self.speak_dialog('leds.colors.notfound', {'color': color})

    # Mycroft start listening
    def _handle_listener_started(self, message):
        self.sio.emit('set_color', '#0000ff')

    # Mycroft stop listening
    def _handle_listener_ended(self, message):
        self.sio.emit('set_color', self.current_color)

def create_skill():
    return RgbLeds()

