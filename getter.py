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

    for thread in threads:
        if str(thread.parent) == 'zkapps-questions' or str(thread.parent) == 'zkapps-developers':
            if thread.created_at.timestamp() < days_ago:
                solved_threads.append(thread)
                continue
            for tag in thread.applied_tags:
                if tag.name == 'Solved':
                    solved_threads.append(thread)
                    break
        else:
            continue

    thread_ids = [id.id for id in solved_threads]
    os.makedirs('threads', exist_ok=True)
    print(len(solved_threads))

    for counter, thread_id in enumerate(thread_ids):
        thread = guild.get_thread(thread_id)
                
        if thread:
            with open(f"threads/{counter}.csv", "w", newline='') as f:
                try:
                    message_writer = csv.writer(f)
                    message_writer.writerow([
                        "thread_name",
                        "id",
                        "channel_id",
                        "author",
                        "content",
                        "timestamp",
                        "mentions",
                        "reactions",
                        "referenced_message",
                        "member"
                    ])
                except:
                    print("error")

                print(f"Retrieving messages for thread: {thread.name}")
                async for message in thread.history(limit=100):
                    try:
                        message_writer = csv.writer(f)
                        message_writer.writerow([
                            thread.name,
                            message.id,
                            message.channel.id,
                            message.author.id,
                            message.content,
                            message.created_at,
                            message.mentions,
                            message.reactions,
                            message.reference.message_id if message.reference is not None else None,
                            message.author
                        ])
                    except Exception as e:
                        print(e)
        else:
            print(f"Thread with ID {thread_id} not found in guild {guild.name}")
    

# Run the client
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv(), override=True)
discord_token = os.getenv('DISCORD_TOKEN')

cor = client.start(discord_token)

asyncio.get_event_loop().run_until_complete(cor)