import discord
from discord.ext import commands
from discord import app_commands
from models import Card
from db import get_db

class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="inventory", description="Zeige deine gesammelten Karten.")
    async def inventory(self, interaction: discord.Interaction):
        db = await get_db()
        cursor = await db.execute(
            "SELECT card_id FROM inventory WHERE discord_id = ?",
            (str(interaction.user.id),)
        )
        rows = await cursor.fetchall()
        await db.close()

        if not rows:
            return await interaction.response.send_message("Du hast noch keine Karten gezogen!")

        # Baue eine Liste als Embed-Description
        lines = []
        for (card_id,) in rows:
            card = Card.get_by_id(card_id)
            lines.append(f"- **{card.name}** (#{card.id}, {card.rarity}, Wert {card.value})")

        embed = discord.Embed(
            title=f"{interaction.user.display_name}’s Karten",
            description="\n".join(lines)
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Inventory(bot))
