import discord
from discord.ext import commands
from discord import app_commands

RULES_CHANNEL_ID = 1522693661211623576
FOOTER = "Zero Gravity Community © 2026"


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="rules",
        description="Post the server rules in the rules channel"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def rules(self, interaction: discord.Interaction):

        channel = self.bot.get_channel(RULES_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Rules channel not found!",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="📜 ZERO GRAVITY COMMUNITY RULES",
            description=(
                "# ⚖️ Server Rules\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n\n"

                "1️⃣ **Respect Everyone**\n"
                "Treat everyone with respect. Harassment, hate speech, or personal attacks are not allowed.\n\n"

                "2️⃣ **No Toxicity**\n"
                "Keep the community friendly and positive.\n\n"

                "3️⃣ **No Spam**\n"
                "Avoid spam, excessive mentions, or repeated messages.\n\n"

                "4️⃣ **No NSFW Content**\n"
                "Adult or inappropriate content is strictly prohibited.\n\n"

                "5️⃣ **No Advertising**\n"
                "Do not advertise other servers, channels, or websites without permission.\n\n"

                "6️⃣ **Use The Correct Channels**\n"
                "Keep discussions in their appropriate channels.\n\n"

                "7️⃣ **No Cheats Or Hacks**\n"
                "Sharing cheats, hacks, or illegal software is forbidden.\n\n"

                "8️⃣ **Respect Staff Decisions**\n"
                "Moderators and admins have the final decision.\n\n"

                "9️⃣ **Protect Privacy**\n"
                "Never share anyone's personal information.\n\n"

                "🔟 **Have Fun**\n"
                "Enjoy the community and help make it a great place.\n\n"

                "━━━━━━━━━━━━━━━━━━━━━━\n"
                "🚀 **No Limits • No Boundaries • Just Gravity**"
            ),
            color=discord.Color.gold()
        )

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
            content="@everyone",
            embed=embed,
            allowed_mentions=discord.AllowedMentions(everyone=True)
        )

        await interaction.response.send_message(
            "✅ Rules have been posted successfully!",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Rules(bot))
