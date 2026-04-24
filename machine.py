


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

    def set_speed(self,speed,name):
        self.mixing_speed = speed
        print(f"Mixer {self.name} speed set to {self.mixing_speed}")

class Extruder(Machine):
    def __init__(self,temperature,name,location):
        self.temperature = temperature
        super().__init__(name,location)
    
    def set_temperature(self,temperature,name):
        self.temperature = temperature
        print(f"Extruder {self.name} temperature set to {self.temperature}")