from opcua import Client

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
    def __init__(self, mixing_speed: float,name,location, opc_client):
        self.mixing_speed = mixing_speed
        self.opc_client = opc_client
        super().__init__(name,location);

    def set_speed(self, new_speed):
        root = self.opc_client.get_root_node()
        node = root.get_child(["0:Objects", "2:Factory", "2:Mixer", "2:mixer_speed"])
        node.set_value(new_speed)
        self.mixing_speed = new_speed

    def get_sesnor_data(self) ->dict:
        root = self.opc_client.get_root_node()
        node = root.get_child(["0:Objects", "2:Factory", "2:Mixer", "2:mixer_vibration"])
        value = node.get_value()
        self.vibration = value
        node = root.get_child(["0:Objects", "2:Factory", "2:Mixer", "2:mixer_temperature"])
        value = node.get_value()
        self.temperature = value 
        return {"speed":self.mixing_speed,"vibration":self.vibration,"temperature":self.temperature}


class Extruder(Machine):
    def __init__(self,temperature : float,name: str,location: str, opc_client):
        self.temperature = temperature
        self.opc_client = opc_client
        super().__init__(name,location)
    
    def set_temperature(self):
        root = self.opc_client.get_root_node()
        node = root.get_child(["0:Objects", "2:Factory", "2:Extruder", "2:extruder_temperature"])
        value =node.get_value()
        self.temperature = value

    def get_sesnor_data(self) -> dict:
        root = self.opc_client.get_root_node()
        node = root.get_child(["0:Objects", "2:Factory", "2:Extruder", "2:extruder_pressure"])
        value =node.get_value()
        self.pressure = value
        
        node = root.get_child(["0:Objects", "2:Factory", "2:Extruder", "2:extruder_output_rate"])
        value =node.get_value()
        self.output_rate = value 
        return {"temperature":self.temperature,"pressure":self.pressure,"output_rate":self.output_rate}