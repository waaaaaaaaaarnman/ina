from discord.ext import commands,tasks
import time
class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        statusloop.start()
    @tasks.loop(seconds=40)
    async def statusloop(self):
      await self.bot.change_presence(activity=discord.Game(f"導入サーバー数:{len(self.bot.guilds)}"))
      time.sleep(10)
      await self.bot.change_presence(activity=discord.Game("てすと1"))
      time.sleep(10)
      await self.bot.change_presence(activity=discord.Game("てすと2"))
      time.sleep(10)
      await self.bot.change_presence(activity=discord.Game("てすと3"))
      time.sleep(10)          
  
def setup(bot):
    bot.add_cog(status(bot))
    print('Status Loaded!')
