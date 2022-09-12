from discord.ext import commands

from ..data.rune import Rune, RuneDatabase


class RuneCog(commands.Cog, name="rune commands"):
    def __init__(self, bot):
        self.bot = bot
        self.db = RuneDatabase.construct()

    @commands.command(description="returns information on a rune")
    async def rune(self, ctx, *, query: str = None):
        if not query:
            rune = self.db.random()
            return await ctx.send(embed=rune.embed)
        rune = self.db.search(query)
        if not rune:
            return await ctx.send("sorry, I couldn't find that rune.")
        else:
            return await ctx.send(embed=rune.embed)

    @commands.command(description="returns a list of runes")
    async def runes(self, ctx):
        return await ctx.send(self.db.discord_string)
