import discord
import discord_interactions
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

token_file = open("token.txt")
TOKEN = token_file.read()
token_file.close()

@bot.command(name="test", description="this is a test command.")
async def test_command(ctx):
    await ctx.channel.send("test")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)