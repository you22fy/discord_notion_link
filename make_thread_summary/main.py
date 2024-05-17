import discord
import os
from dotenv import load_dotenv

from utils.has_url_in_text import has_url_in_text
from utils.get_content_by_url import get_content_by_url
from utils.summarize_text_by_openai import summarize_text

load_dotenv()
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if url := has_url_in_text(message.content):
        try:
            title, ogp_url, body_text = get_content_by_url(url)
            summary = summarize_text(body_text)
            return_message = message
            return_message.content = ogp_url
            thread = await message.channel.create_thread(
                name=f"{str(title)}の議論スレッド",
                message=return_message,
            )
            await thread.send(f"# 要約\n{summary}")
        except Exception as e:
            print(f"Error creating thread: {e}")


client.run(DISCORD_API_KEY)
