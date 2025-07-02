import discord
import numpy as np
import sys

async def handle_mumios(message):
    opener_path = 'sources/mumios_balatro.txt'
    image_path = 'sources/images/mumios.gif'

    try:
        with open(opener_path, 'r', encoding='utf-8') as f:
            openers = [line.strip() for line in f if line.strip()]
        opener = np.random.choice(openers)
    except Exception as e:
        print(f"[ERROR] Reading mumios openers file: {e}", file=sys.stderr)
        opener = "Fucking addict."

    try:
        await message.channel.send(content=opener, file=discord.File(image_path))
    except Exception as e:
        print(f"[ERROR] Sending Mumios media: {e}", file=sys.stderr)
        await message.channel.send("Something broke while sharing Mumios' addiction. He'll cry about it later.")
