import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert to mils
    await ctx.send(f'Pong! 🏓 {latency}ms')


bot.run('MTM1NDk5MTYyMjQ3MTAyNDY5MQ.GAffDk.h9doTPfOaLRkNtqMAgl6Ks1r4om3OwiCG-SsIk')
