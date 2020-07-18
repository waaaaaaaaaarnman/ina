#coding: utf-8
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='i!')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def ping(ctx):
 await ctx.send(f'pong!{bot.latency}')

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
