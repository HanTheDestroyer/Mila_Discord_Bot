# Mila — The Snarky Discord Bot

Mila is your not-so-friendly, dirty‑mouthed Discord companion built with `discord.py`. She doesn’t just flip coins or roll dice — she mocks you while doing it. From image generation and voice messages to Twitch integration and user‑targeted sarcasm, Mila brings attitude with functionality.

---

## 💣 Features

- 🎨 **Image Generation** — `!generate` (WebUI 1111)
- 🎲 **Dice Rolling & Coin Flipping** — `!roll`, `!flip`
- 🧠 **Snarky Facts** — `!fact`, `!til`
- 🗣️ **Personalized User Roasts** — `!felon` (audio clip + image targeting a specific user)
- 📡 **Twitch Stream Tracking** — `!nextstream`
- 💬 **Modular Command System** — Clean handler architecture
- 😈 **Mouth of a sailor** — Mila doesn’t sugarcoat. Ever.

---

## ⚙️ Getting Mila Running

1. **Clone this menace**  
       git clone https://github.com/HanTheDestroyer/Mila_Discord_Bot.git  
       cd Mila_Discord_Bot

2. **Install her dependencies**  
       pip install -r requirements.txt

3. **Prepare your secrets**  
   In `main.py`, fill in:  
       TOKEN = 'DISCORD_TOKEN_HERE'  
       TWITCH_TOKEN  = 'TWITCH_TOKEN_HERE'  
       TWITCH_CLIENT_ID     = 'TWITCH_CLIENT_ID_HERE'  
       TWITCH_CLIENT_SECRET = 'TWITCH_CLIENT_SECRET_HERE'

4. **Launch Mila**  
       python main.py

---

## 🧾 Available Commands

| Command       | Description                                       |
|---------------|---------------------------------------------------|
| `!hello`      | Mila says hi. You’ll regret asking.               |
| `!flip`       | Flips a coin with some sass.                      |
| `!roll`       | Rolls a die. Might insult your luck.              |
| `!fact`       | Useless facts delivered with attitude.            |
| `!til`        | “Today I Learned” — because you need it.          |
| `!felon`      | Drops audio from ConvictedFelon77 — mock included |
| `!generate`   | Image generation via WebUI (port 1111 required)   |
| `!nextstream` | Twitch stream info (credentials needed)           |
| `!ping`       | Pong. Simple, but Mila makes it personal.         |

---

## 🗂️ Project Structure

    Mila_Discord_Bot/
    ├── handlers/          # Command-specific logic
    │   └── handle_*.py    # Modular command files
    ├── sources/           # Facts, audio, images, text openers
    │   ├── facts.txt
    │   ├── flip_openers.txt
    │   ├── felon_barbie.mp3
    │   └── ...
    ├── main.py            # Entry point
    ├── requirements.txt   # Dependencies
    └── README.md          # You are here

---

## 🧨 Notes

- Mila does **not** join voice chats. She sends **voice messages** of pre-created audio files instead.
- All voice and image files live in `sources/`.
- Customize her personality through the various `*.txt` openers.

---

## 📜 License

MIT. Use it, fork it, break it — just don’t blame Mila when it goes wrong.

---

> _“I’m not your average bot. I’m Mila. Learn the difference.”_
