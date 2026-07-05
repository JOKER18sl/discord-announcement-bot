import os
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping", description="Check if the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🏓 Pong! {round(bot.latency * 1000)}ms"
    )


@bot.tree.command(
    name="announce",
    description="Send an announcement"
)
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(
    title="Announcement Title",
    message="Announcement Message"
)
async def announce(
    interaction: discord.Interaction,
    title: str,
    message: str
):

    embed = discord.Embed(
        title=f"📢 {title}",
        description=message,
        color=discord.Color.gold()
    )

    embed.set_footer(text="Zero Gravity Community © 2026")
    embed.timestamp = discord.utils.utcnow()

    await interaction.response.send_message(
        content="@everyone",
        embed=embed
    )


bot.run(TOKEN)
