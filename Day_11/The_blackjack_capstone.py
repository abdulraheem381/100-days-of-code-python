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

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Returns the total score. Adjusts Ace from 11 to 1 if needed."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(user_score, computer_score):
    """Compares user and computer scores and returns result."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

while True:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game != 'y':
        print("See you next time!")
        break

    print(banner)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
