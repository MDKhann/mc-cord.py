import discord
from discord.ext import commands
from typing import List

class Bot(discord.Bot):
    def __init__(self, token: str, *cogs: List[str]):
        intents = discord.Intents.all()
        super().__init__(intents=intents)

        self.token = token
        self.cogs_to_load = cogs

    async def on_ready(self):
        print(f'Bot is ready. Logged in as {self.user}')
        for cog in self.cogs_to_load:
            try:
                self.load_extension(cog)
                print(f'Loaded cog: {cog}')
            except Exception as e:
                print(f'Error loading cog {cog}: {e}')

    async def send_message(self, channel_id: str, message:str):
        channel = self.get_channel(channel_id)
        await channel.send(message)

    

    def run_bot(self):
        self.run(self.token)
