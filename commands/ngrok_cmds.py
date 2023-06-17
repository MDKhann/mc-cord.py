import discord
from discord.ext import commands


class NgrokCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ngrok_settings')
    async def ngork_settings(self, ctx):
        pass

    @commands.slash_command(name='new_ip')
    async def new_ip(self, ctx):
        pass


def setup(bot):
    bot.add_cog(NgrokCmds(bot))
