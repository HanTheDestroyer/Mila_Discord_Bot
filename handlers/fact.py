import numpy as np
import sys

async def handle_fact(message):
    facts_database_path = 'sources/facts.txt'
    fact_openers_path = 'sources/fact_openers.txt'
    try:
        with open(fact_openers_path, 'r', encoding='utf-8') as f:
            fact_openers = [line.strip() for line in f]
        fact_opener = np.random.choice(fact_openers).replace('{user}', message.author.display_name)
    except Exception as e:
        print(f"[ERROR] Reading fact openers file: {e}", file=sys.stderr)
        fact_opener = f"Hey {message.author.display_name}, here's a fact for you!"
    
    try:
        with open(facts_database_path, 'r', encoding='utf-8') as f:
            facts = [line.strip() for line in f]
        fact = np.random.choice(facts)
    except Exception as e:
        print(f"[ERROR] Reading facts file: {e}", file=sys.stderr)
        fact = "I couldn't find any facts to share right now. Please try again later."

    reply_msg = f"{fact_opener}\n`{fact}`"
    await message.channel.send(reply_msg)
