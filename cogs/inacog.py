from discord.ext import commands,tasks
import time

class inacog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
     await ctx.send(f'pong! took:{self.bot.latency}ms')
    @commands.command()
    async def search(self,ctx,*,key):
     keyword = key.replace(' ','+')
     await ctx.send(f'https://www.google.com/search?q={keyword}')
    @commands.command()
    async def honyaku(self,ctx,*,honyaku):
     from googletrans import Translator
     translator = Translator()
     detect = translator.detect(honyaku)
     ans = translator.translate(honyaku, src=detect, dest=jp)
     await ctx.send(ans.text)

def setup(bot):
    bot.add_cog(inacog(bot))
     @tasks.loop(seconds=40)
     async def loop():
      await bot.change_presence(activity=discord.Game(f"導入サーバー数:{len(self.bot.guilds)}"))
      time.sleep(10)
      await bot.change_presence(activity=discord.Game("てすと"))
      time.sleep(10)
      await bot.change_presence(activity=discord.Game("てすと"))
      time.sleep(10)
      await bot.change_presence(activity=discord.Game("てすと"))
      time.sleep(10)          
    loop.start()
    print('testcog load ok')

    
