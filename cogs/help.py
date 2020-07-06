from discord.ext import commands
import .data


class help(commands.Cog):
 @tasks.loop(seconds=3)
 async def loop():
  await bot.change_presence(activity=discord.Game("tes1"))
  await bot.change_presence(activity=discord.Game("tes2"))
  await bot.change_presence(activity=discord.Game("tes3"))
  await bot.change_presence(activity=discord.Game("tes4"))
  
   

def setup(bot):
 bot.add_cog(helq(bot))
