import os

import discord
from discord.ext import commands

import settings
from modules import randomimage

TOKEN = os.getenv('DISCORD_BOT_API_TOKEN')
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')


@bot.command()
async def greet(ctx):
    await ctx.send(':wave: Hello there!')


@bot.command(
    name='image',
    description='Retrieves a random picture related to the search args',
    brief='Retrieves a random picture')
async def get_randompic(ctx, arg):
    try:
        embed = randomimage.process(arg)
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send("Sorry, something went wrong.")

bot.run(TOKEN)
