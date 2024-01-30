import discord # may need more than just importing

from commands.py import *

class Legacy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def on_message(self, message):
        # prevent both from responding to self
        if message.author == bot.user:
            return
        
        match message.content.lower():
            case "!debug.log":
                debug_log(message)
            case _:
                pass # TODO: replace with autocomplete function

