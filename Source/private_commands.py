import discord
from discord.ext import commands
from main import bot

@bot.command()
@commands.has_any_role("admin")
async def load(ctx, extension):
    if ctx.channel.id == 947123434314412044:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('Komut çalıştı.')

@bot.command()
@commands.has_any_role("admin")
async def unload(ctx, extension):
    if ctx.channel.id == 947123434314412044:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send('Komut çalıştı.')

@bot.command()
@commands.has_any_role("admin")
async def reload(ctx, extension):
    if ctx.channel.id == 947123434314412044:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('Komut çalıştı.')

