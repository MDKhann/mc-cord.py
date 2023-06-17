from subprocess import Popen, PIPE, STDOUT
import threading

class minecraft_server:
    def __init__(self, server_id: str):
        self.server_id = server_id
        self.server_handler_running = False
        self.server_thread = ""
    
    def start_thread(self):
        self.server_thread
    
    def run_minecraft_server(self, settings, temp_settings):
        temp_launch_args = settings["minecraft_servers"][self.server_id]["launch_args"]
        x = Popen("cmd.exe", stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True) 
        x.stdin.write(("cd " + temp_launch_args["path"]).encode())
        x.stdin.flush()
        command = f'{temp_launch_args["javapath"]} -Xmx{temp_launch_args["max_memory"]} -jar {temp_launch_args["server_jar"]} {temp_launch_args["launchargs"]} {temp_launch_args["jvmargs"]}'.encode()#java -jar -Xmx1G -Xms512M server/server.jar -nogui 
        x.stdin.write(b'java -Xmx8G -jar fabric-server-launch.jar\n')
        x.stdin.flush()
        while x.poll() is None:###Problem: because its the cmd --> if server is dead == cmd still active ## maybe create temporary bat/sh file to launch server 
            child_output = (x.stdout.readline()).decode()
            print(child_output)###append to a list that is handled by another process. the process waits if there comes more input for some seconds and checks for max cap of signs