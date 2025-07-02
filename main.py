import discord
import os

from handlers.generate import handle_generate
from handlers.hello import handle_hello
from handlers.flip import handle_flip
from handlers.roll import handle_roll
from handlers.ping import handle_ping
from handlers.til import handle_til
from handlers.fact import handle_fact
from handlers.felon import handle_felon
from handlers.nextstream import handle_nextstream
from handlers.mumios import handle_mumios
from handlers.gif import handle_gif
from handlers.schedule import handle_schedule
from credentials import *

intents = discord.Intents.default()
intents.message_content = True



COMMAND_HANDLERS = {
    '!generate': handle_generate,
    '!hello': handle_hello,
    '!flip': handle_flip,
    '!roll': handle_roll,
    '!ping': handle_ping,
    '!til': handle_til,
    '!fact': handle_fact,
    '!felon': handle_felon,
    '!nextstream': handle_nextstream,
    '!mumios': handle_mumios,
    '!gif': handle_gif,
    '!schedule': handle_schedule,
}

class Mila(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user}.')

    async def on_message(self, message):
        if message.author == self.user:
            return
        content = message.content.lower()
        for cmd, handler in COMMAND_HANDLERS.items():
            if content.startswith(cmd):
                # nextstream needs Twitch credentials
                if cmd == '!nextstream' or cmd == '!schedule':
                    await handler(message, TWITCH_TOKEN, TWITCH_CLIENT_ID)
                elif cmd == '!gif':
                    await handler(message, TENOR_API_KEY)
                else:
                    await handler(message)
                break

if __name__ == '__main__':
    bot = Mila()
    bot.run(TOKEN)
