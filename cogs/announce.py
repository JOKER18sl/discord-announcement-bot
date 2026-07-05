import discord
from discord.ext import commands
from discord import app_commands

SERVER_NAME = "Zero Gravity Community"
FOOTER = "Zero Gravity Community © 2026"

@app_commands.command(
    name="announce",
    description="Create a professional announcement"
)
@app_commands.describe(
    title="Announcement Title",
    description="Announcement Description",
    image="Image URL (Optional)",
    ping="Choose a ping"
)
@app_commands.choices(
    ping=[
        app_commands.Choice(name="@everyone", value="everyone"),
        app_commands.Choice(name="@here", value="here"),
        app_commands.Choice(name="No Ping", value="none")
    ]
)
@app_commands.checks.has_permissions(administrator=True)
async def announce(
    self,
    interaction: discord.Interaction,
    title: str,
    description: str,
    ping: app_commands.Choice[str],
    image: str = None
):
