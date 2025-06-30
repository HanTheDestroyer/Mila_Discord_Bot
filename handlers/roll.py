import numpy as np

async def handle_roll(message):
    dice_types = message.content[len('!roll'):].strip().split(', ')
    if not dice_types or (len(dice_types) == 1 and dice_types[0] == ''):
        dice_types = ['1d20']
    for dice_type in dice_types:
        try:
            num, die = dice_type.split('d')
            num = int(num)
            die = int(die)
            if num < 1 or die < 1:
                await message.channel.send("Invalid dice format. Use 'XdY' where X is the number of dice and Y is the type of die.")
                return
            rolls = [np.random.randint(1, die + 1) for _ in range(num)]
            msg = f"Rolled {num}d{die} 🎲: `{', '.join(map(str, rolls))}` `(Total: {sum(rolls)})`\n"
            if 1 in rolls:
                msg += "You rolled a 1! Loser 🎯!\n"
            await message.channel.send(msg)
        except ValueError:
            await message.channel.send("Invalid dice format. Use 'XdY' where X is the number of dice and Y is the type of die.")
            return
