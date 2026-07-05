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
        ping="Choose ping type",
        color="Choose embed color",
        image="Upload background/banner image (Optional)"
    )
    @app_commands.choices(
        ping=[
            app_commands.Choice(name="@everyone", value="everyone"),
            app_commands.Choice(name="@here", value="here"),
            app_commands.Choice(name="No Ping", value="none"),
        ],
        color=[
            app_commands.Choice(name="Gold", value="gold"),
            app_commands.Choice(name="Red", value="red"),
            app_commands.Choice(name="Blue", value="blue"),
            app_commands.Choice(name="Green", value="green"),
        ]
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def announce(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        ping: app_commands.Choice[str],
        color: app_commands.Choice[str],
        image: discord.Attachment = None
    ):
        channel = self.bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Announcement channel not found!",
                ephemeral=True
            )
            return

        ping_text = {
            "everyone": "@everyone",
            "here": "@here",
            "none": ""
        }[ping.value]

        color_map = {
            "gold": discord.Color.gold(),
            "red": discord.Color.red(),
            "blue": discord.Color.blue(),
            "green": discord.Color.green(),
        }

        embed = discord.Embed(
            title=f"📢✨ {title}",
            description=(
                f"✨ {description}\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                "🚀 **No Limits • No Boundaries • Just Gravity**"
            ),
            color=color_map[color.value]
        )

        if image:
            embed.set_image(url=image.url)

        if interaction.guild and interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)
            embed.set_author(
                name="Zero Gravity Community",
                icon_url=interaction.guild.icon.url
            )
        else:
            embed.set_author(name="Zero Gravity Community")

        embed.set_footer(text=FOOTER)
        embed.timestamp = discord.utils.utcnow()

        await channel.send(
            content=ping_text,
            embed=embed
        )

        await interaction.response.send_message(
            "✅ Announcement sent successfully!",
            ephemeral=True
        )

    @announce.error
    async def announce_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.AppCommandError
    ):
        await interaction.response.send_message(
            f"❌ Error: {error}",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Announce(bot))
