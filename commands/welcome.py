from discord.ext import commands
import random


class Welcome(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_messages = [f"Bons olhos te vejam @{member.name}! Então, ainda não leste o enunciado mas precisas de ajuda com o tpc?", f"Então {member.name}? Já experimentaste desligar e voltar a ligar?", f"Welcome to Hell {member.name}"]

        await self.bot.get_channel(704381418309943306).send(welcome_messages[random.randint(0, 2)])
def setup(bot):
    bot.add_cog(Welcome(bot))
