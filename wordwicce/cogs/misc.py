from discord.ext import commands


class MiscCog(commands.Cog, name="miscellaneous"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hello, stranger. i'm glad we could both be here today.")

    @commands.command()
    async def thanks(self, ctx):
        await ctx.send("no problem! i hope our meeting again may be woven into wyrd.")

    @commands.command()
    async def wyrd(self, ctx):
        await ctx.send("> **gǽð á wyrd swá hío sceal**\n> wyrd goes ever as she must")
