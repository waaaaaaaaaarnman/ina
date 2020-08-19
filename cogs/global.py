from discord.ext import commands
import discord
class global(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
     if message.author.bot:
        return
     GLOBAL_CH_NAME = "ina-global"
     GLOBAL_WEBHOOK_NAME = "ina-global-webhook"
    if message.channel.name == GLOBAL_CH_NAME:
        await message.delete()
        channels = self.bot.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        for channel in global_channels:
            ch_webhooks = await channel.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)
            if webhook is None:
             channel.create_webhook(name=GLOBAL_WEBHOOK_NAME)
            await webhook.send(content=message.content,
                               username=message.author.name,
                               avatar_url=message.author.avatar_url_as(format="png"))
def setup(bot):
    bot.add_cog(global(bot))
    print('Global Loaded!')
