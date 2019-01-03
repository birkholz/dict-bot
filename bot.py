import asyncio
import os

import discord

from PyDictionary import PyDictionary


client = discord.Client()


@client.event
async def on_ready():
    print('Ready!')


def format_meaning(meaning):
    reply = ''
    for word_type, definitions in meaning.items():
        reply += f'*{word_type}*\n'
        counter = 1
        for definition in definitions:
            reply += f'  {counter}. {definition}\n'
            counter += 1
    return reply


async def handle_message(message):
    meaning = PyDictionary.meaning(message.content[5:])
    reply = format_meaning(meaning)
    await client.send_message(message.channel, reply)


@client.event
async def on_message(message):
    if message.content.startswith('/def '):
        await handle_message(message)


client.run(os.environ.get('DISCORD_TOKEN'))
