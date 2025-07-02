import requests
import calendar
import time

async def handle_nextstream(message, twitch_token, twitch_client_id):
    parts = message.content.strip().split()
    if len(parts) < 2:
        await message.channel.send("Please provide a Twitch username. Usage: `!nextstream username`")
        return

    user_login = parts[1]

    headers = {
        'Client-ID': twitch_client_id,
        'Authorization': f'Bearer {twitch_token}'
    }

    user_resp = requests.get(f'https://api.twitch.tv/helix/users?login={user_login}', headers=headers)
    user_data = user_resp.json()
    user_id = user_data['data'][0]['id']

    schedule_resp = requests.get(f'https://api.twitch.tv/helix/schedule?broadcaster_id={user_id}', headers=headers)
    schedule_data = schedule_resp.json()

    try:
        segments = schedule_data['data']['segments']
        if not segments:
            await message.channel.send("No upcoming streams found.")
            return
        next_stream = segments[0]
        title = next_stream.get('title', 'Untitled stream')
        start = next_stream['start_time']

        ts = int(calendar.timegm(time.strptime(start, "%Y-%m-%dT%H:%M:%SZ")))
        await message.channel.send(f"Next stream: `{title}` at <t:{ts}:F>")

    except Exception as e:
        await message.channel.send(f"Error parsing schedule: {e}")
