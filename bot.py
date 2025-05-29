import os
import discord
from discord.ext import commands
from db import init_db

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    await init_db()
    await bot.tree.sync()
    print("Ready")

for cog in ["draw","battle","inventory","trade"]:
    bot.load_extension(f"cogs.{cog}")

bot.run(os.getenv("DISCORD_TOKEN"))
