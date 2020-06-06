import asyncio
import os

import discord

from nltk.corpus import wordnet


client = discord.Client()


@client.event
async def on_ready():
    print('Ready!')


PARTS_OF_SPEECH = {
    wordnet.NOUN: "Noun",
    wordnet.ADJ: "Adjective",
    wordnet.VERB: "Verb",
    wordnet.ADJ_SAT: "Adjective Satellite",
    wordnet.ADV: "Adverb"
}


def format_meaning(word, synsets):
    reply = f'**{word}**\n\n'
    counter = 1
    for synset in synsets:
        reply += f'*{PARTS_OF_SPEECH[synset.pos()]}*\n'
        reply += f'    {counter}. {synset.definition()}\n'
        counter += 1
    return reply


async def handle_message(message):
    try:
        word = message.content[5:]
        synsets = wordnet.synsets(word)
        if synsets:
            reply = format_meaning(word, synsets)
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
