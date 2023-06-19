import os
import subprocess
from _curl.get_curl import get_curl
import platform


class ServerDownloader:
    def __init__(self, folder_name):
        self.folder_name = folder_name

    def create_folder(self):
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

    def download_server(self, server_folder, server_url):
        self.create_folder()
        server_path = os.path.join(self.folder_name, server_folder)
        if not os.path.exists(server_path):
            os.makedirs(server_path)

        server_file_path = os.path.join(server_path, "server.jar")

        if platform.platform().__contains__("Linux"):
            command = ['curl', '-o', server_file_path, '--progress-bar', server_url]
            subprocess.call(command)
            print("Server downloaded successfully!")
        else:
            if os.path.exists("curl/curl-8.1.2_3-win64-mingw/bin"):
                command = ['curl', '-o', server_file_path, '--progress-bar', server_url]
                subprocess.call(command)

                print("Server downloaded successfully!")
            else:
                get_curl()
                command = ['curl', '-o', server_file_path, '--progress-bar', server_url]
                subprocess.call(command)

                print("Server downloaded successfully!")

    def download_fabric_server(self, server_folder):
        fabric_url = "https://meta.fabricmc.net/v2/versions/loader/1.20.1/0.14.21/0.11.2/server/jar"  # Replace with actual Fabric server download URL
        self.download_server(server_folder, fabric_url)

    def download_vanilla_server(self, server_folder):
        vanilla_url = "https://piston-data.mojang.com/v1/objects/84194a2f286ef7c14ed7ce0090dba5my9902951553/server.jar"  # Replace with actual Vanilla server download URL
        self.download_server(server_folder, vanilla_url)
