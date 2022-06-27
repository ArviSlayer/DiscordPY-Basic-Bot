import discord
import time
from discord.ext import commands,tasks
from admins import keys
import os
from itertools import cycle
import komutlar
intents = discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix=".",intents=discord.Intents.all())

    
durumlar = cycle(["ArviS","Python","Bot"])
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=(next(durumlar))))

@client.command()
async def load(ctx,extension):
    client.load_extension(f'komutlar.{extension}')

for x in 'len(./komutlar)':
    print ("Çalışıyor")

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'komutlar.{extension}')

for filename in os.listdir('./komutlar'):
    if filename.endswith('.py'):
        client.load_extension(f'komutlar.{filename[:-3]}')

@client.event
async def on_ready():
    change_status.start()
    print("Modüller Aktif")
    print("Bot ID: {}".format(keys.botId))



client.run(keys.token)