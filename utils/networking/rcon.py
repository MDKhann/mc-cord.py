from mcrcon import MCRcon, MCRconException
from string import printable

"""
In server.properties change settings so that rcon works
"""

class rcon:
    def __init__(self, modules: dict):
        self.modules = modules
        self.create_rcon_session()

    def create_rcon_session(self):
        """
        rework for modules dict
        """
        temp_launch_args = self.settings["minecraft_servers"][(self.temp_settings["active_server_id"])]["rcon"]
        try:
            self.rcon_session = MCRcon(temp_launch_args["IP"], temp_launch_args["password"])
            self.rcon_session.connect()
        except MCRconException:
            print(f"Error in creating rcon session: {MCRconException}")
        except Exception:
            print(f"Error in creating rcon session: {Exception}")

    def server_info(self):
        """
        retrieve infos about the server with self.send_command()
        """
        pass
    
    def send_message(self, ctx, data: str, receiver: str="@a"):## message length cap
        message = (
            'tellraw '
            + receiver
            + ' ["",{"text":"[", "color":"white","bold":false},{"text":"Discord","color":"dark_purple","bold":true},{"text":"]['
            + ctx.author.name
            + ']: '
            + data
            + '", "color":"white","bold":false}]'
        )
        return(self.send_error_handler(message))
    
    def send_command(self, data: str):
        return self.send_error_handler(data)
    
    def send_error_handler(self, data: str):
        try:
            return self.rcon_session.command(data)
        except MCRconException:
            print(f"Error in Rcon: {MCRconException}")
            self.create_rcon_session()
            try:
                return self.rcon_session.command(data)
            except MCRconException:
                return f"Something went wrong with rcon: {MCRconException}"
        except Exception:
            print(f"Error in Rcons connection: {Exception}")
            self.create_rcon_session()
            try:
                return self.rcon_session.command(data)
            except MCRconException:
                return f"Something went wrong with rcon: {MCRconException}"
    
    
        


test_dict = {"minecraft_servers":{"101":{"rcon":{"IP":"localhost", "password":"cool"}}}}
temp_test_dict = {"active_server_id":"101"}

test_rcon = rcon(settings=test_dict, temp_settings=temp_test_dict)
while True:
    print(test_rcon.send_command(input("command:")))
"""https://minecraft.tools/en/tellraw.php?tellraw=%3Ca%20data-runcommand%3D%22%2Fkill%20%40s%22%20class%3D%22runcommand%22%20href%3D%22%2Fkill%20%40s%22%3EDownload%20the%20new%20mods%20HERE!%3C%2Fa%3E&selector=%40a"""
"""
'["",{"text":"[", "color":"white","bold":false},{"text":"Discord","color":"dark_purple","bold":true},{"text":"][Apocorn]: Hello", "color":"white","bold":false}]'
{"Haflix has made the advancement ", "color":"white"}{"text":"[Serious Dedication]", "color":"dark_purple","hoverEvent":{"action":"show_text","value":{"text":"Use a Netherite Ingot to upgrade a Hoe, and then reevaluate your life choices", "color":"dark_purple"}}
/tellraw @a ["",{"text":"Haflix has made the advancement "},{"text":"[Serious Dedication]", "color":"dark_purple","hoverEvent":{"action":"show_text","value":"Use a Netherite Ingot to upgrade a Hoe, and then reevaluate your life choices"}}]
/tellraw @a ["",{"text":"[Server: Set Pixx_Unic's game mode to Noob Mode]", "color":"gray","italic":true}]
/tellraw @a ["",{"text":"Haflix joined the game", "color":"yellow"}]
tellraw: https://minecraft.fandom.com/wiki/Raw_JSON_text_format
good commands:
    list
"""

