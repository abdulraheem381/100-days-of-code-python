import random

banner = r"""
 ____  _            _        _            _    
| __ )| | __ _  ___| | __   (_) __ _  ___| | __
|  _ \| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <    | | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\  _/ |\__,_|\___|_|\_\
                          |__/                

┌────────────┐   ┌────────────┐
│ A♠        │   │ K♥        │
│            │   │            │
│            │   │            │
│     ♠      │   │     ♥      │
│            │   │            │
│            │   │            │
│        A♠ │   │        K♥ │
└────────────┘   └────────────┘

           BLACK JACK CAPSTONE
"""



game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if game == 'n':
    print("See you next time!")
    exit()
else:
    print(banner)    

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# User Cards Choice 

cards_owned = []
cards_owned_by_computer = []

your_cards = random.sample(cards, 2)
cards_owned.extend(your_cards)

    
current_score = sum(your_cards)


print(f"\tYour cards: {your_cards}, current score: {current_score}")

# Computer Choice 


computer_cards = random.choice(cards)
cards_owned_by_computer.append(computer_cards)

print(f"\tComputer's first card: {computer_cards}")


# let's begin

choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

def add_card():
    new_card = random.choice(cards)
    cards_owned.append(new_card)


if choice == 'y':
    add_card()    
else:
    print(f"\tYour Final hand: {cards_owned}, final score: {sum(cards_owned)}")
    exit()

print(f"\tYour cards: {cards_owned}, current score: {sum(cards_owned)}")

print(f"\tComputer's first card: {computer_cards}")









