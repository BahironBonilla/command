# app/main.py
from fastapi import FastAPI
from app.devices.tv import TV
from app.devices.sound_system import SoundSystem
from app.devices.light import Light
from app.devices.fan import Fan
from app.commands.tv_commands import TVOnCommand, TVVolumeUpCommand, TVVolumeDownCommand, TVOffCommand
from app.commands.sound_system_commands import SoundSystemOnCommand, SoundSystemVolumeUpCommand
from app.commands.light_commands import LightOnCommand, LightOffCommand
from app.commands.fan_commands import FanOnCommand, FanSpeedHighCommand, FanSpeedLowCommand
from app.remote_control import RemoteControl
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por tu origen específico si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tv = TV()
sound_system = SoundSystem()
light = Light()
fan = Fan()
remote_control = RemoteControl()

@app.post("/tv/on")
async def tv_on():
    print("Endpoint /tv/on ejecutado")
    command = TVOnCommand(tv)
    remote_control.press_button(command)
    return {"status": "TV encendida"}

@app.post("/tv/off")
async def tv_off():
    print("Endpoint /tv/off ejecutado")
    command = TVOffCommand(tv)
    remote_control.press_button(command)
    return {"status": "TV apagada"}

@app.post("/tv/volume/up")
async def tv_volume_up():
    command = TVVolumeUpCommand(tv)
    remote_control.press_button(command)
    return {"volume": tv.volume}

@app.post("/tv/volume/down")
async def tv_volume_up():
    command = TVVolumeDownCommand(tv)
    remote_control.press_button(command)
    return {"volume": tv.volume}

@app.post("/sound/on")
async def sound_on():
    command = SoundSystemOnCommand(sound_system)
    remote_control.press_button(command)
    return {"status": "Sistema de sonido encendido"}

@app.post("/sound/volume/up")
async def sound_volume_up():
    command = SoundSystemVolumeUpCommand(sound_system)
    remote_control.press_button(command)
    return {"volume": sound_system.volume}

@app.post("/light/on")
async def light_on():
    command = LightOnCommand(light)
    remote_control.press_button(command)
    return {"status": "Luz encendida"}

@app.post("/light/off")
async def light_off():
    command = LightOffCommand(light)
    remote_control.press_button(command)
    return {"status": "Luz apagada"}

@app.post("/fan/on")
async def fan_on():
    command = FanOnCommand(fan)
    remote_control.press_button(command)
    return {"status": "Ventilador encendido"}

@app.post("/fan/speed/high")
async def fan_speed_high():
    command = FanSpeedHighCommand(fan)
    remote_control.press_button(command)
    return {"speed": fan.speed}

@app.post("/fan/speed/low")
async def fan_speed_low():
    command = FanSpeedLowCommand(fan)
    remote_control.press_button(command)
    return {"speed": fan.speed}

@app.post("/undo")
async def undo():
    remote_control.press_undo()
    return {"status": "Última acción deshecha"}
