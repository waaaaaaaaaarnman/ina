from discord.ext import commands
import discord
class inacog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
     await ctx.send(f'pong! took:{round(self.bot.latency,2)}ms')
    @commands.command()
    async def search(self,ctx,*,key):
     keyword = key.replace(' ','+')
     await ctx.send(f'https://www.google.com/search?q={keyword}')
    @commands.command()
    async def update_notice(self,ctx):
     await self.bot.get_channel(745531061160640572).follow(destination=ctx.channel)
     await ctx.send("アナウンスチャンネルをフォローしたよ！")
    @commands.command()
    async def global_chat(self,ctx):
     if ctx.channel.name == 'ina-global':
        
    @command.command()
    async def help(self,ctx):
       helpembed = discord.Embed(title="Help",description="コマンドのヘルプだぜぇ") 
       helpembed.add_field(name="ping",value="Ping値を測定できます。")
       helpembed.add_field(name="search <検索したいワード(スペースOK)>",value="Googleの検索ができます。")
       helpembed.add_field(name="update_notice",value="アップデート情報のチャンネルをフォローできます。")
       helpembed.add_field(name="global_chat",value="グローバルチャットに接続できます。")
def setup(bot):
    bot.add_cog(inacog(bot))
    print('testcog load ok')

   
