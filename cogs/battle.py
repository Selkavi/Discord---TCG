import discord
from discord.ext import commands
from discord import app_commands
import random
from models import Card
from db import get_db

class Battle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="duel", description="Duelliere dich mit einem Gegner.")
    @app_commands.describe(opponent="Tagge deinen Gegner")
    async def duel(self, interaction: discord.Interaction, opponent: discord.Member):
        # Inventories laden
        db = await get_db()
        cur1 = await db.execute(
            "SELECT card_id FROM inventory WHERE discord_id = ?",
            (str(interaction.user.id),)
        )
        cur2 = await db.execute(
            "SELECT card_id FROM inventory WHERE discord_id = ?",
            (str(opponent.id),)
        )
        rows1 = await cur1.fetchall()
        rows2 = await cur2.fetchall()
        await db.close()

        if not rows1 or not rows2:
            return await interaction.response.send_message("Beide Spieler brauchen mindestens eine Karte im Inventar!")

        # Random aus der Inventory ziehen
        card1 = Card.get_by_id(random.choice(rows1)[0])
        card2 = Card.get_by_id(random.choice(rows2)[0])

        # Embed mit den gezogenen Karten
        embed = discord.Embed(title="Duel")
        embed.add_field(name=interaction.user.display_name,
                        value=f"{card1.name} (Wert {card1.value})", inline=True)
        embed.add_field(name=opponent.display_name,
                        value=f"{card2.name} (Wert {card2.value})", inline=True)
        await interaction.response.send_message(embed=embed)

        # Gewinner bestimmen und Score updaten
        if card1.value > card2.value:
            winner = interaction.user
        elif card2.value > card1.value:
            winner = opponent
        else:
            winner = None

        if winner:
            # Score-Tabelle in db, falls du die nutzt
            db = await get_db()
            await db.execute(
                "INSERT OR IGNORE INTO scores(discord_id) VALUES (?)",
                (str(winner.id),)
            )
            await db.execute(
                "UPDATE scores SET wins = wins + 1 WHERE discord_id = ?",
                (str(winner.id),)
            )
            await db.commit()
            await db.close()
            await interaction.followup.send(f"🏅 **{winner.display_name}** gewinnt das Duell!")
        else:
            await interaction.followup.send("🤝 Unentschieden!")

async def setup(bot):
    await bot.add_cog(Battle(bot))
