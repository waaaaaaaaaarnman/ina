from discord.ext import commands
import discord
class globalch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def global_chat_on(self,ctx):
      await ctx.channel.create_webhook(name='ina-global-webhook')
      datach = self.bot.get_channel(745805249779990648)
      globaldata = await datach.fetch_message(745814673265393794)
      await globaldata.edit(content=f'{globaldata.content} {ctx.channel.id}')
      await ctx.send('グローバルチャットに接続できました!')
    @commands.command()
    async def global_chat_off(self,ctx):
        datach = self.bot.get_channel(745805249779990648)
        globaldata = await datach.fetch_message(745814673265393794)
        await globaldata.edit(content=globaldata.content.replace(str(ctx.channel.id),''))
        webhooks = await ctx.channel.webhooks()
        webhookk = discord.utils.get(webhooks, name='ina-global-webhook')
        await webhookk.delete()
        await ctx.send('グローバルチャットから切断できました!')
    @commands.Cog.listener()
    async def on_message(self, message):
     if message.author.bot:
        return
     global_ch = self.bot.get_channel(745805249779990648)
     global_channel = await global_ch.fetch_message(745814673265393794)
     global_channels = global_channel.content.split()
     GLOBAL_WEBHOOK_NAME = "ina-global-webhook"
     for globalch in global_channels:
      if str(message.channel.id) == globalch:
        await message.delete()
        for channel in global_channels:
            channeldata = self.bot.get_channel(int(channel))
            ch_webhooks = await channeldata.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)
            await webhook.send(content=message.content,
                               username=message.author.name,
                               avatar_url=message.author.avatar_url_as(format="png"))
def setup(bot):
    bot.add_cog(globalch(bot))
    print('Global Loaded!')
