from discord.ext import commands,tasks


class glo(commands.Cog):
 @tasks.loop(seconds=3)
 async def lol():
  await bot.change_presence(activity=discord.Game("tes1"))
  await bot.change_presence(activity=discord.Game("tes2"))
  await bot.change_presence(activity=discord.Game("tes3"))
  await bot.change_presence(activity=discord.Game("tes4"))
  
   

def setup(bot):
 bot.add_cog(glo(bot))
 lol.start()
 print('cogok')
