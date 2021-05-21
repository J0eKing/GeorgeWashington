import discord
from discord.ext.commands import Bot
from discord.ext import tasks  # Importing tasks here
import os
import get

x = []
bot = Bot(command_prefix='.')
message = """**BEEP BOOP FREE GAME ALERT**

**{}**
{}"""

channelID = 841773185128464415


def get_last_game():
    with open("game.txt", "r") as f:
        last_game = f.readline()
    return last_game


def set_last_game(name):
    with open("game.txt", "w+") as f:
        f.write(name)


def check_if_new():
    global x
    print("LFG")
    x = get.main()
    if x[0] != get_last_game():
        print("new game")
        set_last_game(x[0])
        return True
    else:
        print(":(")
        return False


@tasks.loop(seconds=86400)
async def check_new_game():
    print("checking")
    new = check_if_new()
    if new == None:
        return
    if new:
        channel = bot.get_channel(channelID)
        await channel.send(message.format(x[0], x[1]))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('LFG'))
    print(f'Bot connected as {bot.user}')
    check_new_game.start()


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    print(message)

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
