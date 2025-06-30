import numpy as np
import os

async def handle_hello(message):
    greetings_path = 'C:/Users/han/Documents/Projects/Mila/sources/greetings.txt'
    os.makedirs(os.path.dirname(greetings_path), exist_ok=True)
    try:
        with open(greetings_path, 'r', encoding='utf-8') as f:
            greetings = [line.strip() for line in f]
        greeting = np.random.choice(greetings).replace('{user}', message.author.display_name)
        await message.channel.send(greeting)
    except Exception as e:
        print(f"Error reading greetings file: {e}")
        await message.channel.send(f"Hello, {message.author.display_name}. I am having trouble reading my greetings.")
