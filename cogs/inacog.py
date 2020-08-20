from discord.ext import commands
import discord,random
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
    async def global_chat_on(self,ctx):
      await ctx.channel.create_webhook(name='ina-global-webhook')
      datach = self.bot.get_channel(745805249779990648)
      globaldata = await datach.fetch_message(745814673265393794)
      await globaldata.edit(content=f'{globaldata.content} {ctx.channel.id}')
      await ctx.send('グローバルチャットに接続できました!')
    @commands.command()
    async def global_chat_off(self,ctx):
      datach = self.bot.get_channel(745805249779990648)
      globaldata = await datach.fetch_message(745814673265393794)
      await globaldata.edit(content=globaldata.content.replace(ctx.channel.id,'')
      await ctx.send('グローバルチャットから離脱しました!')
    @commands.command()
    async def about(self,ctx):
        about = discord.Embed(title='about',description='このボットについてです。')
        about.add_field(name="作った人",value="Kaede_728#8140")
        about.add_field(name="ping",value=round(self.bot.latency,2))
        about.add_field(name="人数",value=len(self.bot.users))
        about.add_field(name="サーバー数",value=len(self.bot.guilds))
        await ctx.send(embed=about)
    @commands.command()
    async def help(self,ctx):
        helpembed = discord.Embed(title="Help",description="コマンドのヘルプだぜぇ") 
        helpembed.add_field(name="ping",value="Ping値を測定できます。")
        helpembed.add_field(name="search <検索したいワード(スペースOK)>",value="Googleの検索ができます。")
        helpembed.add_field(name="update_notice",value="アップデート情報のチャンネルをフォローできます。")
        helpembed.add_field(name="global_chat",value="グローバルチャットに接続できます。")
        helpembed.add_field(name="bugandidea <文章>",value="バグ報告とアイデア送信ができます。")
        helpembed.add_field(name="omikuji",value="おみぐじができます。")
        helpembed.add_field(name="about",value="ボットの情報が表示されます。")
        helpembed.add_field(name="公式サバ",value="[公式サバはこちら](https://discord.gg/74ZtTMK)")
        helpembed.add_field(name="公式サイト",value="[公式サイトはこちら](https://waaaaaaaaaarnman.github.io/ina/top/)")
        await ctx.send(embed=helpembed)
    @commands.command()
    async def bugandidea(self,ctx,bugandidea):
     await self.bot.get_channel(745601986669576192).send(bugandidea)
     await ctx.send('バグ報告又はアイデアの送信が完了しました!')
    @commands.command()
    async def omikuji(self,ctx):
     omikujis = ['大凶','凶','吉','小吉','中吉','大吉']
     await ctx.send(random.choice(omikujis))
def setup(bot):
    bot.add_cog(inacog(bot))
    print('TestCog Loaded!')

   
