from mycroft import MycroftSkill, intent_file_handler


class LivingThings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('things.living.intent')
    def handle_things_living(self, message):
        self.speak_dialog('things.living')


def create_skill():
    return LivingThings()

