# app/devices/sound_system.py
class SoundSystem:
    def __init__(self):
        self.is_on = False
        self.volume = 0

    def turn_on(self):
        self.is_on = True
        print("Sistema de sonido encendido.")

    def turn_off(self):
        self.is_on = False
        print("Sistema de sonido apagado.")

    def increase_volume(self):
        self.volume += 1
        print(f"Volumen del sistema de sonido aumentado a {self.volume}.")

    def decrease_volume(self):
        self.volume -= 1
        print(f"Volumen del sistema de sonido disminuido a {self.volume}.")
