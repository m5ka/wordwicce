from discord.ext import commands


class DictionaryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bt(self, ctx, query):
        pass
