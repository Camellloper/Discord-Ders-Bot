from config import *
import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, members=True, reactions=True, presences=True)
bot = commands.Bot(command_prefix=PREFIX,intents=intents)

f = open("token.txt", "r")
TOKEN = f.read()

bot.run(TOKEN)

