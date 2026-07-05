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
                "Be kind to all members. No harassment, hate speech, or personal attacks.\n\n"

                "2️⃣ **No Toxicity**\n"
                "Keep the community friendly. Toxic behavior is not allowed.\n\n"

                "3️⃣ **No Spam**\n"
                "Do not spam messages, emojis, mentions, links, or images.\n\n"

                "4️⃣ **No NSFW Content**\n"
                "Adult, violent, or inappropriate content is not allowed.\n\n"

                "5️⃣ **No Advertising**\n"
                "Do not promote servers, links, pages, or channels without staff permission.\n\n"

                "6️⃣ **Use Correct Channels**\n"
                "Post content in the correct channel to keep the server clean.\n\n"

                "7️⃣ **No Cheats or Hacks**\n"
                "Cheats, hacks, cracked tools, or illegal game content are not allowed.\n\n"

                "8️⃣ **Follow Staff Instructions**\n"
                "Admins and moderators have the final decision in server matters.\n\n"

                "9️⃣ **Protect Privacy**\n"
                "Do not share anyone’s personal information without permission.\n\n"

                "🔟 **Enjoy the Community**\n"
                "Have fun, make friends, and keep Zero Gravity positive.\n\n"

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

        await channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Rules posted successfully!",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Rules(bot))
