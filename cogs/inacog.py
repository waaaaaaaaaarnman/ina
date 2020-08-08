from discord.ext import commands,tasks
import time
import discord

class inacog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
     await ctx.send(f'pong! took:{self.bot.latency}ms')
    @commands.command()
    async def search(self,ctx,*,key):
     keyword = key.replace(' ','+')
     await ctx.send(f'https://www.google.com/search?q={keyword}')
    @commands.command()
    async def ank(self,ctx,main,sub,*,emoji):
     ankmsgm = discord.Embed(title=main,description=sub)
     ankmsg = await ctx.send(embed=ankmsgm)
     ankid.edit(ankmsgm.add_field(name="以下のコマンドで集計:",value=f't!poll {ankmsg.id}'))
     emojisp = emoji.split()
     for rea in emojisp:
      await ankmsg.add_reaction(rea)
    @commands.command()
    async def poll(self,ctx,id):
     poll = await ctx.fetch_message(int(id))
     reactions = poll.reactions
     for reaction in reactions:
      pollans = f'絵文字:{reaction.emoji} カウント:{reaction.count}'
      await ctx.send(pollans)
    @commands.Cog.listener()
    async def on_message(self,message,ctx):
     for ch in global_ch_list:
      if message.channel.id == ch:     
       await message.delete()
       for channel in global_ch_list:
        ch_webhooks = await channel.webhooks()
        webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)
        if webhook is None:
         await channel.create_webhook(name=GLOBAL_WEBHOOK_NAME)
         await webhook.send(content=message.content,
                            username=message.author.name,
                            avatar_url=message.author.avatar_url_as(format="png"))
def setup(bot):
    bot.add_cog(inacog(bot))
    print('testcog load ok')

   
