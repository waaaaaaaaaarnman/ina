from discord.ext import commands
import discord
class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
def setup(bot):
    bot.add_cog(status(bot))
    print(' Loaded!')
