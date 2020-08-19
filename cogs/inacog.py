from discord.ext import commands
import discord
class inacog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
     await ctx.send(f'pong! took:{round(self.bot.latency,1)}ms')
    @commands.command()
    async def search(self,ctx,*,key):
     keyword = key.replace(' ','+')
     await ctx.send(f'https://www.google.com/search?q={keyword}')
    @commands.command()
    async def update_notice(self,ctx):
     await self.bot.get_channel(745531061160640572).follow(destination=ctx.channel)
     await ctx.send("アナウンスチャンネルをフォローしたよ！")
     
   
def setup(bot):
    bot.add_cog(inacog(bot))
    print('testcog load ok')

   
