from discord.ext import commands
import traceback
bot = commands.Bot(command_prefix='i!')
@bot.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='testing'))
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
@bot.command()
async def hello(ctx):
    await ctx.send('hello!')
bot.run('OU02s4VtcIYcI8wHBeIzkwn4R30aXNLX')
