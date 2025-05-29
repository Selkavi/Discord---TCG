import json
import random
from dataclasses import dataclass
from typing import ClassVar, List, Dict, Optional

@dataclass
class Card:
    id: str
    name: str
    rarity: str
    value: int

    # interne Kartenliste + Gewichtung
    _cards: ClassVar[List[Dict]] = []
    _weights: ClassVar[Dict[str,int]] = {
        "Common": 75,
        "Rare":   20,
        "Epic":    5
    }

    @classmethod
    def load_cards(cls, path: str = "data/cards.json"):
        if not cls._cards:
            with open(path, encoding="utf-8") as f:
                cls._cards = json.load(f)

    @classmethod
    def random_card(cls) -> "Card":
        cls.load_cards()
        choice = random.choices(
            population=cls._cards,
            weights=[cls._weights.get(c["rarity"],0) for c in cls._cards],
            k=1
        )[0]
        return Card(**choice)

    @classmethod
    def get_by_id(cls, card_id: str) -> Optional["Card"]:
        cls.load_cards()
        for data in cls._cards:
            if data["id"] == card_id:
                return Card(**data)
        return None


@dataclass
class User:
    discord_id: str
    # hier ggf. weitere Felder, z.B. currency, deck, score etc.


@dataclass
class TradeRequest:
    from_id: str
    to_id:   str
    offer_id: str
    want_id:  str
    status:   str  # pending / accepted / declined
