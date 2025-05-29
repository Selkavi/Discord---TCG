import random
from models import Card

inventory = []

def collecting():
    collected_card = Card.random_card()
    inventory.append(collected_card)
    if collected_card.rarity == "Uncommon":
        print(f"You drew the card: {collected_card.name}! This is an {collected_card.rarity} card.")
    elif collected_card.rarity == "Rare":
        print(f"You drew the card: {collected_card.name}! This is a {collected_card.rarity} card.")
    elif collected_card.rarity == "Epic":
        print(f"Oh wow, you drew {collected_card.name}! This is a very {collected_card.rarity} card!")
    else:
        print(f"You drew {collected_card.name}. (Rarity: {collected_card.rarity})")