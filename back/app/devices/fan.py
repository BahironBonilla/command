# app/devices/fan.py
class Fan:
    def __init__(self):
        self.is_on = False
        self.speed = "medium"

    def turn_on(self):
        self.is_on = True
        print("Ventilador encendido.")

    def turn_off(self):
        self.is_on = False
        print("Ventilador apagado.")

    def set_speed(self, speed: str):
        self.speed = speed
        print(f"Velocidad del ventilador ajustada a {self.speed}.")
