from discord.ext import commands

class inacog(commands.Cog):
    @commands.command()
    async def ping(self, ctx):
     await ctx.send('pong!')
    @commands.command()
    async def what(self, ctx, what):
     await ctx.send(f'{what}とはなんですか？')
    @commands.command()
    async def honyaku(self,ctx,honyaku):
     from googletrans import Translator
     translator = Translator()
     aaa = translator.translate(honyaku, src='en', dest='ja')
     await ctx.send(aaa.text)
    @commands.command()
    async def errortest(ctx):
        prin('test')
    
    
     
    @commands.Cog.listener()
    async def on_message(self, message):
     if message.author.bot:
            return
     if message.content == 'hello':
            await message.channel.send('hello')
def setup(bot):
    bot.add_cog(inacog(bot))

    
