import discord
from discord.ext import commands
from discord import app_commands

FOOTER = "Zero Gravity Community © 2026"
ANNOUNCEMENT_CHANNEL_ID = 1523033447587643522


CATEGORY_DATA = {
    "important": {
        "title": "🔴 IMPORTANT ANNOUNCEMENT",
        "color": discord.Color.red(),
        "emoji": "🔴"
    },
    "tournament": {
        "title": "🏆 TOURNAMENT ANNOUNCEMENT",
        "color": discord.Color.gold(),
        "emoji": "🏆"
    },
    "event": {
        "title": "🎉 EVENT ANNOUNCEMENT",
        "color": discord.Color.blue(),
        "emoji": "🎉"
    },
    "giveaway": {
        "title": "🎁 GIVEAWAY ANNOUNCEMENT",
        "color": discord.Color.green(),
        "emoji": "🎁"
    },
    "update": {
        "title": "🛠️ SERVER UPDATE",
        "color": discord.Color.orange(),
        "emoji": "🛠️"
    }
}


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
        category="Choose announcement category",
        ping="Choose ping type",
        image="Upload banner/background image (Optional)"
    )
    @app_commands.choices(
        category=[
            app_commands.Choice(name="🔴 Important", value="important"),
            app_commands.Choice(name="🏆 Tournament", value="tournament"),
            app_commands.Choice(name="🎉 Event", value="event"),
            app_commands.Choice(name="🎁 Giveaway", value="giveaway"),
            app_commands.Choice(name="🛠️ Update", value="update"),
        ],
        ping=[
            app_commands.Choice(name="@everyone", value="everyone"),
            app_commands.Choice(name="@here", value="here"),
            app_commands.Choice(name="No Ping", value="none"),
        ]
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def announce(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        category: app_commands.Choice[str],
        ping: app_commands.Choice[str],
        image: discord.Attachment = None
    ):
                channel = self.bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Announcement channel not found!",
                ephemeral=True
            )
            return

        data = CATEGORY_DATA[category.value]

        ping_text = {
            "everyone": "@everyone",
            "here": "@here",
            "none": ""
        }[ping.value]

        embed = discord.Embed(
            title=data["title"],
            description=(
                f"# {data['emoji']} {title}\n\n"
                f"{description}\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                "🚀 **No Limits • No Boundaries • Just Gravity**"
            ),
            color=data["color"]
        )

        if image:
            embed.set_image(url=image.url)

        if interaction.guild and interaction.guild.icon:
            embed.set_author(
                name="Zero Gravity Community",
                icon_url=interaction.guild.icon.url
            )
            embed.set_thumbnail(url=interaction.guild.icon.url)
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
        if isinstance(error, app_commands.MissingPermissions):
            message = "❌ You need Administrator permission to use this command."
        else:
            message = f"❌ Error: {error}"

        if interaction.response.is_done():
            await interaction.followup.send(message, ephemeral=True)
        else:
            await interaction.response.send_message(message, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Announce(bot))

    
