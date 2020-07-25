#coding: utf-8

import discord
from discord.ext import commands,tasks
import cogs.inacog as inacog
import os
import time

bot = commands.Bot(command_prefix='i!')

@tasks.loop(seconds=40)
async def loop():
      await bot.change_presence(activity=discord.Game(f"導入サーバー数:{len(self.bot.guilds)}"))
      time.sleep(10)
      await bot.change_presence(activity=discord.Game("てすと"))
      time.sleep(10)
      await bot.change_presence(activity=discord.Game("てすと"))
      time.sleep(10)
      await bot.change_presence(activity=discord.Game("てすと"))
      time.sleep(10)          
  
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)

loop.start()
bot.run(os.environ["BOT_TOKEN"])
