from discord.ext import commands

global_channels = [721168485681463350,724477146885521490]

@commands.Cog.listener()
    async def on_message(message):
     if message.channel.id in global_channels:
      await message.delete()
      for channel in global_channels:
       ch_webhooks = await channel.webhooks()
       webhook = discord.utils.get(ch_webhooks, name='test_webhook')
      if webhook is None:
       continue
      await webhook.send(content=message.content,username=message.author.name,avatar_url=message.author.avatar_url_as(format="png")
                         
def setup(bot):
    bot.add_cog(inacog(bot))
