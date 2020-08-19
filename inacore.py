#coding: utf-8
import discord
from discord.ext import commands,tasks
import cogs.inacog as inacog
import cogs.status as status
import cogs.globalch as globa
import os
bot = commands.Bot(command_prefix='i!')
@bot.event
async def on_command_error(ctx,error):
 await ctx.send(f'エラーが発生しました。エラー:{error}')
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
