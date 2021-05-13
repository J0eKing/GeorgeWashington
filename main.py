from asyncio.tasks import Task
import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks  # Importing tasks here
import os
from keep import keep_alive
import get

x = []
channelID = 841773185128464415
message = """**BEEP BOOP FREE GAME ALERT**

**{}**
{}

Next free game is
*{}*"""


def get_last_game():
    with open("game.txt", "r") as f:
        last_game = f.readline()
    return last_game


def set_last_game(name):
    with open("game.txt", "w") as f:
        f.write(name)


bot = Bot(command_prefix='.')


def check_if_new():
    global x
    x = get.get_games()
    if x == None:
        return None
    if x[0] != get_last_game():
        print("NEW GAME ALERT BEEP BOOP")
        set_last_game(x[0])
        return True
    else:
        print("NO NEW GAMES :(")
        return False


@tasks.loop(seconds=600)
async def check_new_game():
    new = check_if_new()
    if new == None:
        return
    if new:
        channel = bot.get_channel(channelID)
        await channel.send(message.format(x[0], x[1], x[2]))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('kys'))
    print(f'Bot connected as {bot.user}')
    check_new_game.start()


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    print(message)


TOKEN = os.getenv('TOKEN')
bot.run("NzM1MDg1NzcxODE5NzEyNTgy.XxbH-Q.oxdTbGYD0jJtDFdilg62fAU2vhM")
# print(check_if_new())
