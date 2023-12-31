from subprocess import Popen, PIPE, STDOUT
import threading
import platform

class minecraft_server:
    def __init__(self, modules: dict):
        self.server_id = ""
        self.server_state = "off"
        self.server_thread = threading.Thread(target=self.minecraft_server_thread, daemon=True)
        self.modules = modules
        self.start_file = ""
        self.platform = platform.system()
        self.platform_raw = platform.platform()
    
    def start_server_thread(self, server_id: str=""):
        if self.server_state == "off":
            if server_id:
                self.server_id = server_id
            if not self.start_file:
                self.create_start_file()
            self.server_thread.start()
            self.server_state = "booting"
    
    def create_start_file(self):
        """
        TODO:https://minecraft.fandom.com/wiki/Tutorials/Setting_up_a_server # Look for "Minecraft options"
        |--> add more arguments
        """
        launch_args = self.modules["serverConfigHandler"].get_minecraft_servers()[f"{self.server_id}"]
        if self.platform == "Windows":
            with open("launch.bat", "w") as outfile:
                self.write_to_file(outfile, launch_args, "Exit /B")
            self.start_file = "launch.bat"
        elif self.platform("Linux"):
            with open("launch.sh", "w") as outfile:
                self.write_to_file(outfile, launch_args, "exit 0")
            self.start_file = "launch.sh"
        else:
            print("OS is not compatible")

    def write_to_file(self, outfile, launch_args, exit_command):
        outfile.write("cd " + launch_args["path"] + "\n")
        outfile.write(f'{launch_args["javapath"]} -Xmx{launch_args["max_memory"]} -jar {launch_args["server_jar"]} {launch_args["launchargs"]} {launch_args["jvmargs"]}\n')
        outfile.write(exit_command)
        outfile.close()
    
    def minecraft_server_thread(self):
        cmd_subprocess = Popen(f"{self.start_file}", stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
        while cmd_subprocess.poll() is None:
            child_output = (cmd_subprocess.stdout.readline()).decode()
            self.modules["mcServerOutputHandler"].mcOutputQueue.append(child_output)
            print(child_output)
        self.server_state = "off"
        self.start_file = ""