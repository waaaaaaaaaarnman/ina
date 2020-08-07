from discord.ext import commands,tasks
import time

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
    async def ank(ctx,main,sub,*,emoji):
     ankmsgm = discord.Embed(title=main,description=sub)
     ankmsg = await ctx.send(embed=ankmsgm)
     ankid.edit(ankmsgm.add_field(name="以下のコマンドで集計:",value=f't!poll {ankmsg.id}'))
     emojisp = emoji.split()
     for rea in emojisp:
      await ankmsg.add_reaction(rea)
    @commands.command()
    async def poll(ctx,id):
     poll = await ctx.fetch_message(int(id))
     reactions = poll.reactions
     for reaction in reactions:
      pollans = f'絵文字:{reaction.emoji} カウント:{reaction.count}'
      await ctx.send(pollans)
                                  
def setup(bot):
    bot.add_cog(inacog(bot))
    print('testcog load ok')

   
