#coding: utf-8
import discord
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix='i!',command=None)
bot.remove_command("help")

@bot.event
async def on_command_error(ctx, error):
 await ctx.send(f'{error}が発生しました')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    a = open('datas/config.txt','r')
    for b in a:
     print(b.split())
    a.close()
    
@bot.command()
async def test(ctx,test):
 await ctx.send('hi!')
 a = open('datas/config.txt','w')
 a.write(f'{test}\n')
 a.close()
 a = open('datas/config.txt','r')
 for b in a:
  await ctx.send(b.split())
 a.close()
 
 

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
