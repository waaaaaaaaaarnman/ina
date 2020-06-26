from discord.ext import commands

global_channels = [721168485681463350,724477146885521490]

class glo(commands.Cog):
 @commands.Cog.listener()
 async def on_message(ctx,message):
  if message.channel.id in global_channels:
   for channel in global_channels:
     messch = client.get_channel(channel)
     await messch.send(message.content)
    

def setup(bot):
 bot.add_cog(glo(bot))
