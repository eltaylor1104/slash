import os

import discord
import dislash
import jishaku
from discord.ext import commands
from dislash import *
from dotenv import load_dotenv
from jishaku.codeblocks import Codeblock, codeblock_converter

load_dotenv()


bot = commands.Bot(intents=discord.Intents.all(), command_prefix="b!", help_command=None)
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array



DISCORDTOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready():
    print('BonBot is ready :D')

    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{servers} servers and {members} members'
    ))



@bot.command(name="update", hidden=True)
@commands.is_owner()
async def update(ctx):
	updater = bot.get_command("jsk git")
	await updater(ctx, argument=Codeblock("https://github.com/eltaylor1104/bonbot", "pull"))
	bot.unload_extension('cogs.mod')
	bot.load_extension('cogs.mod')
	bot.unload_extension('cogs.utility')
	bot.load_extension('cogs.utility')
	bot.unload_extension('cogs.general')
	bot.load_extension('cogs.general')
	bot.unload_extension('cogs.reddit')
	bot.load_extension('cogs.reddit')

@slash.event
async def on_slash_command_error(ctx, error):
	await ctx.send(f'{error}', ephemeral=True)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.load_extension('jishaku')
bot.run(DISCORDTOKEN)
