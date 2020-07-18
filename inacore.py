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
@bot.event
async def on_message(message):
    globallist = open('datas/global.txt','r')
    for list in globallist:
     global_list = list()
     globallist.append(list.split())
     globallist.close()
    GLOBAL_WEBHOOK_NAME = "ina_global_webhook"
    if message.channel.name == global_list:
        await message.delete()
        for channel in global_list:
            ch_webhooks = await channel.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)
            if webhook == None:
             await channel.create_webhook(name=GLOBAL_WEBHOOK_NAME)
            await webhook.send(content=message.content,
                username=message.author.name,
                avatar_url=message.author.avatar_url_as(format="png"))
    
@bot.command()
async def test(ctx,test):
 await ctx.send('hi!')
 a = open('datas/config.txt','a')
 a.write(f'\n{test}')
 a.close()
 a = open('datas/config.txt','r')
 for b in a:
  await ctx.send(b.split())
 a.close()
 @bot.command
 async def global_on(ctx):
  ac = open('datas/global.txt','w')
  ac.write(ctx.channel.id)
  ac.close(
  await ctx.send(f'追加ができました！id:{ctx.channel.id}')
 
 

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
