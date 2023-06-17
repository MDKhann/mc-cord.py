import os

class ServerProperties:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.properties = {}
        if os.path.isfile(file_path):
            self.load_properties()
        else:
            print("File not found.")

    def load_properties(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    self.properties[key] = value
    
    def get_property(self, key):
        return self.properties.get(key)
    
    def set_property(self, key, value):
        self.properties[key] = value
        self.save_properties()
    
    def save_properties(self):
        with open(self.file_path, 'w') as file:
            for key, value in self.properties.items():
                file.write(f"{key}={value}\n")

props = ServerProperties('new_properties.properties')
motd = props.get_property('motd')

with open("test", "w") as f:
    f.write(motd)
    f.close()