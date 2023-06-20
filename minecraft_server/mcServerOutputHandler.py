import asyncio

class server_output_handler:
    """
    1.if detect server loaded --> start rcon
    """
    def __init__(self, modules: dict):
        self.modules = modules
        self.mcOutputQueue = []
        
    async def new_input(self, data: str):
        pass
    
    async def send_input(self, message_dict: dict):
        pass