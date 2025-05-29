import os
import discord
from discord.ext import commands
from discord import app_commands
from db import init_db

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await init_db()
    print(f"Bot eingeloggt als {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Slash-Commands synchronisiert: {len(synced)}")
    except Exception as e:
        print(f"Sync-Fehler: {e}")

for fname in ["draw", "battle", "inventory", "trade"]:
    bot.load_extension(f"cogs.{fname}")

bot.run(os.getenv("DISCORD_TOKEN"))
