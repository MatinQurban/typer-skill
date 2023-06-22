from mycroft import MycroftSkill, intent_file_handler


class Typer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('typer.intent')
    def handle_typer(self, message):
        self.speak_dialog('typer')


def create_skill():
    return Typer()

