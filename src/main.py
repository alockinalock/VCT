import discord
import os

from legacy.legacy_commands import *
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands, tasks

load_dotenv()
token = os.getenv("token")

# call the bot's commands with ! (for legacy commands)
# TODO: legacy implementation, attempt to find newer way
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

# bot init
@bot.event
async def on_ready():
    print(f'{bot.user} is online')
    try:
        # may need to abstract the await statement into a var
        print(f"{len(await bot.tree.sync())} command(s) successfully loaded.")
    except Exception as error:
        print(error)

# DEV COMMAND: multi-test command
@bot.tree.command(name="debug-log-input-taken", description="developer command that tests a multitude of variables")
async def debug_log_input(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f"{interaction.user.mention} has said {text} in {interaction.channel.name} which has an ID of {interaction.channel_id}")

# TODO: The bot does not have legacy commands implemented
if __name__ == '__main__':
    print("Initializing both slash commands and legacy commands.")
    bot.run(token)