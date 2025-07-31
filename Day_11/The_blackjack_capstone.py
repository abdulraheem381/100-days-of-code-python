import random

banner = r"""
 ____  _            _        _            _    
| __ )| | __ _  ___| | __   (_) __ _  ___| | __
|  _ \| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <    | | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\  _/ |\__,_|\___|_|\_\
                          |__/                

┌────────────┐   ┌────────────┐
│ A♠         │   │ K♥         │
│            │   │            │
│            │   │            │
│     ♠      │   │     ♥      │
│            │   │            │
│            │   │            │
│        A♠  │   │        K♥  │
└────────────┘   └────────────┘

           BLACK JACK CAPSTONE
"""

while True:
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if game == 'n':
        print("See you next time!")
        exit()
    else:
        print(banner)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    cards_owned_by_user = []
    cards_owned_by_computer = []
    current_user_score = 0
    current_comp_score = 0

    def user_2_cards_choice():
        user_cards = random.sample(cards, 2)
        cards_owned_by_user.extend(user_cards)
        return user_cards

    def user_1_card_choice():
        new_card = random.choice(cards)
        cards_owned_by_user.append(new_card)
        return new_card

    def comp_1_card():
        new_card = random.choice(cards)
        cards_owned_by_computer.append(new_card)
        return new_card

    def comp_hidden_choice():
        hidden_card = random.choice(cards)
        cards_owned_by_computer.append(hidden_card)
        return hidden_card

    def add_user_cards():
        return sum(cards_owned_by_user)

    def add_comp_cards():
        return sum(cards_owned_by_computer)
    
    user_2_cards_choice()
    current_user_score = add_user_cards()

    print(f"\tYour cards: {cards_owned_by_user}, current score: {current_user_score}")

    comp_1_card()

    print(f"\tComputer's first card: {cards_owned_by_computer}")

   








    




