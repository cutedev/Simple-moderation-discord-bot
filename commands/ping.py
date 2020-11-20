import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"PONG🏓 **{round(self.bot.latency * 1000)}**ms")


def setup(bot):
    bot.add_cog(Ping(bot))
    
   # Note this is in cogs. Dm me for help Jack Sparrow#4442.
