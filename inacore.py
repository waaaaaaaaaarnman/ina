from discord.ext import commands
import traceback
bot = commands.Bot(command_prefix='i!')
@bot.event
async def on_command_error(ctx, error):
    ch = 721361976122540053
    embed = discord.Embed(title="エラー情報", description="", color=0xf00)
    embed.add_field(name="エラー発生サーバー名", value=ctx.guild.name, inline=False)
    embed.add_field(name="エラー発生サーバーID", value=ctx.guild.id, inline=False)
    embed.add_field(name="エラー発生ユーザー名", value=ctx.author.name, inline=False)
    embed.add_field(name="エラー発生ユーザーID", value=ctx.author.id, inline=False)
    embed.add_field(name="エラー発生コマンド", value=ctx.message.content, inline=False)
    embed.add_field(name="発生エラー", value=error, inline=False)
    m = await bot.get_channel(ch).send(embed=embed)
    await ctx.send("{m.id}")

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
