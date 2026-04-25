from fastapi import FastAPI
from machine import Mixer,Extruder
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

mixer = Mixer(100,"Mixer-1", "Mixing Area")
mixer.start()

extruder = Extruder(120, "TTL","Extrusion Area")
extruder.start()


@app.get("/mixer")
def get_mixer_data():
    logger.info(f"Sensor data requested for mixer")
    return mixer.get_sesnor_data()

@app.get("/extruder")
def get_extruder_data():
    logger.info(f"Sensor data requested for extruder")
    return extruder.get_sesnor_data()

@app.get("/")
def root():
    return {"status": "FactoryMonitor running"}