from discord.ext import commands
import discord,json
class globalch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
     with open('datas/global_channel.json','r') as f:
            global_channels = f.load().split()
     if message.author.bot:
        return
     GLOBAL_WEBHOOK_NAME = "ina-global-webhook"
     if message.channel.id == global_channels:
        await message.delete()
        for channel in global_channels:
            ch_webhooks = await channel.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)
            if webhook is None:
             await channel.create_webhook(name=GLOBAL_WEBHOOK_NAME)
            await webhook.send(content=message.content,
                               username=message.author.name,
                               avatar_url=message.author.avatar_url_as(format="png"))
def setup(bot):
    bot.add_cog(globalch(bot))
    print('Global Loaded!')
