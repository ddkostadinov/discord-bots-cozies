import discord
import os
import requests
import json
import random
import random_quotes


intents = discord.Intents.default()
intents.message_content = True
my_secret = '[insert secret]'
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("We've logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$cookie'):
    await message.channel.send(random.choice(random_quotes.quotes))

client.run(my_secret)
