from discord.ext import commands
import discord,asyncio
class bump(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group()
    async def bump_tuti(ctx,self):
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')
    @bump_tuti.command()
    async def on(self,ctx):
        bumpdata = await self.bot.get_channel(745805249779990648).fetch_message(745906962197381140)
        await bumpdata.edit(content=f'{bumpdata.content} {ctx.channel.id}')
        await ctx.send('bump通知をONにしました!')
    @bump_tuti.command()
    async def off(self,ctx):
        bumpdata = await self.bot.get_channel(745805249779990648).fetch_message(745906962197381140)
        await bumpdata.edit(content=bumpdata.content.replace(ctx.channel.id,'')
        await ctx.send('bump通知をOFFにしました!')
    @commands.Cog.listener()
    async def on_message(self,message):
       if message.author.bot:
            return
       if message.content == '!d bump':
         bumpdata = await self.bot.get_channel(745805249779990648).fetch_message(745906962197381140)
         bumplist = bumpdata.split()
         for bump in bumplist:
           if bump == str(message.channel.id):                       
            await message.channel.send('bumpを検知したので二時間ごに通知します。')
            asyncio.sleep(7200)
            await message.channel.send('bumpしましょう!')
def setup(bot):
    bot.add_cog(bump(bot))
    print('Bump Loaded!')
