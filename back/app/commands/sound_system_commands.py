# app/commands/sound_system_commands.py
from app.commands.command import Command
from app.devices.sound_system import SoundSystem

class SoundSystemOnCommand(Command):
    def __init__(self, sound_system: SoundSystem):
        self.sound_system = sound_system

    def execute(self):
        self.sound_system.turn_on()

    def undo(self):
        self.sound_system.turn_off()

class SoundSystemVolumeUpCommand(Command):
    def __init__(self, sound_system: SoundSystem):
        self.sound_system = sound_system

    def execute(self):
        self.sound_system.increase_volume()

    def undo(self):
        self.sound_system.decrease_volume()
