"""
Bot that checks bhphoto, newegg, and amazon for stock
"""
import discord
import logging
import dtoken
import stonkreplies

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
prefix = 's!'


@client.event
async def on_ready():
    print('Item stock notifier discord bot.')
    print('Copyright (C) 2021 hinuiiik>')
    print('\nBot has started as {0.user}'.format(client))
    await client.change_presence(
        activity=discord.Streaming(name='Prefix: s!', url='https://www.youtube.com/watch?v=xuCO7-DLCaA'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "s!help" or message.content == "s!":
        await message.channel.send(stonkreplies.helptext)


client.run(dtoken.discordtoken)
