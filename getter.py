import discord
import asyncio
from datetime import datetime, timedelta
import os
import csv

from typing import AsyncIterator

# Create a new instance of the Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

FORUM_CHANNEL_ID = 1047214314349658172
GUILD_ID = 484437221055922177

AFTER_DAYS = 7

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Specify the guild and channel by ID
    guild = discord.utils.get(client.guilds, id=GUILD_ID)
    channel = discord.utils.get(guild.channels, id=FORUM_CHANNEL_ID)

    if guild is None or channel is None:
        print('Guild or Channel not found')
        return
    
    days_ago = (datetime.utcnow() - timedelta(days=AFTER_DAYS)).timestamp()

    threads = await guild.active_threads()

    solved_threads = []
    thread_ids = [id.id for id in solved_threads]

    for thread in threads:
        if str(thread.parent) == 'zkapps-questions' | str(thread.parent) == 'zkapps-developers':
            if thread.created_at.timestamp() < days_ago:
                solved_threads.append(thread)
                continue
            for tag in thread.applied_tags:
                if tag.name == 'Solved':
                    solved_threads.append(thread)
                    break
        else:
            continue

    os.makedirs('active_threads', exist_ok=True)
    print("\n".join(str(element) for element in solved_threads))
    

# Run the client
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv(), override=True)
discord_token = os.getenv('DISCORD_TOKEN')

cor = client.start(discord_token)

asyncio.get_event_loop().run_until_complete(cor)