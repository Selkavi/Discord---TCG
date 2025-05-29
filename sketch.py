import random
from models import Card

inventory = []
battle_deck = []

#card varity is in models.py

#collect a random card:

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

#too lazy to write collection() n times lmao

for _ in range(11):
    collecting()

#I don't tell anyone that this function exists if you don't........
def spacing():
    print()
    print()

spacing()

#duel preperation

print("I added the collected cards to your battle deck. Thank me later.")

spacing()

battle_deck.extend(inventory)

#checks if there are enough or too much cards in the battle deck

num_cards = len(battle_deck)

if num_cards < 5:
    print("You need at least 5 cards to play!")
elif num_cards >= 5:
    print("You have the minimum amount to play.")
elif num_cards >= 10:
    print("You can have a maximum of 10 cards in your deck.")
else:
    print("Pretty sure nothing is wrong with your deck. Definitly. Most likely.")



def duel ():
    Card.load_cards("data/cards.json")
    card1 = Card.random_cards()
    card2 = Card.random_cards()








