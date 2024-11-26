# app/devices/light.py
class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Luz encendida.")

    def turn_off(self):
        self.is_on = False
        print("Luz apagada.")
