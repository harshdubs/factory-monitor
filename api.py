from fastapi import FastAPI, HTTPException
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
    try:    
        logger.info(f"Sensor data requested for mixer")
        return mixer.get_sesnor_data()
    except Exception as e:
        logger.error(f"Error fetching mixer data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/extruder")
def get_extruder_data():
    try:    
        logger.info(f"Sensor data requested for extruder")
        return extruder.get_sesnor_data()
    except Exception as e:
        logger.error(f"Error fetching extruder data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"status": "FactoryMonitor running"}