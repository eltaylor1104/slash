import os

import discord
import dislash
import jishaku
from discord.ext import commands
from dislash import *
from dotenv import load_dotenv

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    @slash_commands.command(name="ban", guild_ids=test_ids, description="Ban a user", options=[
        Option("user", "Specify a user to ban.", Type.USER, required=True),
        Option("reason", "specify a reason", Type.STRING, required=False)
        ])
    @slash_commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, user, reason = None):
        await user.ban(reason = reason)
        await ctx.create_response(f"{user} has been banned.", ephemeral=True)


    @slash_commands.command(name="kick", guild_ids=test_ids, description="Kick a user", options=[
        Option("user", "Specify a user to kick.", Type.USER, required=True),
        Option("reason", "specify a reason", Type.STRING, required=False)
        ])
    @slash_commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, user, reason = None):
        await user.kick(reason = reason)
        await ctx.create_response(f"{user} has been kicked.", ephemeral=True)

    @slash_commands.command(name="purge", description="Purge a given amount of messages", guild_ids=test_ids, options=[Option("amount", "amount of messages to purge", Type.INTEGER, required=True)])
    @slash_commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, amount):
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'Cleared {amount} messages.', ephemeral=True)







def setup(bot):
    bot.add_cog(mod(bot))
