import os
import asyncio
import discord

from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

TOKEN = os.getenv("DISCORD_TOKEN")


# Bot intents
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True


class ZeroGravityBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        """
        Loads all Cog files when the bot starts
        and synchronizes slash commands.
        """

        extensions = [
            "cogs.rules",
            "cogs.announcement",
            "cogs.information"
        ]

        for extension in extensions:
            try:
                await self.load_extension(extension)
                print(f"✅ Loaded extension: {extension}")

            except commands.ExtensionAlreadyLoaded:
                print(f"⚠️ Extension already loaded: {extension}")

            except commands.ExtensionNotFound:
                print(f"❌ Extension not found: {extension}")

            except commands.NoEntryPointError:
                print(
                    f"❌ setup() function not found in: {extension}"
                )

            except commands.ExtensionFailed as error:
                print(
                    f"❌ Failed to load {extension}: {error}"
                )

        try:
            synced_commands = await self.tree.sync()

            print(
                f"✅ Synced {len(synced_commands)} slash command(s)"
            )

        except Exception as error:
            print(f"❌ Failed to sync commands: {error}")

    async def on_ready(self):
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"✅ Bot online as: {self.user}")
        print(f"🆔 Bot ID: {self.user.id}")
        print(f"🌐 Connected servers: {len(self.guilds)}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="Zero Gravity Community"
        )

        await self.change_presence(
            status=discord.Status.online,
            activity=activity
        )

    async def on_command_error(
        self,
        context: commands.Context,
        error: commands.CommandError
    ):
        if isinstance(error, commands.CommandNotFound):
            return

        print(f"❌ Prefix command error: {error}")


bot = ZeroGravityBot()


async def main():
    if not TOKEN:
        print("❌ DISCORD_TOKEN was not found in the .env file.")
        print("Create a .env file and add:")
        print("DISCORD_TOKEN=YOUR_BOT_TOKEN")
        return

    try:
        async with bot:
            await bot.start(TOKEN)

    except discord.LoginFailure:
        print("❌ Invalid Discord bot token.")

    except KeyboardInterrupt:
        print("🛑 Bot stopped manually.")

    except Exception as error:
        print(f"❌ Bot startup error: {error}")


if __name__ == "__main__":
    asyncio.run(main())
