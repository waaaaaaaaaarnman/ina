#coding: utf-8

import discord
from discord.ext import commands
import cogs.inacog as inacog
from discord.ext import tasks
import time

bot = commands.Bot(command_prefix='i!')

@bot.command()
async def test(ctx):
    await ctx.send(ctx.channel.id)

@tasks.loop(seconds=40)
async def loop():
 await bot.change_presence(activity=discord.Game("てすと"))
 time.sleep(10)
 await bot.change_presence(activity=discord.Game("てすと"))
 time.sleep(10)
 await bot.change_presence(activity=discord.Game("てすと"))
 time.sleep(10)
 await bot.change_presence(activity=discord.Game("てすと"))
 time.sleep(10)
#機能時のログ
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
