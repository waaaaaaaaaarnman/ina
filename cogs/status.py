from discord.ext import commands,tasks
import asyncio,discord,datetime
class status(commands.Cog):
	    @tasks.loop(seconds=40)
	    async def statusloop(self):
	      await self.bot.change_presence(activity=discord.Game(f"導入サーバー数:{len(self.bot.guilds)}"))
	      await asyncio.sleep(10)
	      await self.bot.change_presence(activity=discord.Game(f"メンバー数:{len(self.bot.users)}"))
	      await asyncio.sleep(10)
	      await self.bot.change_presence(activity=discord.Game("ヘルプはi!help"))
	      await asyncio.sleep(10)
	      dt = datetime.now()
	      await self.bot.change_presence(activity=discord.Game(f'ただいま{dt.hour}:{dt.minute}です！'))
	      await asyncio.sleep(10)
	    def __init__(self, bot):
	        self.bot = bot
	        self.statusloop.start()
def setup(bot):
	    bot.add_cog(status(bot))
	    print('Status Loaded!')
