import discord
from discord.ext import commands

import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
import pytube
from pytube import YouTube
from pytube import Playlist
import discord as d

print("musicの読み込み完了")

color=000000

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()
        if "list" in search:
            return await ctx.send("プレイリストには、対応していません。個別で曲を追加することができます。")
        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        embed = d.Embed(title="キュー追加", description=f"**[{data['title']}]({data['webpage_url']})**をキューに追加しました。", color=color)
        embed.set_thumbnail(url=data['thumbnail'])
        await ctx.send(embed=embed, delete_after=15)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


class MusicPlayer:
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    embed = d.Embed(title="エラー", description="音楽を再生中エラーが発生しました。", color=color)
                    await self._channel.send(embed=embed)
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            embed = d.Embed(title="再生開始", description=f'**{source.title}** \n**追加した人**: {source.requester}', color=color)
            self.np = await self._channel.send(embed=embed)
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

    def destroy(self, guild):
        """Disconnect and cleanup the player."""
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class Music(commands.Cog):
    """Music related commands."""

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        """A local error handler for all errors arising from commands in this cog."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('このコマンドは、DMで使用できません。')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            embed = d.Embed(title="エラー", description='ボイスチャンネルに接続できませんでした。\nあなたがボイスチャンネルに入っているか確認してください。\nまたは、ボイスチャンネルの権限をご確認ください。', color=color)
            return await ctx.send(embed=embed)

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        """Retrieve the guild player, or generate one."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='connect', aliases=['join'])
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        """Connect to voice.
        Parameters
        ------------
        channel: discord.VoiceChannel [Optional]
            The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
            will be made.
        This command also handles moving the bot to different channels.
        """
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                embed = d.Embed(title="エラー", description='参加できるボイスチャンネルがありません。有効なボイスチャンネルを指定するか、ボイスチャンネルに参加してください。', color=color)
                return await ctx.send(embed=embed)

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                embed = d.Embed(title="エラー", description=f'{channel}への接続は、タイムアウトしました。', color=color)
                raise await ctx.send(embed=embed)
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                embed = d.Embed(title="エラー", description=f'{channel}への接続は、タイムアウトしました。', color=color)
                raise await ctx.send(embed=embed)

        embed = d.Embed(title="接続完了", description=f'{channel}へ接続しました。', color=color)
        return await ctx.send(embed=embed)

    @commands.command(name='play', aliases=['sing'])
    async def play_(self, ctx, *, search: str=None):
        """Request a song and add it to the queue.
        This command attempts to join a valid voice channel if the bot is not already in one.
        Uses YTDL to automatically search and retrieve a song.
        Parameters
        ------------
        search: str [Required]
            The song to search and retrieve using YTDL. This could be a simple search, an ID or URL.
        """
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)
            player = self.get_player(ctx)
            try:
                async with timeout(2):
                    source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=True)
            except:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)
            await player.queue.put(source)
        else:
            if vc.is_paused() and search==None:
                ctx.voice_client.resume()
                await ctx.send("再生を再開しました。")
            else:
                player = self.get_player(ctx)
                try:
                    async with timeout(2):
                        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=True)
                except:
                    source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)
                await player.queue.put(source)

    @commands.command(name='pause')
    async def pause_(self, ctx):
        """Pause the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)
        elif vc.is_paused():
            return

        vc.pause()
        embed = d.Embed(title="一時停止", description='曲を一時停止しました。再度流すには、`;resume`を実行してください。', color=color)
        await ctx.send(embed=embed)

    @commands.command(name='resume')
    async def resume_(self, ctx):
        """Resume the currently paused song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)
        elif not vc.is_paused():
            return

        vc.resume()
        embed = d.Embed(title="再生再開", description='音楽の再生を再開しました。', color=color)

    @commands.command(name='skip')
    async def skip_(self, ctx):
        """Skip the song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)
        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return
        vc.stop()
        embed = d.Embed(title="スキップ", description='曲をスキップしました。', color=color)
        await ctx.send(embed=embed)

    @commands.command(name='queue', aliases=['q', 'playlist'])
    async def queue_info(self, ctx):
        """Retrieve a basic queue of upcoming songs."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if player.queue.empty():
            embed = d.Embed(title="エラー", description='キューに音楽は存在しません。', color=color)
            return await ctx.send(embed=embed)

        # Grab up to 5 entries from the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, 10))

        fmt = '\n'.join(f'{_["title"]}' for _ in upcoming)
        embed = discord.Embed(title=f'キューに存在する曲 - 全部で:{len(upcoming)}曲', description=fmt,color=color)
        await ctx.send(embed=embed)

    @commands.command(name='now_playing', aliases=['np', 'current', 'currentsong', 'playing'])
    async def now_playing_(self, ctx):
        """Display information about the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if not player.current:
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)
        embed = d.Embed(title="再生中の曲", description=f'現在再生中:**{vc.source.title}**\nリクエストしたユーザー:{vc.source.requester}', color=color)
        player.np=await ctx.send(embed=embed)

    @commands.command(name='volume', aliases=['vol'])
    async def change_volume(self, ctx, *, vol: float):
        """Change the player volume.
        Parameters
        ------------
        volume: float or int [Required]
            The volume to set the player to in percentage. This must be between 1 and 100.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)

        if not 0 < vol < 101:
            embed = d.Embed(title="エラー", description='音量は、`1`から`100`の間で設定してください。', color=color)
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 100

        player.volume = vol / 100
        embed = d.Embed(title="音量変更", description=f'ボリュームを{vol}%にしました。', color=color)
        await ctx.send(embed=embed)

    @commands.command(name='stop')
    async def stop_(self, ctx):
        """Stop the currently playing song and destroy the player.
        !Warning!
            This will destroy the player assigned to your guild, also deleting any queued songs and settings.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = d.Embed(title="エラー", description='現在VCに接続していません!', color=color)
            return await ctx.send(embed=embed)

        await self.cleanup(ctx.guild)
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
            if not member.guild.voice_client.is_paused() and [i for i in member.guild.me.voice.channel.members if not i.bot] == []:
                await member.guild.voice_client.disconnect()
        except:
            pass

def setup(bot):
    bot.add_cog(Music(bot))
