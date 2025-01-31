import discord
from discord import app_commands
import os
import importlib

# Create a bot instance with intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
client = discord.Client(intents=intents)
bot = app_commands.CommandTree(client)

# Event: When the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")
    await client.change_presence(activity=discord.Game(name="hello"))
    try:
        # Load commands from the commands folder
        for filename in os.listdir("./commands"):
            if filename.endswith(".py") and filename != "__init__.py":  # Skip __init__.py
                module_name = f"commands.{filename[:-3]}"
                module = importlib.import_module(module_name)
                if hasattr(module, "setup"):
                    await module.setup(bot)
                    print(f"Loaded commands from {module_name}")
        
        # Sync commands with Discord
        synced = await bot.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Run the bot
client.run("")