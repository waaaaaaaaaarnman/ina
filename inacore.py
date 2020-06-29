#coding: utf-8
import discord
import cogs.inacog as inacog
import cogs.inacog2 as inacog2
import cogs.glo as glo
from discord.ext import commands

bot = commands.Bot(command_prefix='i!',command=None)
bot.remove_command("help")

@bot.event
async def on_command_error(ctx, error):
 await ctx.send(f'{error}が発生しました')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("test"))
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    inacog.setup(bot)
    inacog2.setup(bot)
    glo.setup(bot)

@tasks.loop(seconds=1)
async def loop():
    channel = bot.get_channel(717604364587630693)
    await channel.send('時間だよ')  

loop.start()
    
bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
