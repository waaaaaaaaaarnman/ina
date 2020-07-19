#coding: utf-8
import discord
from discord.ext import commands
from discord.ext import tasks
import time

bot = commands.Bot(command_prefix='i!')

#pingコマンド
@bot.command()
async def ping(ctx):
 await ctx.send(f'pong! took:{bot.latency}ms')
@bot.command()
async def run(ctx,*,cmd):
 run(cmd)
 await ctx.send(sys.stdout)
#機能時のログ
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game("てすと1"))

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
