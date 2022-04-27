from discord.ext import commands

class Reactions(commands.Cog):
    """Works with reactions"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        Channel = self.bot.get_channel(968519147480809493)
        Text = "Roles"
        Moji = await Channel.send(Text)
        await Moji.add_reaction('1️⃣')
        await Moji.add_reaction('2️⃣')
        await Moji.add_reaction('3️⃣')
        await Moji.add_reaction('4️⃣')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        Channel = self.bot.get_channel(968519147480809493)
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


def setup(bot):
    bot.add_cog(Reactions(bot))
