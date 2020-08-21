from discord.ext import commands
import discord
class gban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def gban(self,ctx,banid,banreason):
     if str(ctx.author) == 'Kaede_728#8140':
      for guild in self.bot.guilds:
       await guild.get_member(banid).ban(reason=banreason)
      await ctx.send('gbanが完了しました')
def setup(bot):
    bot.add_cog(gban(bot))
    print('Gban Loaded!')
