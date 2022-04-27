from discord.ext import commands
import  requests

class Crypto(commands.Cog):
    """Works with Crypto"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="crypto")
    async def binance(self, ctx, coin, base):
        # https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")
            if price:
                await ctx.send(f"O valor do par {coin.upper()}/{base.upper()} é: " + str(
                    price) + f" {base.upper()}\nJá dá para me comprar um presuntinho fumado! Ou preferes chumbar a ES2?HEHE")
            else:
                await ctx.send("PAR INVALIDO!")
        except:
            await ctx.send("API não disponivel no momento 😢")


def setup(bot):
    bot.add_cog(Crypto(bot))
