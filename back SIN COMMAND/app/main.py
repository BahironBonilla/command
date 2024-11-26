from fastapi import FastAPI

app = FastAPI()


class RemoteControl:
    def __init__(self):
        self.state = {
            "tv": {"status": "off", "volume": 0},
            "sound": {"status": "off", "volume": 0},
            "light": {"status": "off"},
            "fan": {"status": "off", "speed": "low"},
            "last_action": None,
        }

    def save_last_action(self, action, device):
        """Guarda la última acción realizada para soportar la función de 'deshacer'."""
        self.state["last_action"] = {"action": action, "device": device}

    def perform_undo(self):
        """Deshace la última acción realizada."""
        last_action = self.state["last_action"]
        if not last_action:
            return {"message": "No hay acciones para deshacer"}

        device = last_action["device"]
        action = last_action["action"]

        # Revertir la acción
        if action == "off":
            self.state[device]["status"] = "off"
        elif action == "on":
            self.state[device]["status"] = "on"
        elif action == "volume_up":
            self.state[device]["volume"] += 1
        elif action == "volume_down":
            self.state[device]["volume"] = max(0, self.state[device]["volume"] - 1)
        elif action == "speed_high":
            self.state[device]["speed"] = "high"
        elif action == "speed_low":
            self.state[device]["speed"] = "low"

        self.state["last_action"] = None
        return {"message": f"Se deshizo la acción para el dispositivo {device}"}


# Instancia del controlador
remote_control = RemoteControl()


@app.get("/")
def root():
    return {"message": "API para Control Remoto"}


@app.post("/tv/on")
def tv_on():
    remote_control.state["tv"]["status"] = "on"
    remote_control.save_last_action("off", "tv")
    return {"message": "TV encendida"}


@app.post("/tv/off")
def tv_off():
    remote_control.state["tv"]["status"] = "off"
    remote_control.save_last_action("on", "tv")
    return {"message": "TV apagada"}


@app.post("/tv/volume/up")
def tv_volume_up():
    remote_control.state["tv"]["volume"] += 1
    remote_control.save_last_action("volume_down", "tv")
    return {"message": f"Volumen del TV aumentado a {remote_control.state['tv']['volume']}"}


@app.post("/tv/volume/down")
def tv_volume_down():
    remote_control.state["tv"]["volume"] = max(0, remote_control.state["tv"]["volume"] - 1)
    remote_control.save_last_action("volume_up", "tv")
    return {"message": f"Volumen del TV reducido a {remote_control.state['tv']['volume']}"}


@app.post("/sound/on")
def sound_on():
    remote_control.state["sound"]["status"] = "on"
    remote_control.save_last_action("off", "sound")
    return {"message": "Sistema de sonido encendido"}


@app.post("/sound/volume/up")
def sound_volume_up():
    remote_control.state["sound"]["volume"] += 1
    remote_control.save_last_action("volume_down", "sound")
    return {"message": f"Volumen del sistema de sonido aumentado a {remote_control.state['sound']['volume']}"}


@app.post("/light/on")
def light_on():
    remote_control.state["light"]["status"] = "on"
    remote_control.save_last_action("off", "light")
    return {"message": "Luz encendida"}


@app.post("/light/off")
def light_off():
    remote_control.state["light"]["status"] = "off"
    remote_control.save_last_action("on", "light")
    return {"message": "Luz apagada"}


@app.post("/fan/on")
def fan_on():
    remote_control.state["fan"]["status"] = "on"
    remote_control.save_last_action("off", "fan")
    return {"message": "Ventilador encendido"}


@app.post("/fan/speed/high")
def fan_speed_high():
    remote_control.state["fan"]["speed"] = "high"
    remote_control.save_last_action("speed_low", "fan")
    return {"message": "Velocidad del ventilador ajustada a alta"}


@app.post("/fan/speed/low")
def fan_speed_low():
    remote_control.state["fan"]["speed"] = "low"
    remote_control.save_last_action("speed_high", "fan")
    return {"message": "Velocidad del ventilador ajustada a baja"}


@app.post("/undo")
def undo():
    return remote_control.perform_undo()
