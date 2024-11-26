# app/commands/fan_commands.py
from app.commands.command import Command
from app.devices.fan import Fan

class FanOnCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

    def undo(self):
        self.fan.turn_off()

class FanSpeedHighCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.set_speed("high")

    def undo(self):
        self.fan.set_speed("medium")  # Revertimos a la velocidad media como ejemplo

class FanSpeedLowCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.set_speed("low")

    def undo(self):
        self.fan.set_speed("medium")
