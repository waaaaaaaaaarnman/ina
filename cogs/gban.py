from discord.ext import commands
import discord
class gban(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
 @commands.group()
 async def gban(self,ctx):
  if ctx.invoked_subcommand is None:
   await ctx.send('このコマンドにはサブコマンドが必要です。')
 @gban.command()
 async def chusei(self,ctx,banorunban,banid,banreason):
    await self.bot.get_channel(745918268308717568).send(f'{ctx.author}さんが{banorunban}を申請しています。Id:{banid}理由:{banreason}')
 @gban.command()
 async def gban(self,ctx,banorunban,banid,banreason):
  bandata = await self.bot.get_channel(745805249779990648).fetch_message(745906962197381140)
  await bandata.edit(content=f'{bandata.content} {banorunban}:{banid}:{banreason}')
def setup(bot):
 bot.add_cog(gban(bot))
    print('Gban Loaded!')
