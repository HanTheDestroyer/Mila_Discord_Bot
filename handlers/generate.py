import requests
import base64
from io import BytesIO
import discord

async def handle_generate(message):
    parts = [p.strip() for p in message.content[len('!generate'):].split('|')]
    prompt = parts[0] if len(parts) > 0 else "An amazing image"
    negative_prompt = parts[1] if len(parts) > 1 else "nude"
    try:
        width = int(parts[2]) if len(parts) > 2 else 512
        height = int(parts[3]) if len(parts) > 3 else 512
    except ValueError:
        await message.channel.send("Width and height must be numbers.")
        return
    if not prompt:
        await message.channel.send("Please provide a prompt after !generate.")
        return
    msg = f'Fucking hell, {message.author.display_name}, I am doing it. Just wait.\n'
    msg += f"You said something like: `{prompt}`\n"
    if negative_prompt == "nude":
        msg += 'You did not provide a negative prompt, so I will use "nude", you perv.\n'
    else:
        msg += f"You don't want any: `{negative_prompt}`\n"
    if width > 1024 or height > 1024:
        msg += f"Oh fuck, the resolution {width}x{height} is rather large, which may cause issues.\n"
    else:
        msg += f"Resolution: `{width}x{height}`"
    await message.channel.send(msg)
    response = requests.post(
        "http://127.0.0.1:7860/sdapi/v1/txt2img",
        json={
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height
        }
    )
    if response.status_code == 200:
        result = response.json()
        img_data = result['images'][0]
        img_bytes = base64.b64decode(img_data)
        file = discord.File(BytesIO(img_bytes), filename="result.png")
        await message.channel.send(file=file)
    else:
        await message.channel.send("Failed to generate image.")
