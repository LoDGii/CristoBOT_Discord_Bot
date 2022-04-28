import discord
from discord.ext import commands
from decouple import config
#import music
#cogs = [music]
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
#for i in range(len(cogs)):
    #cogs[i].setup(bot)

bot.load_extension("music")
bot.load_extension("commands.crypto")
bot.load_extension("commands.math")
bot.load_extension("commands.reactions")
bot.load_extension("commands.talks")

TOKEN = config("TOKEN")
bot.run(TOKEN)