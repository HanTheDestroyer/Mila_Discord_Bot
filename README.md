# Mila — The Snarky Discord Bot

Mila is your not-so-friendly, dirty‑mouthed Discord companion built with `discord.py`. She doesn’t just flip coins or roll dice — she mocks you while doing it. From image generation and voice messages to Twitch integration and user‑targeted sarcasm, Mila brings attitude with functionality.

---

## 💣 Features

- **Image generation** (`!generate`)
- **Audio and image responses**
- **Dice roll** (`!roll`)
- **Coin flip** (`!flip`)
- **Greetings and facts** (`!hello`, `!fact`, `!til`)
- **Dirty-mouthed remarks** (`!felon`)
- **Twitch stream info** (`!nextstream`)
- **Twitch schedule** (`!schedule`)
- **Mocking users with Balatro flair** (`!mumios`)
- Modular command handler structure

---

## ⚙️ Getting Mila Running

1. **Clone the repository:**
   ```sh
   git clone https://github.com/HanTheDestroyer/Mila_Discord_Bot.git
   cd Mila_Discord_Bot
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure credentials:**
   Edit the provided `credentials.py` file and fill in your Discord and Twitch tokens.

4. **Run the bot:**
   ```sh
   python main.py
   ```

---

## 🧾 Available Commands

| Command        | Description                                   |
|----------------|-----------------------------------------------|
| `!generate`    | Generate images                               |
| `!hello`       | Mila says hello                               |
| `!flip`        | Flip a coin                                   |
| `!roll`        | Roll a dice                                   |
| `!ping`        | Ping response                                 |
| `!til`         | Today I Learned fact                          |
| `!fact`        | Random fact                                   |
| `!felon`       | Dirty-mouthed remark                          |
| `!nextstream`  | Twitch stream info                            |
| `!schedule`    | Retrieve Twitch stream schedule               |
| `!mumios`      | Mock user with bad words & Balatro image      |

---

## 🗂️ Project Structure

Mila_Discord_Bot/
├── handlers/              # Command-specific logic
│   └── handle_*.py        # Modular command files
├── sources/               # Static resources used by commands
│   ├── audio/             # Audio clips
│   │   └── felon_barbie.mp3
│   ├── images/            # GIFs, PNGs, etc.
│   │   └── mumios.gif
│   ├── facts.txt
│   ├── flip_openers.txt
│   └── ...
├── main.py                # Entry point
├── requirements.txt       # Dependencies
└── README.md              # You are here

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
