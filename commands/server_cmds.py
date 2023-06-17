import discord
from discord.ext import commands


class ServerCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='select_server')
    async def select_server(self, ctx):
        pass

    @commands.slash_command(name='start')
    async def start(self, ctx):
        pass

    @commands.slash_command(name='stop')
    async def stop(self, ctx):
        pass

    @commands.slash_command(name='restart')
    async def restart(self, ctx):
        pass

    @commands.slash_command(name='add_server')
    async def add_server(self, ctx):
        pass

    @commands.slash_command(name='edit_server')
    async def edit_server(self, ctx):
        pass

    @commands.slash_command(name='info')
    async def info(self, ctx):
        pass



def setup(bot):
    bot.add_cog(ServerCmds(bot))
