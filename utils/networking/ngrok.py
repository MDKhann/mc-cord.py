from pyngrok import conf, ngrok, process
import requests

"""
Add:
    Check for Errors
"""

class ngrok_ip:
    def __init__(self, ngrok_token: str, ngrok_region: str, ngrok_connection: str):
        
        ngrok.install_ngrok()
        
        self.ngrok_token = ngrok_token
        self.ngrok = self.create_ngrok_session(ngrok_token)
        self.ngrok_region = ngrok_region
        self.ngrok_connection = ngrok_connection
        self.ip = self.create_ngrok_ip()

    def create_ngrok_session(self):
        return ngrok.set_auth_token(self.ngrok_token)

    def kill_ngrok(self):
        pass

    def create_tunnel(self):
        conf.get_default().region = self.ngrok_region
        ngrok = ngrok.connect(25565, self.ngrok_connection)
        return(str(ngrok)[20 : 43])