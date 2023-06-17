import discord
from discord.ext import commands


class McCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='edit_user')
    async def edit_user(self, ctx):
        pass
    @commands.slash_command(name='mute_user')
    async def mute_user(self, ctx):
        pass
    @commands.slash_command(name='edit_channels')
    async def edit_channels(self, ctx):
        pass
    @commands.slash_command(name='minecraft_command')
    async def minecraft_command(self, ctx):
        pass
    @commands.slash_command(name='link_accounts')
    async def link_accounts(self, ctx):
        pass
    
def setup(bot):
    bot.add_cog(McCmds(bot))
