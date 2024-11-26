# app/devices/tv.py
class TV:
    def __init__(self):
        self.is_on = False
        self.volume = 0

    def turn_on(self):
        self.is_on = True
        print("TV encendida.")

    def turn_off(self):
        self.is_on = False
        print("TV apagada.")

    def increase_volume(self):
        self.volume += 1
        print(f"Volumen del TV aumentado a {self.volume}.")

    def decrease_volume(self):
        self.volume -= 1
        print(f"Volumen del TV disminuido a {self.volume}.")
