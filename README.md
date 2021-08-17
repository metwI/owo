[![GitHub release](https://img.shields.io/github/release/zenithtea/owo.svg)](https://github.com/zenithtea/owo/releases/latest)
[![test server](https://discordapp.com/api/guilds/841966583932256266/widget.png?style=shield)](https://discord.gg/ppu7afZhDZ)

[OwO](https://github.com/ChristopherBThai/Discord-OwO-Bot) bot'un otomatik para kazanması veya sunucunuzda ki aktifliğin çeşitli botlar ile arttırılabildiği veya [Tatsu](https://tatsu.gg)'de otomatik XP ve Level kastığı bir depolama alanıdır. Bu depolama alanın yapılma sebebi bu botlar ile kazandıklarımızı hem daha çok arttırmak hem de zamanımızdan kaybetmemek adınadır. Bu depolama alanı [Discord Hizmet Şartları](https://discord.com/terms)'nı çiğniyor, bu yüzden de kullanılması durumunda sorumluluk bana ait değildir.

[![Discord Bots](https://discordbots.org/api/widget/status/408785106942164992.svg)](https://discordbots.org/bot/408785106942164992)  [![Discord Bots](https://discordbots.org/api/widget/servers/408785106942164992.svg)](https://discordbots.org/bot/408785106942164992)  [![Discord Bots](https://discordbots.org/api/widget/lib/408785106942164992.svg)](https://discordbots.org/bot/408785106942164992)

[![Discord Bots](https://discordbots.org/api/widget/status/172002275412279296.svg)](https://discordbots.org/bot/172002275412279296)  [![Discord Bots](https://discordbots.org/api/widget/servers/172002275412279296.svg)](https://discordbots.org/bot/172002275412279296)  [![Discord Bots](https://discordbots.org/api/widget/lib/172002275412279296.svg)](https://discordbots.org/bot/172002275412279296)

```
import discord, random
from discord.ext import tasks

client = discord.Client()

channel = None

@tasks.loop(seconds=1) # saniyesini yanda ki bölümden ayarlayabilirsiniz
async def send_message():
  global channel
  await channel.send(random.choice(['mesaj'], ['mesaj']))
# bu yazdığınız mesaj kutularından rastgele birisini seçtiğiniz saniye de gönderir
# eğer tek mesaj olmasını istiyorsanız ikinci kutuyu silebilirsiniz.

@client.event
async def on_ready():
  global channel
  channel = await client.fetch_channel('843053470876696627')
# hangi kanala göndermesini istiyorsanız buraya o kanalın ID'sini koyun
# ID alabilmek için > Kullanıcı Ayarları > Gelişmiş > Geliştirici Modu'nu açın. 
# Kanala sağ tıklayın en aşağıda ki  "COPY ID" bölümüne tıklayarak alabilirsiniz.
  
print(channel)
  print('We have logged in as {0.user}'.format(client))
  send_message.start()

from webserver import keep_alive
import os
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET") 
# repl.it ve/veya başka bir site kullanıyorsanız, 
# .env bölümünden yeni bir kutucak açıp ismini "DISCORD_BOT_SECRET" koyarak açıklama bölümüne de 
# self ve/veya normal bir bot'un tokenini koyabilirsiniz.

client.run(token, bot=False) # eğer bir self bot ise böyle kalmalı eğer normal bir bot ise - 'bot=True' yapınız.
```
