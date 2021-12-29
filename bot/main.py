import os

import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

discord_token = os.getenv("BOT_TOKEN")

intent = discord.Intents.default()
intent.members = True
client = commands.Bot(command_prefix="yo ", intents=intent)

@client.event
async def on_ready():
    print("Mercury is ready")

@commands.has_permissions(administrator=True)
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("{} module is now enable".format(extension))

@commands.has_permissions(administrator=True)
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("{} module is now disable".format(extension))

@commands.has_permissions(administrator=True)
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("{} module has been reloaded".format(extension))


for filename in os.listdir('./bot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(discord_token)