import random, json, sys
from models import Card
from pathlib import Path

inventory = []
battle_deck = []
player2 = Card.random_card()

base_dir = Path(__file__).parent
cards_path = base_dir / "data" / "cards.json"
with cards_path.open("r", encoding="utf-8") as f:
    cards = json.load(f)

#card varity is in models.py

#collect a random card:

def collecting():
    collected_card = Card.random_card()
    inventory.append(collected_card)
    if collected_card.rarity == "Uncommon":
        print(f"You drew {collected_card.name}. (Rarity: {collected_card.rarity})")
    elif collected_card.rarity == "Rare":
        print(f"You drew {collected_card.name}. (Rarity: {collected_card.rarity})")
    elif collected_card.rarity == "Epic":
        print(f"Oh wow, you drew {collected_card.name}! This is a very {collected_card.rarity} card!")
    else:
        print(f"You drew {collected_card.name}. (Rarity: {collected_card.rarity})")

# too lazy to write collection() n times lmao

for _ in range(5):
    collecting()

print()

#----------------------------duel preperation----------------------------------------------------------


print("------------Duel preperations are loading------------")

print()

print("I added the collected cards to your battle deck. Thank me later.")

print()

battle_deck.extend(inventory)

# checks if there are enough or too much cards in the battle deck
print("------------Checking if you have enough or too much cards in your battle deck------------")

print()

num_cards = len(battle_deck)

if num_cards < 5:
    print("You need at least 5 cards to play!")
elif num_cards > 10:
    print("You can have a maximum of 10 cards in your deck.")
else:
    print("You have the right number of cards to play.")

print("Gonna check real quick if you don't have too much epic or rare cards in your battle deck. One sec.")

rare_count = battle_deck.count("Rare")
epic_count = battle_deck.count("Epic")
check_epic_count = False
check_rare_count = False

# Rare-Limits
if num_cards == 5:
    if rare_count > 1:
        print(f"You can't have more than one rare card in your {num_cards}-card deck.")
    else:
        print("Rare cards are okay.")
        check_rare_count = True
elif num_cards >= 7 and num_cards < 10:
    if rare_count > 2:
        print(f"You can't have more than two rare cards in your {num_cards}-card deck.")
    else:
        print("Rare cards are okay.")
        check_rare_count = True
elif num_cards >= 10:
    if rare_count > 3:
        print(f"You can't have more than three rare cards in your {num_cards}-card deck.")
    else:
        print("Rare cards are okay.")
        check_rare_count = True
else:
    print("No rare cards in your battle deck?! I think that means this error.")

# Epic-Limit
if epic_count > 1:
    print(f"You can't have more than one epic card in your {num_cards}-card deck.")
else:
    print("Epic cards are okay.")
    check_epic_count = True

#checks if you actually have the right amount of cards. Otherwise exits the program.
if not check_rare_count and not check_epic_count:
    print("Nice try. Exiting Programm")
    sys.exit(1)

print()
print("------------Continuing------------")

#--------------------------------dueling---------------------------------------------------
print()
print("------------Player 2 is drawing a card------------")
print()
print("------------You are drawing your card------------")
print()
def draw_card():
    return random.choice(cards)

def compare_cards():
    c1 = draw_card()
    c2 = draw_card()
    print(f"Player 1: {c1['name']} (Wert {c1['value']})")
    print(f"Player 2: {c2['name']} (Wert {c2['value']})")

    if c1["value"] > c2["value"]:
        print("Player 1 wins!")
    elif c1["value"] < c2["value"]:
        print("Player 2 wins!")
    else:
        print("Unentschieden!")

draw_card()
compare_cards()

