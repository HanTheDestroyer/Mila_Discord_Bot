import numpy as np
import sys

async def handle_flip(message):
    flip_openers_path = 'sources/flip_openers.txt'
    result = "Heads" if np.random.rand() < 0.5 else "Tails"
    
    try:
        with open(flip_openers_path, 'r', encoding='utf-8') as f:
            openers = [line.strip() for line in f if line.strip()]
        opener = np.random.choice(openers).replace('{user}', message.author.display_name)
    except Exception as e:
        print(f"[ERROR] Reading flip openers file: {e}", file=sys.stderr)
        opener = f"The coin landed on, {message.author.display_name}:"

    await message.channel.send(f"{opener} `{result}`")
