import javaproperties

def server_properties_reader_2(filename):
    with open(filename, 'rb') as config_file:
        server_properties = javaproperties.load(config_file)
    print(server_properties)
    return server_properties

def server_properties_writer(filename, obj):
    with open(filename, 'w') as config_file:
        javaproperties.dump(obj, config_file, comments="Minecraft server properties\n#Fri Jun 16 16:26:27 CEST 2023", timestamp=False, ensure_ascii=False, ensure_ascii_comments=False)

def properties_extractor(filename: str):
    try:
        with open(filename, 'r') as f:

            data = f.read_lines()
            vares = data.split('\n')
            print(vars)

    except Exception:
        print("File not found")

#server_properties_reader()
props = server_properties_reader_2("./vars/server.properties")
props["max-players"] = "1"
props = list(props.items())
print(props)
server_properties_writer("new_properties.properties", props)
