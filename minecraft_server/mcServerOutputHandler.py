class server_output_handler:
    """
    if detect server loaded --> start rcon
    """
    def __init__(self, modules: dict):
        self.modules = modules
        self.mcOutputQueue = []
        
    def new_line(self, data: str):
        pass