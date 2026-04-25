from opcua import Server
import time
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/factory")

objects = server.get_objects_node()

idx = server.register_namespace("factory")

factory = objects.add_object(idx, "Factory")
mixer = factory.add_object(idx, "Mixer")
extruder = factory.add_object(idx, "Extruder")

#tags                        
mixer_speed = mixer.add_variable(idx, "mixer_speed", 100.0)
mixer_speed.set_writable()

mixer_temperature = mixer.add_variable(idx, "mixer_temperature", 156.2)
mixer_temperature.set_writable()

mixer_vibration = mixer.add_variable(idx, "mixer_vibration", 0.6)
mixer_vibration.set_writable()

extruder_outputrate = extruder.add_variable(idx, "extruder_output_rate", 23)
extruder_outputrate.set_writable()

extruder_temperature = extruder.add_variable(idx, "extruder_temperature", 122.3)
extruder_temperature.set_writable()

extruder_pressure = extruder.add_variable(idx, "extruder_pressure", 5.3)
extruder_pressure.set_writable()

server.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    server.stop()
