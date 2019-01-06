from redduckclient import Client
import os

client = Client()
client.run(os.environ.get('BOT_TOKEN'))



