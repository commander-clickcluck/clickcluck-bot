import discord
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the token from the environment variable
TOKEN = os.getenv('TOKEN')

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("No token found. Please set the token in your .env file.")

# Initialize the client
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(TOKEN)