from discord.ext import commands

class inacog(commands.Cog):
    @commands.command()
    async def pin2g(ctx):
     await ctx.send(f'pong!{bot.latency}')
    @commands.command()
    async def what(ctx, what):
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
                         
def setup(bot):
    bot.add_cog(inacog(bot))

    
