#coding: utf-8
import discord.py
from discord.ext import commands
import traceback
from googlesearch import search
from googletrans import Translator
bot = commands.Bot(command_prefix='i!')
client = discord.client()
@bot.event
async def on_command_error(self,ctx, error):
 ctx.send('エラー',error)
@bot.event
async def on_ready():
 await bot.get_channel(717604364587630693).send('opened!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
async def search(ctx):
    count = 0
    for url in search(ctx.message.content, lang="jp",num = 5):
     ctx.send(url)
     count += 1
     if(count == 5):
      break
async def honyaku(ctx):
 translator = Translator()
 aaa = translator.translate(ctx.message.content, src='en', dest='ja')
 await ctx.send(aaa.text)
@client.event
async def on_message(message):
 if message.content == 'aaa':
  await message.channel.send('aa')
             
    

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.XuRqJQ.sesJjpbvS2ojf9fiJ-FJ0kFZbpk')
client.run('NzE3NTkwOTc2MTU1MjIyMDI4.XuRqJQ.sesJjpbvS2ojf9fiJ-FJ0kFZbpk')
