from discord.ext import commands

class Talks(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Balle")
    async def send_balle(self, ctx):
        name = ctx.author.name
        response = "Balle!"
        await ctx.send(response)

    @commands.command(name="ajuda")
    async def help(self, ctx):
        await ctx.author.send("https://jpst.it/2PAhs")
def setup(bot):
    bot.add_cog(Talks(bot))
