import discord
from googlesearch import search
client = discord.Client()
# 起動時のメッセージ
@client.event
async def on_ready():
 open = client.get_channel(チャンネルID)
 await open.send('opened!')
@client.event
async def on_message(message):
 if message.author.bot:
  return
 if message.content == 'i!kensaku':
  tango = message.content
  kensaku = tango.split(' ')[1]
  count = 0
  await message.channel.send('以下のものが見つかったよ。')
  for url in search(kensaku, lang="jp",num = 5):
   await message.channel.send(url)
   count += 1
   if(count == 5):
    break
 if message.content.startwith('こん')
  await message.channel.send('こんにちは！')
client.run('NzE3NTkwOTc2MTU1MjIyMDI4.XtcmVw.k8QN9W-LtTZyhNc1J2A6mi89aMs')
