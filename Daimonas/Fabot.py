import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

bot.load_extension("commands.mestre")
bot.load_extension("commands.adm")
bot.load_extension("commands.geral")
bot.load_extension("events.bot")
bot.load_extension("events.manager")

bot.run('MTAyNDY2NjY1MTc1ODcxMDg5Ng.GjIqe9.TTj7TJxcQWY2IvJaBPgeJhrbp1tzHCPm2EnlCI')
