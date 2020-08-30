#coding: utf-8
import discord,os
from discord.ext import commands
import cogs.inacog as inacog
import cogs.status as status
import cogs.globalch as globa
bot = commands.Bot(command_prefix='i!',help_command=None)
bot.remove_command("help")
@bot.event
async def on_command_error(ctx,error):
 try:
  errorembed = discord.Embed(title='Error!',description=str(error),color=discord.Colour.from_rgb(166,8,8))
  await ctx.send(embed=errorembed)
 except RecursionError:
  break
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)
    status.setup(bot)
    globa.setup(bot)
bot.run(os.environ["BOT_TOKEN"])
