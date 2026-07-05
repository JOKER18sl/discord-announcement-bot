import discord
from discord.ext import commands
from discord import app_commands

SERVER_NAME = "Zero Gravity Community"
FOOTER = "Zero Gravity Community © 2026"

class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="announce",
        description="Send a server announcement"
    )
    @app_commands.describe(
        title="Announcement title",
        message="Announcement message"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def announce(
        self,
        interaction: discord.Interaction,
        title: str,
        message: str
    ):

        embed = discord.Embed(
            title=f"📢 {title}",
            description=message,
            color=discord.Color.gold()
        )

        embed.set_footer(text=FOOTER)
        embed.timestamp = discord.utils.utcnow()

        await interaction.response.send_message(
            content="@everyone",
            embed=embed
        )

async def setup(bot):
    await bot.add_cog(Announce(bot))
