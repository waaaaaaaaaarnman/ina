from discord.ext import commands
import discord,asyncio
import os
import asyncpg
from yarl import URL
dburl = URL(os.environ["DATABASE_URL"])
host = dburl.host
user = dburl.user
database = dburl.path[1:]
port = dburl.port
password = dburl.password
async def DB(SQL):
    #printするときに使ったやつをついでにURLをそのままでもよし
    conn = await asyncpg.connect(
        host = host ,
        user = user, 
        database = database, 
        port = port, 
        password = password
        )
    #SQLを実行
    values = await conn.fetch(SQL)
    #接続を切る
    await conn.close()
    return values
class globalch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def sql(ctx,*,SQL):
     msg = await DB(SQL)
     await ctx.send(msg)
    @commands.command()
    async def global_chat_on(self,ctx):
      await ctx.channel.create_webhook(name='ina-global-webhook')
      await DB(f'insert into globalch values ({ctx.channel.id})')
      datas = await DB('select * from globalch')
      for channel in datas:
             channeldata = self.bot.get_channel(int(channel))
             ch_webhooks = await channeldata.webhooks()
             webhook = discord.utils.get(ch_webhooks, name='ina-global-webhook')
             await webhook.send(content=f'{ctx.guild.name}がGchatに参加しました',
                                username='Ina Gchat System',
                                avatar_url='https://raw.githubusercontent.com/waaaaaaaaaarnman/ina/master/AA89C19A-BA85-462F-BF8C-4C0336ABBF84.png')
    @commands.command()
    async def global_chat_off(self,ctx):
        datach = self.bot.get_channel(745805249779990648)
        globaldata = await datach.fetch_message(745814673265393794)
        await globaldata.edit(content=globaldata.content.replace(str(ctx.channel.id),''))
        webhooks = await ctx.channel.webhooks()
        webhookk = discord.utils.get(webhooks, name='ina-global-webhook')
        await webhookk.delete()
        await ctx.send('グローバルチャットから切断できました!')
        global_ch = self.bot.get_channel(745805249779990648)
        global_channel = await global_ch.fetch_message(745814673265393794)
        global_channels = global_channel.content.split()
        for channel in global_channels:
             channeldata = self.bot.get_channel(int(channel))
             ch_webhooks = await channeldata.webhooks()
             webhook = discord.utils.get(ch_webhooks, name='ina-global-webhook')
             await webhook.send(content=f'{ctx.guild.name}がGchatから去りました',
                                username='Ina Gchat System',
                                avatar_url='https://raw.githubusercontent.com/waaaaaaaaaarnman/ina/master/AA89C19A-BA85-462F-BF8C-4C0336ABBF84.png')
    @commands.Cog.listener()
    async def on_message(self, message):
     if message.author.bot:
        return
     if message.content.startswith('i!'):
        return
     global_ch = self.bot.get_channel(745805249779990648)
     global_channel = await global_ch.fetch_message(745814673265393794)
     global_channels = global_channel.content.split()
     GLOBAL_WEBHOOK_NAME = "ina-global-webhook"
     for globalch in global_channels:
      if str(message.channel.id) == globalch:
        for channel in global_channels:
            if str(message.channel.id) == channel:
             break
            else:
             channeldata = self.bot.get_channel(int(channel))
             ch_webhooks = await channeldata.webhooks()
             webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)
             await webhook.send(content=message.content,
                                username=message.author.name,
                                avatar_url=message.author.avatar_url_as(format="png"))
             await message.add_reaction('<:good_check:745967536704716900>')
             await asyncio.sleep(3)
             await message.remove_reaction('<:good_check:745967536704716900>',await self.bot.fetch_user(717590976155222028))
def setup(bot):
    bot.add_cog(globalch(bot))
    print('Global Loaded!')
