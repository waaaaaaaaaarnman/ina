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
        bumpdata = await self.bot.get_channel(745805249779990648).
                                              
def setup(bot):
    bot.add_cog(bump(bot))
    print('Bump Loaded!')
