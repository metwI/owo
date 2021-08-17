import discord, random
from discord.ext import tasks

client = discord.Client()

channel = None

@tasks.loop(seconds=1)
async def send_message():
  global channel
  await channel.send(random.choice(['cu ne? ananın amcuuuuuuuu']))

@client.event
async def on_ready():
  global channel
  channel = await client.fetch_channel('843053470876696627')
  print(channel)
  print('We have logged in as {0.user}'.format(client))
  send_message.start()

from webserver import keep_alive
import os
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run("ODc3MDgwNDg5NDM2MDA0MzUz.YRtgNQ.aE4A7pLzc9VgNfYNy1SkLdArlqk", bot=False)