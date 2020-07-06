from discord.ext import commands
import data.data as data_file


class help(commands.Cog):
 async def help(ctx,page):
  send_page = data_file.get_page(page)
  if msg == None:
   msg = await ctx.send(send_page)
  else:
   msg.edit(send_page)
 
  
   

def setup(bot):
 bot.add_cog(help(bot))
