# app/commands/tv_commands.py
from app.commands.command import Command
from app.devices.tv import TV

class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

    def undo(self):
        self.tv.turn_off()

class TVOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

    def undo(self):
        self.tv.turn_on()


class TVVolumeUpCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.increase_volume()

    def undo(self):
        self.tv.decrease_volume()

class TVVolumeDownCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.decrease_volume()

    def undo(self):
        self.tv.increase_volume()
