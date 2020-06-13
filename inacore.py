from discord.ext import commands
import traceback

bot = commands.Bot(command_prefix='i!')

@bot.event
async def on_command_error(ctx, error):
 print(error,ctx.message.content)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

bot.run('NzE3NTkwOTc2MTU1MjIyMDI4.XuRqJQ.sesJjpbvS2ojf9fiJ-FJ0kFZbpk') # Botのトークン
