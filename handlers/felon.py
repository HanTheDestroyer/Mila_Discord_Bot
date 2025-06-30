import discord
import numpy as np
import sys

async def handle_felon(message):
    opener_path = 'sources/felon_barbie.txt'
    audio_path = 'sources/audio/felon_barbie.mp3'

    try:
        with open(opener_path, 'r', encoding='utf-8') as f:
            openers = [line.strip() for line in f if line.strip()]
        opener = np.random.choice(openers)
    except Exception as e:
        print(f"[ERROR] Reading felon openers file: {e}", file=sys.stderr)
        opener = "Brace yourself. Felon's trash track incoming."

    try:
        await message.channel.send(content=opener, file=discord.File(audio_path))
    except Exception as e:
        print(f"[ERROR] Sending Felon media: {e}", file=sys.stderr)
        await message.channel.send("Something broke while sending Felon's masterpiece. He'll cry about it later.")
