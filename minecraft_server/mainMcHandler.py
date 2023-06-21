import threading

"""
notes:
--------
when starting up, change to default status
check if port exists multiple times
create AND add server function
--------
serverproperties = allow-flight=false
allow-nether=true
broadcast-console-to-ops=true
broadcast-rcon-to-ops=true
difficulty=normal
enable-command-block=false
enable-jmx-monitoring=false
enable-query=false
enable-rcon=true
enable-status=true
enforce-secure-profile=true
enforce-whitelist=false
entity-broadcast-range-percentage=100
force-gamemode=false
function-permission-level=2
gamemode=survival
generate-structures=true
generator-settings={}
hardcore=false
hide-online-players=false
initial-disabled-packs=
initial-enabled-packs=vanilla
level-name=world
level-seed=
level-type=minecraft\:normal
max-chained-neighbor-updates=1000000
max-players=69420
max-tick-time=60000
max-world-size=29999984
motd=§5Willkommen bei§4§l Gboard\!§5 Texte, die Sie hier§4 kopieren,§5 werden§4 hier§5 gespeichert.
network-compression-threshold=256
online-mode=true
op-permission-level=4
player-idle-timeout=0
prevent-proxy-connections=false
pvp=true
query.port=25565
rate-limit=0
rcon.password=cool
rcon.port=25575
require-resource-pack=false
resource-pack=
resource-pack-prompt=
resource-pack-sha1=
server-ip=
server-port=25565
simulation-distance=10
spawn-animals=true
spawn-monsters=true
spawn-npcs=true
spawn-protection=16
sync-chunk-writes=true
text-filtering-config=
use-native-transport=true
view-distance=10
white-list=false
"""
all_vars = {
    "active":{
        "servers":[],
        "ports":[]
    },
    "all_servers":{
        "<server_id>":{
            "basic_info":{
                "server_name":"",
                "server_description":"",
                "minecraft_version":"",
                },
            "server_properties":{
                ### server.properties
            },
            "launch_config":{
                "server_path":"",
                "java_path":"",
                "max_memory":"",
                "jvmargs": "",
                "launchargs": "",
                "server_jar":"", #full path #why?: because better, and u can use the same jar for multiple servers then (saves storage) #users can choose from downloaded jars folder
            },
            "status":{
                "minecraft_server_status":"Offline",
                "minecraft_server_players":{},
                "minecraft_server_playercount":"",
                "minecraft_server_active_log":[]
            },
            "networking":{
                "minecraft_port":25565,
                "rcon_port":25575,
                "rcon_password":"",#NEEDS A PASSWORD
                "discord":{
                    "use_bot":True,
                    "bot_token":"<bot_token>",
                    "channels":{
                        "<channel_id>":{
                            "use_this_channel":True,
                            "discord_to_minecraft":True,
                            "minecraft_to_discord":{
                                "messages":True,
                                "death_notes":True,
                                "join_leave":True,
                                "achievements":True,
                                "warns":False,
                                "errors":False
                            },
                        },
                    },
                },
                "ngrok":{
                    "use_ngrok":True,
                    "ngrok_token":"<ngrok_token>",
                    "ngrok_ip":""
                }
            }
        }
    }
}


class mainMcHandler:
    def __init__(self):
        pass
    
    def update_server_list(self):pass
    
    def update_thread(self):pass