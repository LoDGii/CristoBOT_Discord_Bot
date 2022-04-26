# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import discord
import random


token = "XXXXXXXXXXX"#INSERT YOUR DISCORD TOKEN HERE
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'Balle?':
            await message.channel.send("Balle!")
        elif message.content == '?nivel':
            await message.author.send("Qual nivel seu burro? Isto não tem niveis!")

            async def on_member_join(self,member):
                guild = member.guild
                if guild.system_channel is not None:
                    mensagem = f'Bons olhos te vejam {message.author.name}! Não, HTML não é uma linguagem de progamação, ok?'
                    await guild.system_channel.send(mensagem)




intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(token)