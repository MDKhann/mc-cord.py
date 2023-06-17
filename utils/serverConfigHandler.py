import os
import json

class Config:
    def __init__(self, filename):
        self.filename = filename
        self.load_config()

        self.config = {}

    def load_config(self):
        if not os.path.isfile(self.filename):
            self.create_default_config()
        else:
            with open(self.filename, 'r') as file:
                try:
                    self.config = json.load(file)
                    self.settings = self.config['settings']
                except (json.JSONDecodeError, KeyError):
                    self.create_default_config()

    def create_default_config(self):
        default_config = json.load(open("utils/default_servercfg.json", "r"))
        with open(self.filename, 'w') as file:
            json.dump(default_config, file, indent=4)
            self.config = default_config
            self.settings = self.config['settings']
            file.close()

    def get_minecraft_servers(self):
        return self.settings['minecraft_servers']

    def set_minecraft_servers(self, servers: dict):
        self.settings['minecraft_servers'] = servers

    def get_discord_token(self):
        return self.settings['tokens']['discord_token']

    def set_discord_token(self, token):
        self.settings['tokens']['discord_token'] = token
        self.save_config()

    def get_ngrok_token(self):
        return self.settings['tokens']['ngrok_token']

    def set_ngrok_token(self, token):
        self.settings['tokens']['ngrok_token'] = token
        self.save_config()

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)
            file.close()

config = Config("server_config.json")