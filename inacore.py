#coding: utf-8
import discord
import cogs.inacog as inacog
import cogs.inacog2 as inacog2
from discord.ext import commands
import time
bot = commands.Bot(command_prefix='i!',command=None)
bot.remove_command("help")
def test():
 while True:
     await bot.change_presence(activity=discord.Game("."))
     time.sleep(0.5)
     await bot.change_presence(activity=discord.Game(".."))
     time.sleep(0.5)
     await bot.change_presence(activity=discord.Game("..."))
     time.sleep(0.5)
     await bot.change_presence(activity=discord.Game("...."))
     time.sleep(0.5)
@bot.event
async def on_command_error(ctx, error):
 await ctx.send(f'{error}が発生しました')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)
    inacog2.setup(bot)
    test()
    
bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
