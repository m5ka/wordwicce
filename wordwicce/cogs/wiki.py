from discord import Embed
from discord.ext import commands

from ..data.wiki import Wiki


class WikiCog(commands.Cog, name="wiki commands"):
    def __init__(self, bot):
        self.bot = bot
        self.data = Wiki()

    @commands.command(description="returns a short wiki excerpt")
    async def wiki(self, ctx, *, query: str = None):
        if not query:
            return await ctx.send("you need to tell me what you're looking for!")
        response = self.data.search(query)
        if not response:
            return await ctx.send("sorry! i couldn't find that on the wiki.")
        return await ctx.send(embed=response.to_embed())
