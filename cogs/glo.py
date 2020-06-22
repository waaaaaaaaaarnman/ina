from discord.ext import commands

global_channels = ['721168485681463350','724477146885521490']

class glo(commands.Cog):
 @commands.Cog.listener()
 async def on_message(ctx,message):
  if message.channel.id in global_channels:
   for channel in global_channels:
    ch_webhooks = await channel.webhooks()
    webhook = discord.utils.get(ch_webhooks, name='test_webhook')
    if webhook is None:
     continue
    await webhook.send(content=message.content,
    username=message.author.name,
    avatar_url=message.author.avatar_url_as(format="png"))
    await bot.process_commands(message)

def setup(bot):
 bot.add_cog(glo(bot))
