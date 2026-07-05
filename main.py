import os
import asyncio
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def load_extensions():
    await bot.load_extension("cogs.announce")
    await bot.load_extension("cogs.rules")


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} commands")
        for cmd in synced:
            print(f"➡️ /{cmd.name}")
    except Exception as e:
        print(f"❌ Sync error: {e}")


@bot.tree.command(name="ping", description="Check if the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🏓 Pong! {round(bot.latency * 1000)}ms",
        ephemeral=True
    )


async def main():
    if TOKEN is None:
        print("❌ TOKEN environment variable not found!")
        return

    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


asyncio.run(main())
