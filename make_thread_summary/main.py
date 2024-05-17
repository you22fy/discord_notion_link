import discord
import os
from dotenv import load_dotenv

from utils.has_url_in_text import has_url_in_text

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
            thread = await message.channel.create_thread(
                name=f"{url}の議論スレッド",
                message=message,
            )
            await thread.send("このURLについての議論スレッドを作成しました！")
        except Exception as e:
            print(f"Error creating thread: {e}")


client.run(DISCORD_API_KEY)
