import random


class Machine:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.status = "stopped"

    def start(self):
        self.status = "Started"

    def stop(self):
        self.status = "Stopeed"

    def get_status(self):
        print(self.status)

class Mixer(Machine):
    def __init__(self, mixing_speed,name,location):
        self.mixing_speed = mixing_speed
        super().__init__(name,location)

    def set_speed(self,speed):
        self.mixing_speed = speed

    def get_sesnor_data(self):
        self.vibration = random.uniform(0.1,0.5)
        self.temperature = random.uniform(60,120)
        return {"speed":self.mixing_speed,"vibration":self.vibration,"temperature":self.temperature}


class Extruder(Machine):
    def __init__(self,temperature,name,location):
        self.temperature = temperature
        super().__init__(name,location)
    
    def set_temperature(self):
        self.temperature = random.uniform(60,120)

    def get_sesnor_data(self):
        self.pressure = random.uniform(10,100)
        self.output_rate = random.uniform(5,50)
        return {"temperature":self.temperature,"pressure":self.pressure,"output_rate":self.output_rate}