import discord

from discord.ext import commands
from utils.userConfigHandler import config

class Onmsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx: discord.ApplicationContext):
        id = str (ctx.author.id) 
        data = config.get_user_data(id)
        muted = data[id]['other']['allow_messages_to_server']
        if muted == True:
            muted=False
        elif muted == False:
            muted=True
        

def setup(bot):
    bot.add_cog(Onmsg(bot))