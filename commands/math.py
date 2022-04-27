from discord.ext import commands

class Math(commands.Cog):
    """Works with math"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calcular")
    async def calculate(self, ctx, expression):
        response = eval(expression)
        await ctx.send("Resultado: " + str(response))

def setup(bot):
    bot.add_cog(Math(bot))
