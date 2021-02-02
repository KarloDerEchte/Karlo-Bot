import discord
import os

client = discord.Client()

@client.event

async def on_ready():
  print('Eingeloggt als {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content.startswith("§help"):
    await message.channel.send("SoonTM")

client.run(os.getenv('TOKEN'))