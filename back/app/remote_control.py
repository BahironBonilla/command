# app/remote_control.py
from app.commands.command import Command

class RemoteControl:
    def __init__(self):
        self.history = []

    def press_button(self, command):
        command.execute()
        self.history.append(command)

    def press_undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
