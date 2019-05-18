import os
import sys, traceback
import discord
from discord.ext import commands

import settings


initial_extensions = ["modules.image", "modules.fortnite"]
TOKEN = os.getenv("DISCORD_BOT_API_TOKEN")
bot = commands.Bot(command_prefix="!")

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}.", file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")


@bot.command()
async def greet(ctx):
    await ctx.send(":wave: Hello there!")


bot.run(TOKEN)
