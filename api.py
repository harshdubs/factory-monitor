from fastapi import FastAPI
from machine import Mixer,Extruder

app = FastAPI()

@app.get("/")
def root():
    return {"status": "FactoryMonitor running"}

mixer = Mixer(100,"Mixer-1", "Mixing Area")
mixer.start()

extruder = Extruder(120, "TTL","Extrusion Area")
extruder.start()


@app.get("/mixer")
def get_mixer_data():
    return mixer.get_sesnor_data()

@app.get("/extruder")
def get_extruder_data():
    return extruder.get_sesnor_data()