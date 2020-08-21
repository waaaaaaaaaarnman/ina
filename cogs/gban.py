from discord.ext import commands
import discord
class gban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def gban(self,ctx,banid,banreason):
        
def setup(bot):
    bot.add_cog(gban(bot))
    print('Gban Loaded!')
