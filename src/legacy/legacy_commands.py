import discord
import dotenv

from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands, tasks

load_dotenv()
token = os.getenv("token")

if __name__ == '__main__':
    print("Initializing only legacy commands")
    bot.run(token)

# FIXME: this may not work for legacy commands (specifically line 21)
@bot.event
async def on_ready():
    print(f"{bot.user} has been initialized WITH only legacy commands.")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} legacy command(s) successfully loaded.")
    except Exception as error:
        print(error)

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
    
