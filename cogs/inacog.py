from discord.ext import commands

class inacog(commands.Cog):
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
     ans = translator.translate(honyaku.lang, src=detect, dest=jp)
     await ctx.send(ans.text)
                         
def setup(bot):
    bot.add_cog(inacog(bot))
    print('testcog load ok')

    
