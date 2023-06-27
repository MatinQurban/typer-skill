from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import play_mp3


class Typer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        

    

    @intent_file_handler('typer.intent')
    def handle_typer(self, message):
        self.speak_dialog('Waiting')
        self.wait_while_speaking()
        play_mp3('/home/pi/mycroft-core/mycroft/skills/typer-skill.mycroftai/typer.mp3')
        self.speak_dialog('typer')


def create_skill():
    return Typer()

