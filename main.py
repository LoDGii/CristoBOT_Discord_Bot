import os
import discord
import random
import requests
from discord.ext import commands, tasks
from decouple import config


bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f"CONECTADO COM SUCESSO!\nBem Vindo ao mundo {bot.user}!")

@bot.command(name = "Balle")
async def send_balle(ctx):
    name = ctx.author.name
    response = "Balle!"
    await ctx.send(response)

@bot.command(name = "calcular")
async def calculate(ctx, expression):
    response = eval(expression)
    await ctx.send("Resultado: " + str(response))

@bot.command(name = "crypto")
async def binance(ctx, coin, base):
    #https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
        data = response.json()
        price = data.get("price")
        if price:
            await ctx.send(f"O valor do par {coin.upper()}/{base.upper()} é: " + str(price) + f" {base.upper()}\nJá dá para me comprar um presuntinho fumado! Ou preferes chumbar a ES2?HEHE")
        else:
            await ctx.send("PAR INVALIDO!")
    except:
        await ctx.send("API não disponivel no momento 😢")

@bot.command(name = "ajuda")
async def help(ctx):
    await ctx.author.send("https://jpst.it/2PAhs")



@bot.event
async def on_ready():
    Channel = bot.get_channel(968519147480809493)
    Text= "Roles"
    Moji = await Channel.send(Text)
    await Moji.add_reaction('1️⃣')
    await Moji.add_reaction('2️⃣')
    await Moji.add_reaction('3️⃣')
    await Moji.add_reaction('4️⃣')

@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    Channel = bot.get_channel(968519147480809493)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "1️⃣":
        role = user.guild.get_role(968992230767464468)
        await user.add_roles(role)
    elif reaction.emoji == "2️⃣":
        role = user.guild.get_role(968992330680004679)
        await user.add_roles(role)
    elif reaction.emoji == "3️⃣":
        role = user.guild.get_role(968992446149189722)
        await user.add_roles(role)
    elif reaction.emoji == "4️⃣":
        role = user.guild.get_role(968992582388576306)
        await user.add_roles(role)







TOKEN = config("TOKEN")
bot.run(TOKEN)