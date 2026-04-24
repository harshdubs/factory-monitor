import time
from machine import Mixer,Extruder

mixer = Mixer(100,"Mixer-1", "Mixing Area")
mixer.start()

extruder = Extruder(120, "TTL","Extrusion Area")
extruder.start()

for i in range(4):
    print(mixer.get_sesnor_data())
    print(extruder.get_sesnor_data())
    time.sleep(1)
