#coding: utf-8
from discord.ext import commands
import traceback
from googlesearch import search
from googletrans import Translator
bot = commands.Bot(command_prefix='i!')
@bot.event
async def on_command_error(ctx, error):
    ch = 721361976122540053
    embed = discord.Embed(title="エラー情報", description="", color=0xf00)
    embed.add_field(name="エラー発生サーバー名", value=ctx.guild.name, inline=False)
    embed.add_field(name="エラー発生サーバーID", value=ctx.guild.id, inline=False)
    embed.add_field(name="エラー発生ユーザー名", value=ctx.author.name, inline=False)
    embed.add_field(name="エラー発生ユーザーID", value=ctx.author.id, inline=False)
    embed.add_field(name="エラー発生コマンド", value=ctx.message.content, inline=False)
    embed.add_field(name="発生エラー", value=error, inline=False)
    m = await bot.get_channel(ch).send(embed=embed)
    await ctx.send(f"何らかのエラーが発生しました。ごめんなさい。\nこのエラーについて問い合わせるときはこのコードも一緒にお知らせください：{m.id}")
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
    

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.XuRqJQ.sesJjpbvS2ojf9fiJ-FJ0kFZbpk')
