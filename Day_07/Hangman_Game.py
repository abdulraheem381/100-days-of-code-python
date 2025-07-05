import random

# 🎮 Game Title Banner
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                      

        🐍 100 Days of Code - Hangman Game
-------------------------------------------------
""")

stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

lives = 6

word_list = [
    "camel", "bird", "lake", "germany", "candle", "python", "jungle", "rocket", "planet", "guitar",
    "flower", "window", "stream", "hunter", "island", "bridge", "castle", "dragon", "engine", "forest",
    "gloves", "helmet", "insect", "jacket", "kitten", "laptop", "mirror", "needle", "orange", "pencil",
    "quartz", "rabbit", "silver", "tunnel", "vacuum", "whales", "zombie", "banana", "clouds", "dancer",
    "empire", "fabric", "galaxy", "hammer", "icebox", "jungle", "karate", "legend", "magnet", "napkin",
    "oxygen", "parrot", "quiver", "rocket", "saddle", "temple", "utopia", "velvet", "wizard", "yogurt",
    "anchor", "butter", "crayon", "domino", "eagle", "fossil", "goblin", "harbor", "ignite", "jigsaw",
    "kernel", "lizard", "meteor", "nachos", "oracle", "pirate", "quokka", "rescue", "shield", "talent",
    "unicorn", "violet", "walnut", "xenons", "yellow", "zenith", "blazer", "chisel", "decode", "ethics",
    "fusion", "grapes", "hazard", "icicle", "jester", "klaxon", "lantern", "mantis", "napper", "onyx"
]

chosen_word = random.choice(word_list)

# For debugging, you can uncomment this
# print("DEBUG: The word is", chosen_word)

placeholder = "_" * len(chosen_word)
print("Word to guess:", " ".join(placeholder))

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    # Check if letter was guessed before
    if guess in guessed_letters:
        print(f"⚠️ You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    display = ""
    wrong_guess = True

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            wrong_guess = False
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if wrong_guess:
        lives -= 1
        print(f"❌ Wrong guess! You lost a life. Lives remaining: {lives}")
    else:
        print(f"✅ Good guess!")

    print("Word: ", " ".join(display))
    print(stages[6 - lives])
    print(f"📌 Letters guessed so far: {', '.join(sorted(guessed_letters))}")

    placeholder = display

    if "_" not in display:
        game_over = True
        print("""
       __     ______  _    _   _      ____   __     __
       \ \   / / __ \| |  | | | |    / __ \  \ \   / /
        \ \_/ / |  | | |  | | | |   | |  | |  \ \_/ / 
         \   /| |  | | |  | | | |   | |  | |   \   /  
          | | | |__| | |__| | | |___| |__| |    | |   
          |_|  \____/ \____/  |______\____/     |_|   

             🎉 CONGRATULATIONS! YOU WON!
""")
        break

    if lives == 0:
        game_over = True
        print("""
     _____                         ____                 
    / ____|                       |  _ \                
   | |  __  __ _ _ __ ___   ___   | |_) | __ _ ___  ___ 
   | | |_ |/ _` | '_ ` _ \ / _ \  |  _ < / _` / __|/ _ \\
   | |__| | (_| | | | | | |  __/  | |_) | (_| \__ \  __/
    \_____|\__,_|_| |_| |_|\___|  |____/ \__,_|___/\___|
                                                        
             💀 GAME OVER - You Were Hanged!
""")
        print(f"🔤 The word was: {chosen_word}")
