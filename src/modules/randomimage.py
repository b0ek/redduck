import discord
import requests


def process(search_args):
    url = 'https://loremflickr.com/'
    search_url = (f'https://loremflickr.com/320/240/{search_args}')
    info = (f'A random picture related to ({search_args})')

    embed = discord.Embed(
            title=search_args,
            type='rich',
            description="{0}\n{1}".format(info, search_url),
            url=search_url,
            image=search_url).set_image(url=search_url)

    return embed
