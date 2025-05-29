import discord
from discord.ext import commands
from discord import app_commands
from models import TradeRequest
from db import get_db

class Trade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="trade", description="Starte einen Karten-Tausch.")
    @app_commands.describe(
        opponent="Tagge deinen Tauschpartner",
        offer="ID der Karte, die du anbietest",
        want="ID der Karte, die du haben möchtest"
    )
    async def trade(self, interaction: discord.Interaction, opponent: discord.Member, offer: str, want: str):
        # TradeRequest in DB schreiben
        db = await get_db()
        await db.execute(
            "INSERT INTO trades(from_id, to_id, offer_id, want_id, status) VALUES (?, ?, ?, ?, 'pending')",
            (str(interaction.user.id), str(opponent.id), offer, want)
        )
        await db.commit()
        await db.close()
        await interaction.response.send_message(
            f"🔄 Tausch-Anfrage #{interaction.id} gesendet: Du gibst `{offer}`, willst `{want}` von {opponent.mention}."
        )

    @app_commands.command(name="trade_accept", description="Akzeptiere eine Tausch-Anfrage.")
    @app_commands.describe(trade_id="ID der Tausch-Anfrage")
    async def trade_accept(self, interaction: discord.Interaction, trade_id: int):
        db = await get_db()
        # Anfrage validieren und Status ändern…
        await db.execute(
            "UPDATE trades SET status = 'accepted' WHERE rowid = ? AND to_id = ?",
            (trade_id, str(interaction.user.id))
        )
        await db.commit()
        await db.close()
        await interaction.response.send_message(f"✅ Tausch #{trade_id} akzeptiert!")

async def setup(bot):
    await bot.add_cog(Trade(bot))
