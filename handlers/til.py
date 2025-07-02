import os
import sys

async def handle_til(message):
    facts_database_path = 'facts.txt'
    os.makedirs(os.path.dirname(facts_database_path), exist_ok=True)
    fact = message.content[4:].strip()
    if not fact:
        await message.channel.send('Please provide a fact after !til, you dumbo.')
        return
    try:
        with open(facts_database_path, 'a', encoding='utf-8') as f:
            f.write(fact + '\n')
        await message.channel.send(f'One more useless fact added: `{fact}`')
    except Exception as e:
        await message.channel.send("Couldn't save that. I might be broken, or sad.")
