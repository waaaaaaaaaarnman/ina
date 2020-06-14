from discord.ext import commands

class yomiage(commands.Cog):
 @commands.command()
 async def join(ctx):
  voice_state = ctx.author.voice
  if (not voice_state) or (not voice_state.channel):
   await ctx.send("先にボイスチャンネルに入っている必要があります。")
   return
  channel = voice_state.channel
  await channel.connect()
 @commands.command()
 async def leave(ctx):
  voice_client = ctx.message.guild.voice_client
  if not voice_client:
   await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
   return
  await voice_client.disconnect()
  await ctx.send("ボイスチャンネルから切断しました。")
 @commands.command()
 async def play(ctx):
  voice_client = ctx.message.guild.voice_client
  if not voice_client:
   await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
   return
 @commands.Cog.listener()
 async def on_message(message):
  if voice_client:
   hoge = gTTS(message.content)
   hoge.save("s.mp3")
   ffmpeg_audio_source = discord.FFmpegPCMAudio("s.mp3")
   voice_client.play(ffmpeg_audio_source)
 
def setup(bot):
    bot.add_cog(yomiage(bot))
