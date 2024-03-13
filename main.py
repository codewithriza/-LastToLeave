import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def lasttoleave(ctx):
    if not ctx.author.voice or not ctx.author.voice.channel:
        await ctx.send("You are not in a voice channel.")
        return

    channel = ctx.author.voice.channel

    embed = discord.Embed(
        title="Last to Leave Event",
        description=f"Joining voice channel: {channel.name}",
        color=0x00ff00
    )
    await ctx.send(embed=embed)

    vc = await channel.connect()

    # Get a list of only human users in the channel
    human_members = [member for member in channel.members if not member.bot]

    # Continuously check for the last human member in the channel
    while len(human_members) > 1:
        await asyncio.sleep(1)  # Wait for 1 second before checking again
        human_members = [member for member in channel.members if not member.bot]

    winner = human_members[0]

    embed = discord.Embed(
        title="Last to Leave Event",
        description=f"{winner.mention} is the winner of the last to leave event!",
        color=0xff0000
    )
    await ctx.send(embed=embed)

    await vc.disconnect()


bot.run('TOKEN')
