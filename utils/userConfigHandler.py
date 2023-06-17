import json

default_user_profile = {"default_user_profile": {
                                "admin": False,
                                "commands": {
                                    "select_minecraft_server": False,
                                    "info": True,
                                    "control_server_state": False,
                                    "ip_settings": False,
                                    "edit_user_settings": False,
                                    "mute_users": False,
                                    "minecraft_commands": False,
                                    "add_server": False,
                                    "edit_minecraft_server": False,
                                    "link_account": True
                                },
                                "other": {
                                    "allow_messages_to_server": True,
                                    "linked_minecraft_accounts": []
                                }}
}

default_data = {
    "user_data": {}
}
class Config:
    def __init__(self, filename):
        self.filename = filename

        try:
            with open(filename, 'r') as file:
                self.config = json.load(file)
                self.data = self.config['user_data']
        except Exception:
            print("File not found, creating default file")
            f = open(filename, "w")
            json.dump(default_data, f, indent=4)

    def add_user(self, id):
        self.config[id] = default_user_profile

    def get_user_data(self, id):
        return self.config[id]

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)

config = Config("user_config.json")