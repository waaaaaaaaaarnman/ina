from discord.ext import commands
import discord
class inacog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
     ping = self.bot.latency
     await ctx.send(f'pong! took:{ping.round}ms')
    @commands.command()
    async def search(self,ctx,*,key):
     keyword = key.replace(' ','+')
     await ctx.send(f'https://www.google.com/search?q={keyword}')
    
     
   
def setup(bot):
    bot.add_cog(inacog(bot))
    print('testcog load ok')

   
