from discord.ext import commands
import discord
class gban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def gban(self,ctx,banid,banreason):
     if str(ctx.author) == 'Kaede_728#8140':
       await self.bot.fetch_user(int(banid)).ban(reason=banreason)
       await ctx.send('gbanが完了しました')
    @commands.command()
    async def ungban(self,ctx,ungbanid,ungbanreason):
      if str(ctx.author) == 'Kaede_728#8140':
       await self.bot.fetch_user(int(banid)).unban(reason=ungbanreason)
       await ctx.send('ungbanが完了しました')
def setup(bot):
    bot.add_cog(gban(bot))
    print('Gban Loaded!')
