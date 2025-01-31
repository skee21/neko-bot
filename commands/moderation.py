import discord
from discord import app_commands
from typing import Optional
import datetime

async def setup(bot):
    @bot.command(name="kick", description="Kicks a member")
    async def kick(interaction: discord.Interaction, user: discord.Member, reason: Optional[str] = "No reason provided"):
        if interaction.guild.me.guild_permissions.kick_members:
            if interaction.user.guild_permissions.kick_members:
                await interaction.response.send_message(f"{user.mention} has been kicked successfully")
                await user.kick(reason=reason)
            else:
                await interaction.response.send_message(":middle_finger: :middle_finger:", ephemeral=True)
        else:
            await interaction.response.send_message("Gimme the necessary permission first dummies.")

    @bot.command(name="mute", description="Mutes a member")
    async def mute(interaction: discord.Interaction, user: discord.Member, duration: int = 1440, reason: Optional[str] = "No reason"):
        if interaction.guild.me.guild_permissions.moderate_members:
            if interaction.user.guild_permissions.moderate_members:
                time = datetime.timedelta(minutes=duration)
                await user.timeout(time, reason=reason)
                await interaction.response.send_message(f"User muted for {time} successfully.")
            else:
                await interaction.response.send_message(":middle_finger: :middle_finger:", ephemeral=True)
        else:
            await interaction.response.send_message("Gimme the necessary permissions dummy!")

    @bot.command(name="unmute", description="Unmutes a member")
    async def unmute(interaction: discord.Interaction, user: discord.Member):
        if interaction.guild.me.guild_permissions.moderate_members:
            if interaction.user.guild_permissions.moderate_members:
                await user.edit(timed_out_until=None)
                await interaction.response.send_message(f"{user.mention} has been unmuted successfully!")
            else:
                await interaction.response.send_message(":middle_finger:", ephemeral=True)
        else:
            await interaction.response.send_message("Gimme the necessary permissions dummy!")

    @bot.command(name='ban', description='Bans a member')
    async def ban(interaction: discord.Interaction, user: discord.Member, reason: Optional[str] = "No reason"):
        if interaction.guild.me.guild_permissions.ban_members:
            if interaction.user.guild_permissions.ban_members:
                await interaction.response.send_message(f"{user.name} has been banned for {reason}")
                await interaction.guild.ban(user, reason=reason, delete_message_days=1)
            else:
                await interaction.response.send_message(":middle_finger:", ephemeral=True)
        else:
            await interaction.response.send_message("Give me the necessary permissions first dummy.")

    @bot.command(name="unban", description="Unbans a member")
    async def unban(interaction: discord.Interaction, user: str, reason: Optional[str] = "No reason"):
        user = await interaction.client.fetch_user(user)
        if interaction.guild.me.guild_permissions.ban_members:
            if interaction.user.guild_permissions.ban_members:
                await interaction.guild.unban(user, reason=reason)
                await interaction.response.send_message(f"{user.name} has been unbanned.")
            else:
                await interaction.response.send_message(":middle_finger:", ephemeral=True)
        else:
            await interaction.response.send_message("Give me the necessary permissions first dummy.")