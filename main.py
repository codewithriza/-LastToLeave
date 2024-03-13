import discord
from discord.ext import commands

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

    await ctx.send(f"Joining voice channel: {channel.name}")
    vc = await channel.connect()

    def check(member, before, after):
        return len(channel.members) == 1

    await bot.wait_for('voice_state_update', check=check)
    winner = channel.members[0]

    # Create an Embed object
    embed = discord.Embed(
        title="Last to Leave Event Winner",
        description=f"{winner.mention} is the winner of the last to leave event!",
        color=0x00ff00  # Green color
    )

    await ctx.send(embed=embed)

    await vc.disconnect()

bot.run('TOKEN')
