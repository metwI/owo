import discord, random
from discord.ext import tasks

client = discord.Client()

channel = None

@tasks.loop(seconds=1) # saniyesini yanda ki bölümden ayarlayabilirsiniz
async def send_message():
  global channel
  await channel.send(random.choice(['mesaj'], ['mesaj'])) # bu yazdığınız mesaj kutularından rastgele birisini seçtiğiniz saniye de gönderir, eğer tek mesaj olmasını istiyorsanız ikinci kutuyu silebilirsiniz.

@client.event
async def on_ready():
  global channel
  channel = await client.fetch_channel('843053470876696627') # hangi kanala göndermesini istiyorsanız buraya o kanalın ID'sini koyun, ID alabilmek için > Kullanıcı Ayarları > Gelişmiş > Geliştirici Modu'nu açın. Kanala sağ tıklayın en aşağıda ki  "COPY ID" bölümüne tıklayarak alabilirsiniz.
  print(channel)
  print('We have logged in as {0.user}'.format(client))
  send_message.start()

from webserver import keep_alive
import os
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET") # repl.it ve/veya başka bir site kullanıyorsanız, .env bölümünden yeni bir kutucak açıp ismini "DISCORD_BOT_SECRET" koyarak açıklama bölümüne de self ve/veya normal bir bot'un tokenini koyabilirsiniz.

client.run(token, bot=False) # eğer bir self bot ise böyle kalmalı eğer normal bir bot ise - 'bot=True' yapınız.
