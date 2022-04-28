from discord.ext import commands
import asyncio




class Nospam(commands.Cog):
    """Anti-Spam measures"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        cooldown = commands.CooldownMapping.from_cooldown(10, 10, commands.BucketType.member)
        if msg.author.bot:
            return
        if "Silenciado" in str(msg.author.roles):
            await msg.delete()
            return


def setup(bot):
    bot.add_cog(Nospam(bot))