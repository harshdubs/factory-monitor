from fastapi import FastAPI, HTTPException
from machine import Mixer,Extruder
import logging
import os
from pydantic import BaseModel
from opcua import Client

opc_client = Client("opc.tcp://localhost:4840/factory")
opc_client.connect()


class MixerData(BaseModel):
    speed: float
    vibration: float
    temperature : float

class ExtruderData(BaseModel):
    temperature: float
    pressure: float
    output_rate : float

class SpeedCommand(BaseModel):
    speed: float

mixer_speed = int(os.environ.get("MIXER_SPEED", "100"))
extruder_speed = int(os.environ.get("EXTRUDER_TEMP", "120"))

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

mixer = Mixer(mixer_speed,"Mixer-1", "Mixing Area",opc_client)
mixer.start()

extruder = Extruder(extruder_speed, "TTL","Extrusion Area",opc_client)
extruder.start()


@app.get("/mixer", response_model=MixerData)
def get_mixer_data() -> MixerData: 
    try:    
        logger.info(f"Sensor data requested for mixer")
        return mixer.get_sesnor_data()
    except Exception as e:
        logger.error(f"Error fetching mixer data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/extruder", response_model=ExtruderData)
def get_extruder_data():
    try:    
        logger.info(f"Sensor data requested for extruder")
        return extruder.get_sesnor_data()
    except Exception as e:
        logger.error(f"Error fetching extruder data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/mixer/speed/")
def set_mixer_speed(command: SpeedCommand):
    try:
        mixer.set_speed(command.speed)    
        logger.info(f"Speed updated")
        return {"message": "speed updated", "new_speed": command.speed}
    except Exception as e:
        logger.error(f"Error setting mixer speed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def root():
    return {"status": "FactoryMonitor running"}