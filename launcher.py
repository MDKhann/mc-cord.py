from subprocess import Popen, PIPE, STDOUT
import discord
import asyncio

import json
import platform

os_name = platform.system()
os_ver = platform.release()


def run_minecraft_server(settings):
    temp_launch_args = settings["minecraft_servers"][(temp_settings["active_server_id"])]["launch_args"]
    x = Popen("cmd.exe", stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True) 
    x.stdin.write(("cd " + temp_launch_args["path"]).encode())
    x.stdin.flush()
    command = f'{temp_launch_args["javapath"]} -Xmx{temp_launch_args["max_memory"]} -jar {temp_launch_args["server_jar"]} {temp_launch_args["launchargs"]} {temp_launch_args["jvmargs"]}'.encode()#java -jar -Xmx1G -Xms512M server/server.jar -nogui 
    x.stdin.write(b'java -Xmx8G -jar fabric-server-launch.jar\n')
    x.stdin.flush()
    while x.poll() is None:
        child_output = (x.stdout.readline()).decode()
        print(child_output)


def load_from_save():
    try:
        with open("config.json", "r") as openfile:
            json_object = json.load(openfile)
        print("Loaded from file")
        
    except Exception:
        print(f"Error in loading config: {Exception}")
        json_object = {"all":{"user_data":{},"settings":{"tokens":{"discord_token":None, "ngrok_token":None},"minecraft_servers":{}}}}
        with open("config.json", "w") as outfile:
            json.dump(json_object, outfile)
    return json_object

def dump_into_save():
    savefile = {"all":{"user_data":user_data, "settings":settings}}
    with open("config.json", "w") as outfile:
        json.dump(savefile, outfile)
    print("Saved to file")

def init_vars():
    global temp_settings, user_data, settings, bot
    bot = discord.Bot()
    intents = discord.Intents.default()
    intents.message_content = True
    temp_settings = {"server_running":False, "active_server_id":"", "IP":"", "rcon_instance":None}
    json_object = load_from_save()
    user_data, settings = json_object["all"]["user_data"], json_object["all"]["settings"]

def import_cogs():
    bot.load_extension('commands.mc_cmds')
    bot.load_extension('commands.ngrok_cmds')
    bot.load_extension('commands.server_cmds')