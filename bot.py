import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

bot.load_extension("commands.welcome")
bot.load_extension("music")
bot.load_extension("commands.crypto")
bot.load_extension("commands.math")
bot.load_extension("commands.reactions")
bot.load_extension("commands.talks")

TOKEN = config("TOKEN")
bot.run(TOKEN)