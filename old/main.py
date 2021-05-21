import discord
from discord.ext.commands import Bot
from discord.ext import tasks  # Importing tasks here
import os
import get
from flask import Flask
from threading import Thread

app = Flask('asdasd')


@app.route('/')
def home():
    return "I'm alive"


def run():
    print("start server")
    app.run(host='0.0.0.0', port=6666)


t = Thread(target=run)
t.start()

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
    print("LFG")
    x = get.get_games()
    if x[0] == None:
        exit()
    if x[0] != get_last_game():
        print("NEW GAME ALERT BEEP BOOP")
        set_last_game(x[0])
        return True
    else:
        print("NO NEW GAMES :(")
        return False


@tasks.loop(seconds=86400)
async def check_new_game():
    print("checking")
    new = check_if_new()
    if new == None:
        return
    if new:
        channel = bot.get_channel(channelID)
        await channel.send(message.format(x[0], x[1], x[2]))


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
bot.run("NzM1MDg1NzcxODE5NzEyNTgy.XxbH-Q.qLYkfAktZznzptoVJv5MqVnwB6o")
t.raise_exception()
