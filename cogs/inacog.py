from discord.ext import commands

global_channels = [721168485681463350,724477146885521490]

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
    @commands.command()
    async def vc(ctx):
     channel = ctx.get_channel(ctx.VoiceChannel.id)
     vc = await channel.connect()
    @commands.command()
    async def test(ctx):
     ctx.send(ctx.channel.id)
    @commands.Cog.listener()
    async def on_message(message):
     if message.channel.id in global_channels:
      await message.delete()
      for channel in global_channels:
       ch_webhooks = await channel.webhooks()
       webhook = discord.utils.get(ch_webhooks, name='test_webhook')
      if webhook is None:
       continue
      await webhook.send(content=message.content,username=message.author.name,avatar_url=message.author.avatar_url_as(format="png")

def setup(bot):
    bot.add_cog(inacog(bot))

    
