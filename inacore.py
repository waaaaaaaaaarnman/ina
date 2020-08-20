#coding: utf-8
import discord
from discord.ext import commands,tasks
import cogs.inacog as inacog
import cogs.status as status
import cogs.globalch as globa
import os
bot = commands.Bot(command_prefix='i!',help_command=None)
bot.remove_command("help")
@bot.event
async def on_command_error(ctx,error):
 errorembed = discord.Embed(title='Error!',description=str(error),color=discord.Colour.from_rgb(166,8,8))
 await ctx.send(embed=errorembed)
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
@bot.event
async def on_member_join(member):
 bandata = await self.bot.get_channel(745805249779990648).fetch_message(745906962197381140)
 listban = bandata.split()
 listbanr = listban.split(':')
 for bann in listban:
   if bann[0] == str(member.id):
    banuser = self.bot.fetch_user(member.id)
    await ban(banuser,f'Ina Gban SystemによってGbanされました。理由:{bann[1]})
bot.run(os.environ["BOT_TOKEN"])
