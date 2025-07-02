import requests
import calendar
import time
import discord

async def handle_schedule(message, twitch_token, twitch_client_id):
    parts = message.content.strip().split()
    if len(parts) < 2:
        await message.channel.send("Please provide a Twitch username. Usage: `!schedule username`")
        return

    user_login = parts[1]
    headers = {
        'Client-ID': twitch_client_id,
        'Authorization': f'Bearer {twitch_token}'
    }

    try:
        user_resp = requests.get(f'https://api.twitch.tv/helix/users?login={user_login}', headers=headers)
        user_data = user_resp.json()
        user_id = user_data['data'][0]['id']
    except Exception as e:
        await message.channel.send(f"❌ Error fetching Twitch user ID: {e}")
        return

    try:
        schedule_resp = requests.get(f'https://api.twitch.tv/helix/schedule?broadcaster_id={user_id}', headers=headers)
        schedule_data = schedule_resp.json()
        segments = schedule_data['data']['segments']
        if not segments:
            await message.channel.send("📭 No upcoming streams found.")
            return
    except Exception as e:
        await message.channel.send(f"❌ Error fetching schedule: {e}")
        return

    def parse_segment(segment):
        title = segment.get('title', 'Untitled Stream')
        start = segment.get('start_time')
        end = segment.get('end_time')

        tstart = int(calendar.timegm(time.strptime(start, "%Y-%m-%dT%H:%M:%SZ"))) if start else None
        tend = int(calendar.timegm(time.strptime(end, "%Y-%m-%dT%H:%M:%SZ"))) if end else None
        return title, tstart, tend

    # Create a Discord embed for the schedule
    embed = discord.Embed(
        title="📺 Weekly Stream Schedule",
        description="Here's when the user will be streaming this week!\n\nAll times in your local timezone",
        color=0x9147ff  # Twitch purple color
    )
    
    for i, segment in enumerate(segments[:4]):
        title, tstart, tend = parse_segment(segment)
        
        # Create time range text
        if tstart and tend:
            time_text = f"<t:{tstart}:F> - <t:{tend}:t>"
        elif tstart:
            time_text = f"<t:{tstart}:F> - TBD"
        else:
            time_text = "TBD"
        
        # Add field for each stream
        embed.add_field(
            name=f"**{title}**",
            value=time_text,
            inline=False
        )
    
    # Add footer with source info
    embed.set_footer(text="Source: Twitch")
    
    await message.channel.send(embed=embed)
