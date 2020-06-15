#coding: utf-8
import discord
import cogs.inacog as inacog
import cogs.inacog2 as inacog2
from discord.ext import commands

bot = commands.Bot(command_prefix='i!',command=None)
bot.remove_command("help")
@bot.event
async def command_not_found(self,string):
    return f"{string} というコマンドは存在しません。"
@bot.event
async def on_command_error(ctx, error):
 return f'{error}が発生しました'
    

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)
    inacog2.setup(bot)
bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.XuRqJQ.sesJjpbvS2ojf9fiJ-FJ0kFZbpk')
