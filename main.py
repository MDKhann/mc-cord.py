import subprocess

server_process = None
command = "cmd server/start.bat"

def start_server():
    global server_process
    if server_process is None or server_process.poll() is not None:
        server_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        
        print("Minecraft server is starting.")
        while True:
            line = server_process.stdout.readline()
            if line:
                print(line)
            if server_process.poll() is not None:
                break
# can u create shared terminal
def stop_server():
    global server_process
    if server_process is not None and server_process.poll() is None:
        server_process.stdin.write("stop\n")
        server_process.stdin.flush()
        server_process.wait()
        print("Minecraft server stopped.")
        server_process = None
    else:
        print("No Minecraft server is currently running.")

def send_command(command):
    global server_process
    if server_process is not None and server_process.poll() is None:
        server_process.stdin.write(command + "\n")
        server_process.stdin.flush()
    else:
        print("No Minecraft server is currently running.")
start_server() 