import discord
from discord.ext import commands
from discord import app_commands

FOOTER = "Zero Gravity Community © 2026"
ANNOUNCEMENT_CHANNEL_ID = 1523033447587643522


class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="announce",
        description="Create a professional announcement"
    )
    @app_commands.describe(
        title="Announcement title",
        description="Announcement description",
        image="Image URL (Optional)"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def announce(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        image: str = None
    ):

        channel = self.bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Announcement channel not found!",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title=f"📢 {title}",
            description=f"✨ {description}",
            color=discord.Color.gold()
        )

        if image:
            embed.set_image(url=image)

        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)

        embed.set_author(
            name="Zero Gravity Community",
            icon_url=interaction.guild.icon.url if interaction.guild.icon else None
        )

        embed.set_footer(text=FOOTER)
        embed.timestamp = discord.utils.utcnow()

        await channel.send(
            content="@everyone",
            embed=embed
        )

        await interaction.response.send_message(
            "✅ Announcement sent successfully!",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Announce(bot))
