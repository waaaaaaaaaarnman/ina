#coding: utf-8

import discord
from discord.ext import commands
import cogs.inacog as inacog

bot = commands.Bot(command_prefix='i!')

#pingコマンド
@bot.command()
async def ping(ctx):
 await ctx.send(f'pong! took:{bot.latency}ms')
#検索コマンド
@bot.command()
async def search(ctx,*,keyword):
 await ctx.send(f'https://www.google.com/search?q={keyword}')
 
#機能時のログ
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)
    await bot.change_presence(activity=discord.Game("てすと"))

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
