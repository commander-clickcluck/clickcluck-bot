import discord
import os
import re
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
STORE_ID = os.getenv("AMAZON_STORE_ID")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

AMAZON_REGEX = r"(https?://(?:www\.)?amazon\.[a-z\.]{2,6}/(?:[^ ]+))"

def convert_to_affiliate_link(url):
    if "tag=" in url:
        return url  # already has tag
    separator = "&" if "?" in url else "?"
    return f"{url}{separator}tag={STORE_ID}"

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    matches = re.findall(AMAZON_REGEX, message.content)
    if matches:
        for url in matches:
            affiliate_link = convert_to_affiliate_link(url)
            await message.channel.send(f"Affiliate link: {affiliate_link}")

client.run(TOKEN)