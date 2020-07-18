#coding: utf-8
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='i!')

@bot.command()
async def ping(ctx):
 await ctx.send(f'pong!{bot.latency}')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game("てすと"))

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
