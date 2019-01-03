import asyncio
import os

import discord

from PyDictionary import PyDictionary


client = discord.Client()


@client.event
async def on_ready():
    print('Ready!')


def format_meaning(word, meaning):
    reply = f'**{word}**\n\n'
    for word_type, definitions in meaning.items():
        reply += f'*{word_type}*\n'
        counter = 1
        for definition in definitions:
            reply += f'    {counter}. {definition}\n'
            counter += 1
    return reply


async def handle_message(message):
    try:
        word = message.content[5:]
        meaning = PyDictionary.meaning(word)
        if meaning:
            reply = format_meaning(word, meaning)
        else:
            reply = f'Sorry, {word} has no definition. :('
    except:
        reply = 'Sorry, an error occurred while fetching that definition.'
    await client.send_message(message.channel, reply)


@client.event
async def on_message(message):
    if message.content.startswith('/def '):
        await handle_message(message)


client.run(os.environ.get('DISCORD_TOKEN'))
