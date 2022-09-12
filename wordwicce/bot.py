from discord.ext import commands

from .cogs.misc import MiscCog
from .cogs.rune import RuneCog
from .cogs.wiki import WikiCog
from .settings import local


class WordwicceBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__("w!", **kwargs)
        self.add_cog(MiscCog(self))
        self.add_cog(RuneCog(self))
        self.add_cog(WikiCog(self))

    async def on_ready(self):
        print(f"Logged in as {self.user} on {len(self.guilds)} servers!")

    async def on_command_error(self, ctx, exception):
        if isinstance(exception, commands.errors.CommandNotFound):
            return
        return await super().on_command_error(ctx, exception)


def run():
    bot = WordwicceBot()
    bot.run(local.DISCORD_TOKEN)
