import requests
import discord

async def handle_gif(message, tenor_api_key):
    query = message.content[len('!gif'):].strip()
    if not query:
        await message.channel.send("You forgot to tell me what gif you want, genius.")
        return

    url = f"https://tenor.googleapis.com/v2/search?q={query}&key={tenor_api_key}&limit=1&media_filter=minimal"
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            await message.channel.send("Tenor is acting up. Try again later.")
            return
        
        data = resp.json()
        if not data.get('results'):
            await message.channel.send("No gifs found. Maybe your taste is just awful.")
            return
        
        gif_url = data['results'][0]['media_formats']['gif']['url']
        await message.channel.send(gif_url)
    except Exception as e:
        await message.channel.send(f"Something fucked up: {e}")
