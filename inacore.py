#coding: utf-8
import discord
from discord.ext import commands
from discord.ext import tasks
import time

bot = commands.Bot(command_prefix='i!')

@tasks.loop(seconds=40)
async def loop():
 await bot.change_presence(activity=discord.Game("てすと"))
 time.sleep(10)
 await bot.change_presence(activity=discord.Game("てすとと"))
 time.sleep(10)
 await bot.change_presence(activity=discord.Game("てすととと"))
 time.sleep(10)
 await bot.change_presence(activity=discord.Game("てすとととと"))
 time.sleep(10)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    loop.start()
    
@bot.command()
async def ping(ctx):
 await ctx.send(f'pong!{bot.latency}')

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
