import discord
from discord import app_commands

async def setup(bot):
    @bot.command(name="hello", description="Say hello to the bot!")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message("Hello! How can I help you?")