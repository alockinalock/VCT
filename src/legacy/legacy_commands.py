import discord
import dotenv
import os

from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands, tasks

load_dotenv()
token = os.getenv("token")

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

# bot parses through all messages (may be resource costly)
@bot.event
async def on_message(message):
    # prevent bot from responding to itself
    if message.author == bot.user:
        return

    # FIXME: may need to abstract message.content.lower() to a var
    match message.content.lower():
        case "!debug.log":
            # FIXME: Mention the user who sent the message
            await message.channel.send(f"{message.author} invoked !debug.log")
        case _:
            # TODO: yeah no autocomplete function here... not yet
            pass
    
# turn this file into a class to be used for main.py
if __name__ == '__main__':
    print("Initializing only legacy commands")
    bot.run(token)