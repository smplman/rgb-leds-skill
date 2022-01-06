from mycroft import MycroftSkill, intent_file_handler


class RgbLeds(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('leds.rgb.intent')
    def handle_leds_rgb(self, message):
        self.speak_dialog('leds.rgb')


def create_skill():
    return RgbLeds()

