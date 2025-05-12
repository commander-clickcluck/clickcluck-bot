import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up the necessary intents
intents = discord.Intents.default()
intents.message_content = True  # This is required to read message content

# Create the bot with a command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Example command: ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot
bot.run(TOKEN)