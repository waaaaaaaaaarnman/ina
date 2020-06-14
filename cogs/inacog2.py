from discord.ext import commands

class inacog2(commands.Cog):
    @commands.command()
    async def pingu(self, ctx):
     await ctx.send('pongu!')
    @commands.command()
    async def whatis(self, ctx, what):
     await ctx.send(f'{whatis}とは？')
def setup(bot):
    bot.add_cog(inacog2(bot))
