from discord.ext import commands

global_channels = [721168485681463350,724477146885521490]

class glo(commands.Cog):
 @commands.command
 async def teest(ctx):
  ctx.send('teest')
                         
def setup(bot):
 bot.add_cog(glo(bot))
