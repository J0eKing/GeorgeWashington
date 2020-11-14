import discord
from discord.ext.commands import Bot

dictionary = {}

def readtomap():
    print("loaded")
    with open("stats.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            pos = line.find('::')
            name = line[:pos]
            num = line[pos+2:]
            dictionary[name] = int(num)

def addtofile(d={}):
    with open("stats.txt", "w") as f:
        for i in d:
            f.write(i + "::" + str(d[i]) + "\n")

def increaseuser(user):
    if user in dictionary.keys():
        dictionary[user] += 1
    else:
        dictionary[user] = 1

bot = Bot(command_prefix='.')


ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
readtomap()
mess = "This is the {} time you've messaged the bot on the wrong fucking discord channel. You fucking donkey. The #bot channel exists for a fucking reason"

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('Nekopara'))
    print(f'Bot connected as {bot.user}')
    
	
@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    print(message)

    if message.content.startswith('.'):
        await message.channel.send('Hello!')

    if message.content.startswith('!play'):
        if message.channel.name == "general":
            increaseuser(message.author.name)
            addtofile(dictionary)
            await message.channel.send(mess.format(ordinal(dictionary[message.author.name])))

TOKEN = os.getenv('TOKEN')		
bot.run(TOKEN)
