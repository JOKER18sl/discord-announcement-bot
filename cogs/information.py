import discord
from discord.ext import commands
from discord import app_commands

# ===========================
# CONFIG
# ===========================

INFORMATION_CHANNEL_ID = 1522566152520208419  # <-- Replace with your Information Channel ID

FOOTER = "Zero Gravity Community © 2026"

# ===========================
# SOCIAL BUTTONS
# ===========================

class SocialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(
            discord.ui.Button(
                label="YouTube",
                emoji="🎥",
                url="https://www.youtube.com/@ZeroGravityCommunity"
            )
        )

        self.add_item(
            discord.ui.Button(
                label="TikTok",
                emoji="🎵",
                url="https://www.tiktok.com/@zerogravitycommunity"
            )
        )

        self.add_item(
            discord.ui.Button(
                label="Facebook",
                emoji="📘",
                url="https://www.facebook.com/ZeroGravityCommunity/"
            )
        )

        self.add_item(
            discord.ui.Button(
                label="Discord Invite",
                emoji="💬",
                url="https://discord.gg/D2ck92UEWc"
            )
        )


# ===========================
# COG
# ===========================

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="information",
        description="Post the server information embed."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def information(self, interaction: discord.Interaction):

        channel = self.bot.get_channel(INFORMATION_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Information channel not found!",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="🌌 CONNECT WITH ZERO GRAVITY",
            description=(
                "**One Community. Everywhere.**\n\n"
                "Stay connected with Zero Gravity across all our official platforms.\n\n"
                "✨ **What you'll find:**\n"
                "• Live Streams\n"
                "• Gaming Highlights\n"
                "• Community Updates\n"
                "• Events & Giveaways\n"
                "• Tournaments\n\n"
                "**Click the buttons below to join us!**"
            ),
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/embed/avatars/0.png"
        )

        embed.set_footer(text=FOOTER)

        await channel.send(
            embed=embed,
            view=SocialView()
        )

        await interaction.response.send_message(
            "✅ Information message has been posted.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Information(bot))
