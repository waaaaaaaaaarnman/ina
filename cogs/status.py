from discord.ext import commands,tasks
class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.statusloop.start()
    @tasks.loop(seconds=40)
    async def statusloop(self):
        print('loop ok')
def setup(bot):
    bot.add_cog(status(bot))
