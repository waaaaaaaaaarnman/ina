from discord.ext import commands

class inacog(commands.Cog):
    @commands.command()
    async def ping(self, ctx):
     await ctx.send('pong!{0}'.format(round(commands.latency,1)))
    @commands.command()
    async def what(self, ctx, what):
     await ctx.send(f'{what}とはなんですか？')
    @commands.command()
    async def honyaku(self,ctx,geng1,geng2,*,honyaku):
     from googletrans import Translator
     translator = Translator()
     aaa = translator.translate(honyaku, src=geng1, dest=geng2)
     await ctx.send(aaa.text)
    
    
     
    @commands.Cog.listener()
    async def on_message(self, message):
     if message.author.bot:
            return
     if message.content == 'hello':
            await message.channel.send('hello')
     global voich
     # 接続
     if message.content.startswith('/connect'):
      voich = await discord.VoiceChannel.connect(message.author.voice.channel)
     # 切断
     if message.content.startswith('/discon'):
      await voich.disconnect()
def setup(bot):
    bot.add_cog(inacog(bot))

    
