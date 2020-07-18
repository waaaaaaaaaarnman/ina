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
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    GLOBAL_CH_NAME = "伊奈グローバル" 
    GLOBAL_WEBHOOK_NAME = "ina-global-webhook"
    if message.channel.name == GLOBAL_CH_NAME:
        await message.delete()
        channels = bot.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        for channel in global_channels:
            ch_webhooks = await channel.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)
            if webhook is None:
                await channel.create_webhook(name=GLOBAL_WEBHOOK_NAME)
            await webhook.send(content=message.content,
                username=message.author.name,
                avatar_url=message.author.avatar_url_as(format="png"))
@bot.command()
async def ping(ctx):
 await ctx.send(f'pong!{bot.latency}')
bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.Xu2_bw.MD4oJ_ZuFNYljkLsJiZi3zxMTy4')
