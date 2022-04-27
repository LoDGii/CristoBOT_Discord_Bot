from discord.ext import commands
from decouple import config


bot = commands.Bot('!')

bot.load_extension("commands.crypto")
bot.load_extension("commands.math")
bot.load_extension("commands.reactions")
bot.load_extension("commands.talks")

TOKEN = config("TOKEN")
bot.run(TOKEN)