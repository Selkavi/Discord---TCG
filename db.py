from discord.ext import commands
from discord import app_commands
from models import Card
from db import get_db

class Draw(commands.Cog):
    @app_commands.command(name="draw", description="Ziehe eine Karte")
    async def draw(self, interaction):
        card = Card.random_card()
        # … save to DB, respond with Embed …
