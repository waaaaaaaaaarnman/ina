from discord.ext import commands
import discord
class inacog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
     await ctx.send(f'Pong! Took:{round(self.bot.latency,2)}ms')
    @commands.command()
    async def search(self,ctx,*,key):
     keyword = key.replace(' ','+')
     await ctx.send(f'検索結果:https://www.google.com/search?q={keyword}')
    @commands.command()
    async def update_notice(self,ctx):
     await self.bot.get_channel(745531061160640572).follow(destination=ctx.channel)
     await ctx.send("アナウンスチャンネルをフォローしたよ！")
    @commands.command()
    async def global_chat(self,ctx):
     if ctx.channel.name == 'ina-global':
      await ctx.channel.create_webhook(name='ina-global-webhook')
      await ctx.send('グローバルチャットに接続できました!')
     else:
      await ctx.send('ina-globalというチャンネル名をつけてもう一度試してね!')
    @commands.command()
    async def help(self,ctx):
       await ctx.send('''**Help**
コマンドのヘルプだぜぇ
ping:Ping値を測定できます。 
search <検索したいワード(スペースOK)>:Googleの検索ができます。
update_notice:アップデート情報のチャンネルをフォローできます。
global_chat:グローバルチャットに接続できます。
公式サバはこちら:https://discord.gg/74ZtTMK
~~embed使いたかったのに謎エラーで使えなかった。起訴~~''')
       
def setup(bot):
    bot.add_cog(inacog(bot))
    print('TestCog Loaded!')

   
