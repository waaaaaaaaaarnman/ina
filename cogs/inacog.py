from discord.ext import commands

class inacog(commands.Cog):
    @commands.command()
    async def ping(self, ctx):
     await ctx.send('pong!')
    @commands.command()
    async def what(self, ctx, what):
     await ctx.send(f'{what}とはなんですか？')
def setup(bot):
    bot.add_cog(inacog(bot))

    
