import discord
from discord.ext import commands
from discord import app_commands
from models import Card
from db import get_db

class Draw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="draw", description="Ziehe eine zufällige Karte.")
    async def draw(self, interaction: discord.Interaction):
        # Karte ziehen
        card = Card.random_card()

        # In DB speichern
        db = await get_db()
        await db.execute(
            "INSERT OR IGNORE INTO users(discord_id) VALUES (?)",
            (str(interaction.user.id),)
        )
        await db.execute(
            "INSERT INTO inventory(discord_id, card_id) VALUES (?, ?)",
            (str(interaction.user.id), card.id)
        )
        await db.commit()
        await db.close()

        # Embed bauen und senden
        embed = discord.Embed(
            title=card.name,
            description=f"Seltenheit: **{card.rarity}**"
        )
        embed.add_field(name="Wert", value=str(card.value), inline=True)
        # optional, falls du image_url in deinen Cards hast
        if getattr(card, "image_url", None):
            embed.set_image(url=card.image_url)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Draw(bot))
