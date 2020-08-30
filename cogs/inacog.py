from discord.ext import commands
import discord,random,libneko
def default_buttons():
    from libneko.pag.reactionbuttons import (
        first_page,
        back_10_pages,
        previous_page,
        next_page,
        forward_10_pages,
        last_page
    )

    return (
        first_page(),
        back_10_pages(),
        previous_page(),
        next_page(),
        forward_10_pages(),
        last_page()
    )
buttons = default_buttons()
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
    async def about(self,ctx):
        about = discord.Embed(title='about',description='このボットについてです。',color=discord.Colour.from_rgb(222,198,16))
        about.add_field(name="作った人",value="Kaede_728#8140")
        about.add_field(name="ping",value=round(self.bot.latency,2))
        about.add_field(name="人数",value=len(self.bot.users))
        about.add_field(name="サーバー数",value=len(self.bot.guilds))
        await ctx.send(embed=about)
    @commands.command()
    async def help(self, ctx):
            pages = [(discord.Embed(title="ヘルプコマンド")),
                     (discord.Embed(title="お遊びコマンド")),
                     (discord.Embed(title="グローバルチャットのコマンド")),
                     (discord.Embed(title="その他コマンド"))]
            pages[0].add_field(name="i!about", value="このBotについてのInfoを表示します。")
            pages[0].add_field(name='i!help', value='このヘルプを表示します。')
            pages[0].add_field(name="公式サバ",value="[公式サバはこちら](https://discord.gg/tZqkn8H)")
            pages[0].add_field(name="公式サイト",value="[公式サイトはこちら](https://waaaaaaaaaarnman.github.io/ina/top/)")
            pages[1].add_field(name="i!omjkuji", value="おみくじができます。~~ですがかなり地味です。~~")
            pages[2].add_field(name="i!global＿chat＿<on or off>", value="グローバルチャットをオンオフできます。")
            pages[3].add_field(name="i!search <調べたい単語>", value="グローバルチャットに登録します。")
            pages[3].add_field(name="i!ping", value="Ping測定ができます。")
            pages[3].add_field(name="i!bugandidea", value="レポートができます。")
            nav = libneko.pag.navigator.EmbedNavigator(ctx, pages, buttons=default_buttons(), timeout=30)
            nav.start()
            await ctx.send(nav)
    
    @commands.command()
    async def bugandidea(self,ctx,bugandidea):
     await self.bot.get_channel(745601986669576192).send(f'{ctx.author}さん:{bugandidea}')
     await ctx.send('バグ報告又はアイデアの送信が完了しました!')
    @commands.command()
    async def omikuji(self,ctx):
     omikujis = ['大凶','凶','吉','小吉','中吉','大吉']
     await ctx.send(random.choice(omikujis))
def setup(bot):
    bot.add_cog(inacog(bot))
    print('TestCog Loaded!')

   
