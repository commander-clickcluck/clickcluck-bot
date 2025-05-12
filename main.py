import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
AFFILIATE_TAG = os.getenv("AMAZON_ASSOCIATE_TAG")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def affiliate(ctx, *, url: str):
    if "amazon." not in url:
        await ctx.send("Please provide a valid Amazon link.")
        return

    if "tag=" in url:
        await ctx.send("Affiliate link already exists.")
    else:
        sep = "&" if "?" in url else "?"
        affiliate_link = f"{url}{sep}tag={AFFILIATE_TAG}"
        await ctx.send(f"Affiliate link: {affiliate_link}")

bot.run(TOKEN)