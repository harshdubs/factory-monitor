import random


class Machine:
    def __init__(self,name: str,location: str):
        self.name = name
        self.location = location
        self.status = "stopped"

    def start(self) -> None:
        self.status = "Started"

    def stop(self)-> None:
        self.status = "Stopeed"

    def get_status(self)-> str:
        print(self.status)

class Mixer(Machine):
    def __init__(self, mixing_speed: float,name,location):
        self.mixing_speed = mixing_speed
        super().__init__(name,location)

    def set_speed(self,speed: float):
        self.mixing_speed = speed

    def get_sesnor_data(self) ->dict:
        self.vibration = random.uniform(0.1,0.5)
        self.temperature = random.uniform(60,120)
        return {"speed":self.mixing_speed,"vibration":self.vibration,"temperature":self.temperature}


class Extruder(Machine):
    def __init__(self,temperature : float,name: str,location: str):
        self.temperature = temperature
        super().__init__(name,location)
    
    def set_temperature(self):
        self.temperature = random.uniform(60,120)

    def get_sesnor_data(self) -> dict:
        self.pressure = random.uniform(10,100)
        self.output_rate = random.uniform(5,50)
        return {"temperature":self.temperature,"pressure":self.pressure,"output_rate":self.output_rate}