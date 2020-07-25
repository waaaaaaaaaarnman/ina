#coding: utf-8

import discord
from discord.ext import commands
import cogs.inacog as inacog
from discord.ext import tasks
import time
import os

bot = commands.Bot(command_prefix='i!')

@bot.command()
async def test(ctx):
    await ctx.send(ctx.channel.id)

#機能時のログ
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)

bot.run(os.environ["BOT_TOKEN"])
