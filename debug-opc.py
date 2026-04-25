from opcua import Client

client = Client("opc.tcp://localhost:4840/factory")
client.connect()

root = client.get_root_node()
objects = client.get_objects_node()

for child in objects.get_children():
    print(child, child.get_browse_name())
    for subchild in child.get_children():
        print("  ", subchild, subchild.get_browse_name())
        for tag in subchild.get_children():
            print("    ", tag, tag.get_browse_name())

client.disconnect()