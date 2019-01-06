import discord

class Client(discord.Client):

    async def on_ready(self):
        print('We have logged in as {0}'.format(self.user))

    async def on_message(self, message):
        pass

    