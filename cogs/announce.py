import discord
from discord.ext import commands
from discord import app_commands


# Announcement channel ID
ANNOUNCEMENT_CHANNEL_ID = 1523033447587643522

# Footer text
FOOTER = "Zero Gravity Community © 2026"


class Announcement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="announce",
        description="Send an announcement to the announcement channel"
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
        # Get announcement channel
        channel = self.bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)

        # Channel not found
        if channel is None:
            await interaction.response.send_message(
                "❌ Announcement channel not found. Please check the channel ID.",
                ephemeral=True
            )
            return

        # Check whether it is a text channel
        if not isinstance(channel, discord.TextChannel):
            await interaction.response.send_message(
                "❌ The selected channel is not a text channel.",
                ephemeral=True
            )
            return

        # Create announcement embed
        embed = discord.Embed(
            title=f"📢 {title}",
            description=(
                f"{message}\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "🚀 **No Limits • No Boundaries • Just Gravity**"
            ),
            color=discord.Color.from_rgb(88, 101, 242)
        )

        embed.set_footer(text=FOOTER)

        try:
            # Send announcement
            await channel.send(
                content="@everyone",
                embed=embed,
                allowed_mentions=discord.AllowedMentions(
                    everyone=True,
                    users=False,
                    roles=False
                )
            )

            await interaction.response.send_message(
                f"✅ Announcement sent successfully to {channel.mention}.",
                ephemeral=True
            )

        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ The bot does not have permission to send messages in the announcement channel.",
                ephemeral=True
            )

        except discord.HTTPException as error:
            await interaction.response.send_message(
                f"❌ Failed to send the announcement.\n`{error}`",
                ephemeral=True
            )

    @announce.error
    async def announce_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.AppCommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            error_message = (
                "❌ You need Administrator permission to use this command."
            )
        else:
            error_message = f"❌ An error occurred:\n`{error}`"

        if interaction.response.is_done():
            await interaction.followup.send(
                error_message,
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                error_message,
                ephemeral=True
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Announcement(bot))
